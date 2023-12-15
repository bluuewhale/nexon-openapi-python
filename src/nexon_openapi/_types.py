from __future__ import annotations

from abc import ABC, abstractmethod
from os import PathLike
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncIterator,
    Callable,
    Dict,
    Iterator,
    List,
    Mapping,
    Optional,
    Set,
    Type,
    TypeVar,
    Union,
)
from typing_extensions import Literal, TypedDict, override, runtime_checkable, Protocol

from httpx import Response, Timeout
import pydantic

if TYPE_CHECKING:
    from ._models import BaseModel


_T = TypeVar("_T")
Query = Mapping[str, object]
Body = object
AnyMapping = Mapping[str, object]
ModelT = TypeVar("ModelT", bound=pydantic.BaseModel)
StrBytesIntFloat = Union[str, bytes, int, float]
IncEx = Union[Set[int], Set[str], Dict[int, Any], Dict[str, Any], None]


if TYPE_CHECKING:
    NoneType: Type[None]
else:
    NoneType = type(None)


class Omit:
    """In certain situations you need to be able to represent a case where a default value has
    to be explicitly removed and `None` is not an appropriate substitute, for example:

    ```py
    # as the default `Content-Type` header is `application/json` that will be sent
    client.post('/upload/files', files={'file': b'my raw file content'})

    # you can't explicitly override the header as it has to be dynamically generated
    # to look something like: 'multipart/form-data; boundary=0d8382fcf5f8c3be01ca2e11002d2983'
    client.post(..., headers={'Content-Type': 'multipart/form-data'})

    # instead you can remove the default `application/json` header by passing Omit
    client.post(..., headers={'Content-Type': Omit()})
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False


OMIT = Omit()


class HeadersLikeProtocol(Protocol):
    def get(self, __key: str) -> Optional[str]:
        ...


Headers = Mapping[str, Union[str, Omit]]
HeadersLike = Union[Headers, HeadersLikeProtocol]


# Sentinel class used when the response type is an object with an unknown schema
class UnknownResponse:
    ...


# Sentinel class used until PEP 0661 is accepted
class NotGiven:
    """
    A sentinel singleton class used to distinguish omitted keyword arguments
    from those passed in with the value None (which may have different behavior).

    For example:

    ```py
    def get(timeout: Union[int, NotGiven, None] = NotGiven()) -> Response: ...

    get(timeout=1) # 1s timeout
    get(timeout=None) # No timeout
    get() # Default timeout behavior, which may not be statically known at the method definition.
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


NotGivenOr = Union[_T, NotGiven]
NOT_GIVEN = NotGiven()

ResponseT = TypeVar(
    "ResponseT",
    bound="Union[str, None, BaseModel, List[Any], Dict[str, Any], Response, UnknownResponse]",
)


class RequestOptions(TypedDict, total=False):
    headers: Headers
    max_retries: int
    timeout: Union[float, Timeout, None]
    params: Query
    extra_json: AnyMapping
    idempotency_key: str


PostParser = Callable[[Any], Any]


class BinaryResponseContent(ABC):
    @abstractmethod
    def __init__(
        self,
        response: Any,
    ) -> None:
        ...

    @property
    @abstractmethod
    def content(self) -> bytes:
        pass

    @property
    @abstractmethod
    def text(self) -> str:
        pass

    @property
    @abstractmethod
    def encoding(self) -> Optional[str]:
        """
        Return an encoding to use for decoding the byte content into text.
        The priority for determining this is given by...

        * `.encoding = <>` has been set explicitly.
        * The encoding as specified by the charset parameter in the Content-Type header.
        * The encoding as determined by `default_encoding`, which may either be
          a string like "utf-8" indicating the encoding to use, or may be a callable
          which enables charset autodetection.
        """
        pass

    @property
    @abstractmethod
    def charset_encoding(self) -> Optional[str]:
        """
        Return the encoding, as specified by the Content-Type header.
        """
        pass

    @abstractmethod
    def json(self, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    def read(self) -> bytes:
        """
        Read and return the response content.
        """
        pass

    @abstractmethod
    def iter_bytes(self, chunk_size: Optional[int] = None) -> Iterator[bytes]:
        """
        A byte-iterator over the decoded response content.
        This allows us to handle gzip, deflate, and brotli encoded responses.
        """
        pass

    @abstractmethod
    def iter_text(self, chunk_size: Optional[int] = None) -> Iterator[str]:
        """
        A str-iterator over the decoded response content
        that handles both gzip, deflate, etc but also detects the content's
        string encoding.
        """
        pass

    @abstractmethod
    def iter_lines(self) -> Iterator[str]:
        pass

    @abstractmethod
    def iter_raw(self, chunk_size: Optional[int] = None) -> Iterator[bytes]:
        """
        A byte-iterator over the raw response content.
        """
        pass

    @abstractmethod
    def stream_to_file(
        self,
        file: Union[str, PathLike[str]],
        *,
        chunk_size: Optional[int] = None,
    ) -> None:
        """
        Stream the output to the given file.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Close the response and release the connection.
        Automatically called if the response body is read to completion.
        """
        pass

    @abstractmethod
    async def aread(self) -> bytes:
        """
        Read and return the response content.
        """
        pass

    @abstractmethod
    async def aiter_bytes(self, chunk_size: Optional[int] = None) -> AsyncIterator[bytes]:
        """
        A byte-iterator over the decoded response content.
        This allows us to handle gzip, deflate, and brotli encoded responses.
        """
        pass

    @abstractmethod
    async def aiter_text(self, chunk_size: Optional[int] = None) -> AsyncIterator[str]:
        """
        A str-iterator over the decoded response content
        that handles both gzip, deflate, etc but also detects the content's
        string encoding.
        """
        pass

    @abstractmethod
    async def aiter_lines(self) -> AsyncIterator[str]:
        pass

    @abstractmethod
    async def aiter_raw(self, chunk_size: Optional[int] = None) -> AsyncIterator[bytes]:
        """
        A byte-iterator over the raw response content.
        """
        pass

    @abstractmethod
    async def astream_to_file(
        self,
        file: Union[str, PathLike[str]],
        *,
        chunk_size: Optional[int] = None,
    ) -> None:
        """
        Stream the output to the given file.
        """
        pass

    @abstractmethod
    async def aclose(self) -> None:
        """
        Close the response and release the connection.
        Automatically called if the response body is read to completion.
        """
        pass


@runtime_checkable
class ModelBuilderProtocol(Protocol):
    @classmethod
    def build(
        cls: Type[_T],
        *,
        response: Response,
        data: object,
    ) -> _T:
        ...
