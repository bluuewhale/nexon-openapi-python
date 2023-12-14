from __future__ import annotations

import os
from typing import Dict, Mapping, Union
from typing_extensions import override

import httpx

from ._base_client import SyncAPIClient
from ._types import NotGiven, NOT_GIVEN, Omit
from ._constants import DEFAULT_MAX_RETRIES, DEFAULT_LIMITS
from ._exceptions import NexonError
from ._qs import Querystring
from .__version__ import __version__
from ._exceptions import *
from .utils import is_mapping
from .resources import WarsOfPrasia


class NexonOpenAPI(SyncAPIClient):
    api_key: str

    wars_of_prasia: WarsOfPrasia

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        limits: httpx.Limits = DEFAULT_LIMITS,
        default_headers: Union[Mapping[str, str], None] = None,
        default_query: Union[Mapping[str, object], None] = None,
        http_client: Union[httpx.Client, None] = None,
        strict_response_validation: bool = True,
    ) -> None:
        """construct a new synchronous nexon openapi client instance

        This automatically infers the following arguments from their corresponding environment variables if they are not provided

        - `api_key` from `NEXON_OPENAPI_API_KEY`
        - `base_url` from `NEXON_OPENAPI_BASE_URL`
        """

        if api_key is None:
            api_key = os.environ.get("NEXON_OPENAPI_API_KEY")
        if api_key is None:
            raise NexonError(
                "The api_key client option must be set either by passing api_key to the client or by setting the NEXON_OPENAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("NEXON_OPENAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://open.api.nexon.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            limits=limits,
            custom_headers=default_headers,
            custom_query=default_query,
            strict_response_validation=strict_response_validation,
        )

        self.wars_of_prasia = WarsOfPrasia(self)

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> Dict[str, str]:
        return {"x-nxopen-api-key": self.api_key}

    @property
    @override
    def default_headers(self) -> Dict[str, Union[str, Omit]]:
        return {
            **super().default_headers,
            **self._custom_headers,
        }
