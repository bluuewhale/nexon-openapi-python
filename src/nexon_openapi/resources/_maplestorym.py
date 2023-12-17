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


class MapleStoryM(SyncAPIResource):
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
            "maplestorym/v1/id",
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
    ) -> MapleStoryMCharacterBasic:
        return self._get(
            path="maplestorym/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterBasic,
        )

    def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterItemEquipment:
        return self._get(
            path="maplestorym/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterItemEquipment,
        )

    def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterStat:
        return self._get(
            path="maplestorym/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterStat,
        )

    def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterGuild:
        return self._get(
            path="maplestorym/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterGuild,
        )


class MapleStoryMAsync(AsyncAPIResource):
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
            "maplestorym/v1/id",
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
    ) -> MapleStoryMCharacterBasic:
        return await self._get(
            path="maplestorym/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterBasic,
        )

    async def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterItemEquipment:
        return await self._get(
            path="maplestorym/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterItemEquipment,
        )

    async def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterStat:
        return await self._get(
            path="maplestorym/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterStat,
        )

    async def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryMCharacterGuild:
        return await self._get(
            path="maplestorym/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryMCharacterGuild,
        )


class GetOcidRequestParam(TypedDict, total=True):
    world_name: Required[str]
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MapleStoryMCharacterBasic(BaseModel):
    character_name: str
    """ 캐릭터 명 """

    world_name: str
    """ 월드 명 """

    character_date_create: str
    """ 캐릭터 생성 일(시) (UTC0) """

    character_date_last_login: str
    """ 캐릭터 마지막 로그인 일(시) (UTC0) """

    character_date_last_logout: str
    """ 캐릭터 마지막 로그아웃 일(시) (UTC0) """

    character_job_name: str
    """캐릭터 직업 명"""

    character_gender: str
    """ 캐릭터 성별 """

    character_level: int
    """ 캐릭터 레벨 """

    character_exp: int
    """ 캐릭터 경험치 """


class GetCharacterItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MapleStoryMCharacterItemEquipment(BaseModel):
    item_equipment: List[Item]

    class Item(BaseModel):
        item_name: str
        """ 장착 아이템 명 """

        item_equipment_page_name: str
        """ 장착 아이템 페이지 명 """

        item_equipment_slot_name: str
        """ 장착 아이템 페이지 내 슬롯 명 """


class GetCharacterStatRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MapleStoryMCharacterStat(BaseModel):
    stat: List[Stat]

    class Stat(BaseModel):
        stat_name: str
        """ 스탯 명 """

        stat_value: str
        """ 스탯 값 """


class GetCharacterGuildRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MapleStoryMCharacterGuild(BaseModel):
    guild_name: str
