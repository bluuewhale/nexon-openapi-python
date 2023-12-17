from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union
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


class V4(SyncAPIResource):
    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ocid(
        self,
        *,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = self._get(
            "v4/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"character_name": character_name},
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
    ) -> V4CharacterBasic:
        return self._get(
            path="v4/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterBasic,
        )

    def get_character_honor(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> V4CharacterHonor:
        return self._get(
            path="v4/v1/character/honor",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterHonorRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterHonor,
        )

    def get_character_honor_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> V4CharacterHonorEquipment:
        return self._get(
            path="v4/v1/character/honor-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterHonorEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterHonorEquipment,
        )


class V4Async(AsyncAPIResource):
    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ocid(
        self,
        *,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "v4/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"character_name": character_name},
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
    ) -> V4CharacterBasic:
        return await self._get(
            path="v4/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterBasic,
        )

    async def get_character_honor(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> V4CharacterHonor:
        return await self._get(
            path="v4/v1/character/honor",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterHonorRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterHonor,
        )

    async def get_character_honor_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> V4CharacterHonorEquipment:
        return await self._get(
            path="v4/v1/character/honor-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterHonorEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V4CharacterHonorEquipment,
        )


class GetOcidRequestParam(TypedDict, total=True):
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class V4CharacterBasic(BaseModel):
    server_name: str
    """ 서버 명 """

    character_name: str
    """ 캐릭터 명 """

    character_date_create: str
    """ 캐릭터 생성 일(시) (UTC0) """

    character_create_type: str
    """ 캐릭터 생성 타입 (0:일반 캐릭터, 1:점핑 캐릭터) """

    character_date_last_login: str
    """ 캐릭터 마지막 로그인 일(시) (UTC0) """

    character_date_last_logout: str
    """ 캐릭터 마지막 로그아웃 일(시) (UTC0) """

    character_class_name: str
    """캐릭터 직업 명"""

    character_level: int
    """ 캐릭터 레벨 """


class GetCharacterHonorRequestParam(TypedDict, total=False):
    ocid: Required[str]


class V4CharacterHonor(BaseModel):
    honor: List[Honor]

    class Honor(BaseModel):
        honor_type_name: str
        """ 명예 타입 명 """

        honor_name: str
        """ 명예 명 """

        date_expire: str
        """ 명예 만료 일(시) (UTC0) """


class GetCharacterHonorEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class V4CharacterHonorEquipment(BaseModel):
    honor_equipment: List[HonorEquipment]

    class HonorEquipment(BaseModel):
        honor_type_name: str
        """ 장착 명예 타입 명 """

        honor_name: str
        """ 장착 명예 명 """

        date_expire: str
        """ 장착 명예 만료 일(시) (UTC0) """
