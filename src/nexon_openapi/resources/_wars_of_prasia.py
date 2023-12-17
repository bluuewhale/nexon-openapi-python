from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union
from typing_extensions import Required, TypedDict


import httpx

from ._types import Ocid
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI, NexonOpenAPIAsync

__all__ = ["WarsOfPrasia", "WarsOfPrasiaCharacterBasic"]


class WarsOfPrasia(SyncAPIResource):
    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ocid(
        self,
        *,
        world_name: str,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = self._get(
            "wp/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"world_name": world_name, "character_name": character_name},
                    GetOcidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ocid,
        )

        return response.ocid

    def get_character_basic(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> WarsOfPrasiaCharacterBasic:
        return self._get(
            path="wp/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=WarsOfPrasiaCharacterBasic,
        )


class WarsOfPrasiaAsync(AsyncAPIResource):
    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ocid(
        self,
        *,
        world_name: str,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "wp/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"world_name": world_name, "character_name": character_name},
                    GetOcidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ocid,
        )

        return response.ocid

    async def get_character_basic(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> WarsOfPrasiaCharacterBasic:
        return await self._get(
            path="wp/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=WarsOfPrasiaCharacterBasic,
        )


class GetOcidRequestParam(TypedDict, total=True):
    world_name: Required[str]
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class WarsOfPrasiaCharacterBasic(BaseModel):
    realm_name: str
    character_name: str

    character_date_create: str
    """ 캐릭터 생성 일(시) (UTC0) """

    character_date_last_login: str
    """ 캐릭터 마지막 로그인 일(시) (UTC0) """

    character_date_last_logout: str
    """ 캐릭터 마지막 로그아웃 일(시) (UTC0) """

    character_class_name: str
    """캐릭터 직업 명"""

    character_gender: str
    """ 캐릭터 성별 """

    character_level: int
    """ 캐릭터 레벨 """

    character_exp: int
    """ 캐릭터 경험치 """
