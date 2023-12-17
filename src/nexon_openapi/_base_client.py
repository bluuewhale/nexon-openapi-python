from __future__ import annotations
import asyncio

import email
import email.utils
import json
import logging
from random import random
import time
from types import TracebackType
from typing import (
    TypeVar,
    Union,
    Any,
    Dict,
    Generic,
    Mapping,
    Optional,
    Type,
    cast,
)
import anyio

import httpx

from ._constants import DEFAULT_MAX_RETRIES, DEFAULT_LIMITS, DEFAULT_TIMEOUT
from ._types import (
    NotGiven,
    ResponseT,
    Query,
    Body,
    NOT_GIVEN,
    Omit,
    Headers,
    RequestOptions,
    PostParser,
    AnyMapping,
)
from .utils import is_given, is_mapping
from ._models import FinalRequestOptions
from ._compat import model_dump
from ._qs import Querystring
from ._response import APIResponse
from ._exceptions import APIConnectionError, APIStatusError, APITimeoutError

try:
    from httpx._config import DEFAULT_TIMEOUT_CONFIG as HTTPX_DEFAULT_TIMEOUT
except ImportError:
    # taken from https://github.com/encode/httpx/blob/3ba5fe0d7ac70222590e759c31442b1cab263791/httpx/_config.py#L366
    HTTPX_DEFAULT_TIMEOUT = httpx.Timeout(5.0)  # type: ignore

log = logging.getLogger(__name__)

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_HttpxClientT = TypeVar("_HttpxClientT", bound=Union[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[_HttpxClientT]):
    _client: _HttpxClientT
    max_retries: int
    timeout: Union[float, httpx.Timeout, None]
    _limits: httpx.Limits

    def __init__(
        self,
        *,
        version: str,
        base_url: Union[str, httpx.URL],
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, httpx.Timeout, None] = DEFAULT_TIMEOUT,
        limits: httpx.Limits = DEFAULT_LIMITS,
        strict_response_validation: bool = True,
        custom_headers: Union[Mapping[str, str], None] = None,
        custom_query: Union[Mapping[str, object], None] = None,
    ) -> None:
        self._version = version
        self._base_url = httpx.URL(base_url)
        self.max_retries = max_retries
        self.timeout = timeout
        self._limits = limits
        self._strict_response_validation = strict_response_validation
        self._custom_headers = custom_headers or {}
        self._custom_query = custom_query or {}
        self._idempotency_header = None

    @property
    def qs(self) -> Querystring:
        return Querystring()

    def _enforce_trailing_slash(self, url: httpx.URL) -> httpx.URL:
        if url.raw_path.endswith(b"/"):
            return url
        return url.copy_with(raw_path=url.raw_path + b"/")

    def _make_status_error_from_response(
        self,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.is_closed and not response.is_stream_consumed:
            # We can't read the response body as it has been closed
            # before it was read. This can happen if an event hook
            # raises a status error.
            body = None
            err_msg = f"Error code: {response.status_code}"
        else:
            err_text = response.text.strip()
            body = err_text

            try:
                body = json.loads(err_text)
                err_msg = f"Error code: {response.status_code} - {body}"
            except Exception:
                err_msg = err_text or f"Error code: {response.status_code}"

        return self._make_status_error(err_msg, body=body, response=response)

    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        raise NotImplementedError()

    def _remaining_retries(
        self,
        remaining_retries: Optional[int],
        options: FinalRequestOptions,
    ) -> int:
        return remaining_retries if remaining_retries is not None else options.get_max_retries(self.max_retries)

    def _build_headers(self, options: FinalRequestOptions) -> httpx.Headers:
        custom_headers = options.headers or {}
        headers_dict = _merge_mappings(self.default_headers, custom_headers)
        self._validate_headers(headers_dict, custom_headers)

        # headers are case-insensitive while dictionaries are not.
        return httpx.Headers(headers_dict)

    def _prepare_url(self, url: str) -> httpx.URL:
        """
        Merge a URL argument together with any 'base_url' on the client,
        to create the URL used for the outgoing request.
        """
        # Copied from httpx's `_merge_url` method.
        merge_url = httpx.URL(url)
        if merge_url.is_relative_url:
            merge_raw_path = self.base_url.raw_path + merge_url.raw_path.lstrip(b"/")
            return self.base_url.copy_with(raw_path=merge_raw_path)

        return merge_url

    def _build_request(
        self,
        options: FinalRequestOptions,
    ) -> httpx.Request:
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Request options: %s", model_dump(options, exclude_unset=True))

        kwargs: dict[str, Any] = {}

        json_data = options.json_data
        if options.extra_json is not None:
            if json_data is None:
                json_data = cast(Body, options.extra_json)
            elif is_mapping(json_data):
                json_data = _merge_mappings(json_data, options.extra_json)
            else:
                raise RuntimeError(f"Unexpected JSON data type, {type(json_data)}, cannot merge with `extra_body`")

        headers = self._build_headers(options)
        params = _merge_mappings(self._custom_query, options.params)

        return self._client.build_request(
            headers=headers,
            timeout=self.timeout if isinstance(options.timeout, NotGiven) else options.timeout,
            method=options.method,
            url=self._prepare_url(options.url),
            params=self.qs.stringify(params) if params else None,  # type: ignore
            json=json_data,
            **kwargs,
        )

    def _process_response(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        response: httpx.Response,
    ) -> ResponseT:
        api_response = APIResponse(
            raw=response,
            cast_to=cast_to,
            strict_response_validation=self._strict_response_validation,
            options=options,
        )

        return api_response.parse()

    @property
    def custom_auth(self) -> Optional[httpx.Auth]:
        return None

    @property
    def auth_headers(self) -> Dict[str, str]:
        return {}

    @property
    def default_headers(self) -> Dict[str, Union[str, Omit]]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
            **self.auth_headers,
            **self._custom_headers,
        }

    def _validate_headers(
        self,
        headers: Headers,  # noqa: ARG002
        custom_headers: Headers,  # noqa: ARG002
    ) -> None:
        """Validate the given default headers and custom headers.

        Does nothing by default.
        """
        return

    @property
    def user_agent(self) -> str:
        return f"{self.__class__.__name__}/Python {self._version}"

    @property
    def base_url(self) -> httpx.URL:
        return self._base_url

    @base_url.setter
    def base_url(self, url: Union[httpx.URL, str]) -> None:
        self._base_url = self._enforce_trailing_slash(url if isinstance(url, httpx.URL) else httpx.URL(url))

    def _calculate_retry_timeout(
        self,
        remaining_retries: int,
        options: FinalRequestOptions,
        response_headers: Optional[httpx.Headers] = None,
    ) -> float:
        max_retries = options.get_max_retries(self.max_retries)
        try:
            # About the Retry-After header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After
            #
            # <http-date>". See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After#syntax for
            # details.
            if response_headers is not None:
                retry_header = response_headers.get("retry-after")
                try:
                    retry_after = float(retry_header)
                except Exception:
                    retry_date_tuple = email.utils.parsedate_tz(retry_header)
                    if retry_date_tuple is None:
                        retry_after = -1
                    else:
                        retry_date = email.utils.mktime_tz(retry_date_tuple)
                        retry_after = int(retry_date - time.time())
            else:
                retry_after = -1

        except Exception:
            retry_after = -1

        # If the API asks us to wait a certain amount of time (and it's a reasonable amount), just do what it says.
        if 0 < retry_after <= 60:
            return retry_after

        initial_retry_delay = 0.5
        max_retry_delay = 8.0
        nb_retries = max_retries - remaining_retries

        # Apply exponential backoff, but not more than the max.
        sleep_seconds = min(initial_retry_delay * pow(2.0, nb_retries), max_retry_delay)

        # Apply some jitter, plus-or-minus half a second.
        jitter = 1 - 0.25 * random()
        timeout = sleep_seconds * jitter
        return timeout if timeout >= 0 else 0

    def _should_retry(self, response: httpx.Response) -> bool:
        # TODO: read response header and decide whether to retry or not

        # Retry on request timeouts.
        if response.status_code == 408:
            return True

        # Retry on lock timeouts.
        if response.status_code == 409:
            return True

        # Retry on rate limits.
        if response.status_code == 429:
            return True

        # Retry internal errors.
        if response.status_code >= 500:
            return True

        return False


class SyncHttpxClientWrapper(httpx.Client):
    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


class SyncAPIClient(BaseClient[httpx.Client]):
    _client: httpx.Client

    def __init__(
        self,
        *,
        version: str,
        base_url: Union[str, httpx.URL],
        limits: httpx.Limits,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = None,
        http_client: Union[httpx.Client, None] = None,
        custom_headers: Union[Mapping[str, str], None] = None,
        custom_query: Union[Mapping[str, object], None] = None,
        strict_response_validation: bool,
    ) -> None:
        if not is_given(timeout):
            # if the user passed in a custom http client with a non-default
            # timeout set then we use that timeout.
            #
            # note: there is an edge case here where the user passes in a client
            # where they've explicitly set the timeout to match the default timeout
            # as this check is structural, meaning that we'll think they didn't
            # pass in a timeout and will ignore it
            if http_client and http_client.timeout != HTTPX_DEFAULT_TIMEOUT:
                timeout = http_client.timeout
            else:
                timeout = DEFAULT_TIMEOUT

        super().__init__(
            version=version,
            limits=limits,
            timeout=timeout,
            base_url=base_url,
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
            strict_response_validation=strict_response_validation,
        )

        self._client = http_client or SyncHttpxClientWrapper(
            base_url=base_url,
            timeout=timeout,
            limits=limits,
        )

    def is_closed(self) -> bool:
        return self._client.is_closed

    def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        # If an error is thrown while constructing a client, self._client
        # may not be present
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        self.close()

    def _prepare_options(
        self,
        options: FinalRequestOptions,  # noqa: ARG002
    ) -> None:
        """Hook for mutating the given options"""
        return None

    def _prepare_request(
        self,
        request: httpx.Request,  # noqa: ARG002
    ) -> None:
        """This method is used as a callback for mutating the `Request` object
        after it has been constructed.
        This is useful for cases where you want to add certain headers based off of
        the request properties, e.g. `url`, `method` etc.
        """
        return None

    def request(
        self,
        *,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        remaining_retries: Optional[int] = None,
    ) -> ResponseT:
        return self._request(
            cast_to=cast_to,
            options=options,
            remaining_retries=remaining_retries,
        )

    def _request(
        self,
        *,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        remaining_retries: Optional[int],
    ) -> ResponseT:
        self._prepare_options(options)

        retries = self._remaining_retries(remaining_retries, options)
        request = self._build_request(options)
        self._prepare_request(request)

        try:
            response = self._client.send(
                request,
                auth=self.custom_auth,
            )
        except httpx.TimeoutException as err:
            if retries > 0:
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    response_headers=None,
                )

            raise APITimeoutError(request=request) from err
        except Exception as err:
            if retries > 0:
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    response_headers=None,
                )

            raise APIConnectionError(request=request) from err

        log.debug(
            'HTTP Request: %s %s "%i %s"',
            request.method,
            request.url,
            response.status_code,
            response.reason_phrase,
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            if retries > 0 and self._should_retry(err.response):
                err.response.close()
                return self._retry_request(
                    options,
                    cast_to,
                    retries,
                    err.response.headers,
                )

            # If the response is streamed then we need to explicitly read the response
            # to completion before attempting to access the response text.
            if not err.response.is_closed:
                err.response.read()

            raise self._make_status_error_from_response(err.response) from None

        return self._process_response(
            cast_to=cast_to,
            options=options,
            response=response,
        )

    def _retry_request(
        self,
        options: FinalRequestOptions,
        cast_to: Type[ResponseT],
        remaining_retries: int,
        response_headers: Optional[httpx.Headers],
    ) -> ResponseT:
        remaining = remaining_retries - 1
        timeout = self._calculate_retry_timeout(remaining, options, response_headers)
        log.info("Retrying request to %s in %f seconds", options.url, timeout)

        # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
        # different thread if necessary.
        time.sleep(timeout)

        return self._request(
            options=options,
            cast_to=cast_to,
            remaining_retries=remaining,
        )

    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="get", url=path, **options)
        # cast is required because mypy complains about returning Any even though
        # it understands the type variables
        return self.request(cast_to=cast_to, options=opts)

    def post(
        self,
        path: str,
        cast_to: Type[ResponseT],
        body: Optional[Body] = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="post", url=path, json_data=body, **options)
        return self.request(cast_to=cast_to, options=opts)

    def patch(
        self,
        path: str,
        cast_to: Type[ResponseT],
        body: Optional[Body] = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="patch", url=path, json_data=body, **options)
        return self.request(cast_to=cast_to, options=opts)

    def put(
        self,
        path: str,
        cast_to: Type[ResponseT],
        body: Optional[Body] = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="put", url=path, json_data=body, **options)
        return self.request(cast_to=cast_to, options=opts)

    def delete(
        self,
        path: str,
        cast_to: Type[ResponseT],
        body: Optional[Body] = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="delete", url=path, json_data=body, **options)
        return self.request(cast_to=cast_to, options=opts)


def make_request_options(
    *,
    query: Optional[Query] = None,
    extra_headers: Optional[Headers] = None,
    extra_query: Optional[Query] = None,
    extra_body: Optional[Body] = None,
    idempotency_key: Optional[str] = None,
    timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    post_parser: Union[PostParser, NotGiven] = NOT_GIVEN,
) -> RequestOptions:
    """Create a dict of type RequestOptions without keys of NotGiven values."""
    options: RequestOptions = {}
    if extra_headers is not None:
        options["headers"] = extra_headers

    if extra_body is not None:
        options["extra_json"] = cast(AnyMapping, extra_body)

    if query is not None:
        options["params"] = query

    if extra_query is not None:
        options["params"] = {**options.get("params", {}), **extra_query}

    if not isinstance(timeout, NotGiven):
        options["timeout"] = timeout

    if idempotency_key is not None:
        options["idempotency_key"] = idempotency_key

    if is_given(post_parser):
        # internal
        options["post_parser"] = post_parser  # type: ignore

    return options


def _merge_mappings(
    obj1: Mapping[_T_co, Union[_T, Omit]],
    obj2: Mapping[_T_co, Union[_T, Omit]],
) -> Dict[_T_co, _T]:
    """Merge two mappings of the same type, removing any values that are instances of `Omit`.

    In cases with duplicate keys the second mapping takes precedence.
    """
    merged = {**obj1, **obj2}
    return {key: value for key, value in merged.items() if not isinstance(value, Omit)}


class AsyncHttpxClientWrapper(httpx.AsyncClient):
    def __del__(self) -> None:
        try:
            asyncio.get_running_loop().create_task(self.aclose())
        except Exception:
            pass


class AsyncAPIClient(BaseClient[httpx.AsyncClient]):
    _client: httpx.AsyncClient

    def __init__(
        self,
        *,
        version: str,
        base_url: Union[str, httpx.URL],
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        limits: Optional[httpx.Limits] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        custom_headers: Optional[Mapping[str, str]] = None,
        custom_query: Optional[Mapping[str, object]] = None,
        strict_response_validation: bool,
    ) -> None:
        limits = DEFAULT_LIMITS if limits is None else limits

        if not is_given(timeout):
            # if the user passed in a custom http client with a non-default
            # timeout set then we use that timeout.
            #
            # note: there is an edge case here where the user passes in a client
            # where they've explicitly set the timeout to match the default timeout
            # as this check is structural, meaning that we'll think they didn't
            # pass in a timeout and will ignore it
            if http_client and http_client.timeout != HTTPX_DEFAULT_TIMEOUT:
                timeout = http_client.timeout
            else:
                timeout = DEFAULT_TIMEOUT

        super().__init__(
            version=version,
            base_url=base_url,
            limits=limits,
            # cast to a valid type because mypy doesn't understand our type narrowing
            timeout=cast(httpx.Timeout, timeout),
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
            strict_response_validation=strict_response_validation,
        )

        self._client = http_client or AsyncHttpxClientWrapper(
            base_url=base_url,
            # cast to a valid type because mypy doesn't understand our type narrowing
            timeout=cast(httpx.Timeout, timeout),
            limits=limits,
        )

    def is_closed(self) -> bool:
        return self._client.is_closed

    async def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        await self._client.aclose()

    async def __aenter__(self: _T) -> _T:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def _prepare_options(
        self,
        options: FinalRequestOptions,  # noqa: ARG002
    ) -> None:
        """Hook for mutating the given options"""
        return None

    async def _prepare_request(
        self,
        request: httpx.Request,  # noqa: ARG002
    ) -> None:
        """This method is used as a callback for mutating the `Request` object
        after it has been constructed.
        This is useful for cases where you want to add certain headers based off of
        the request properties, e.g. `url`, `method` etc.
        """
        return None

    async def request(
        self, cast_to: Type[ResponseT], options: FinalRequestOptions, *, remaining_retries: Optional[int] = None
    ) -> ResponseT:
        await self._prepare_options(options)

        retries = self._remaining_retries(remaining_retries, options)
        request = self._build_request(options)
        await self._prepare_request(request)

        try:
            response = await self._client.send(
                request,
                auth=self.custom_auth,
            )
        except httpx.TimeoutException as err:
            if retries > 0:
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    response_headers=None,
                )

            raise APITimeoutError(request=request) from err
        except Exception as err:
            if retries > 0:
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    response_headers=None,
                )

            raise APIConnectionError(request=request) from err

        log.debug(
            'HTTP Request: %s %s "%i %s"', request.method, request.url, response.status_code, response.reason_phrase
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            if retries > 0 and self._should_retry(err.response):
                await err.response.aclose()
                return await self._retry_request(
                    options,
                    cast_to,
                    retries,
                    err.response.headers,
                )

            # If the response is streamed then we need to explicitly read the response
            # to completion before attempting to access the response text.
            if not err.response.is_closed:
                await err.response.aread()

            raise self._make_status_error_from_response(err.response) from None

        return self._process_response(
            cast_to=cast_to,
            options=options,
            response=response,
        )

    async def _retry_request(
        self,
        options: FinalRequestOptions,
        cast_to: Type[ResponseT],
        remaining_retries: int,
        response_headers: httpx.Headers | None,
    ) -> ResponseT:
        remaining = remaining_retries - 1
        timeout = self._calculate_retry_timeout(remaining, options, response_headers)
        log.info("Retrying request to %s in %f seconds", options.url, timeout)

        await anyio.sleep(timeout)

        return await self.request(
            options=options,
            cast_to=cast_to,
            remaining_retries=remaining,
        )

    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="get", url=path, **options)
        return await self.request(cast_to, opts)

    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="post", url=path, json_data=body, **options)
        return await self.request(cast_to, opts)

    async def patch(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="patch", url=path, json_data=body, **options)
        return await self.request(cast_to, opts)

    async def put(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="put", url=path, json_data=body, **options)
        return await self.request(cast_to, opts)

    async def delete(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        opts = FinalRequestOptions.construct(method="delete", url=path, json_data=body, **options)
        return await self.request(cast_to, opts)
