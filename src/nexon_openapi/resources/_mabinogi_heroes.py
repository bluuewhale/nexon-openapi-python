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

__all__ = ["MabinogiHeroes", "MabinogiHeroesCharacterBasic"]


class MabinogiHeroes(SyncAPIResource):
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
            "heroes/v1/id",
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
    ) -> MabinogiHeroesCharacterBasic:
        return self._get(
            path="heroes/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterBasic,
        )

    def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterTitle:
        return self._get(
            path="heroes/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterTitle,
        )

    def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterTitleEquipment:
        return self._get(
            path="heroes/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterTitleEquipment,
        )

    def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterItemEquipment:
        return self._get(
            path="heroes/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterItemEquipment,
        )

    def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterStat:
        return self._get(
            path="heroes/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterStat,
        )

    def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterGuild:
        return self._get(
            path="heroes/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterGuild,
        )


class MabinogiHeroesAsync(AsyncAPIResource):
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
            "heroes/v1/id",
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
    ) -> MabinogiHeroesCharacterBasic:
        return await self._get(
            path="heroes/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterBasic,
        )

    async def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterTitle:
        return await self._get(
            path="heroes/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterTitle,
        )

    async def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterTitleEquipment:
        return await self._get(
            path="heroes/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterTitleEquipment,
        )

    async def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterItemEquipment:
        return await self._get(
            path="heroes/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterItemEquipment,
        )

    async def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterStat:
        return await self._get(
            path="heroes/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterStat,
        )

    async def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterGuild:
        return await self._get(
            path="heroes/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterGuild,
        )


class GetOcidRequestParam(TypedDict, total=True):
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterBasic(BaseModel):
    character_name: str
    """ 영웅(캐릭터) 명 """

    character_date_create: str
    """ 영웅(캐릭터) 생성 일(시) (UTC0) """

    character_last_login: str
    """ 영웅(캐릭터) 마지막 로그인 일(시) (UTC0) """

    character_last_logout: str
    """ 영웅(캐릭터) 마지막 로그아웃 일(시) (UTC0) """

    character_class_name: str
    """영웅(캐릭터) 직업 명"""

    character_gender: str
    """ 영웅(캐릭터) 성별 """

    character_level: int
    """ 영웅(캐릭터) 레벨 """

    character_exp: int
    """ 영웅(캐릭터) 경험치 """


class GetCharacterTitleRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterTitle(BaseModel):
    title: List[Title]

    class Title(BaseModel):
        title_type: str
        """타이틀 타입 (title:타이틀, pattern:문양)"""

        title_name: str
        """타이틀/문양 명"""


class GetCharacterTitleEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterTitleEquipment(BaseModel):
    title_equipment: List[TitleEquipment]

    class TitleEquipment(BaseModel):
        title_equipment_type_name: str
        """장착 타이틀/문양 장착 위치 명"""

        title_type: str
        """타이틀 타입 (title:타이틀, pattern:문양)"""

        title_name: str
        """타이틀/문양 명"""


class GetCharacterItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterItemEquipment(BaseModel):
    item_equipment: List[ItemEquipment]

    class ItemEquipment(BaseModel):
        item_equipment_page: str
        """장착 아이템 장착 페이지 (Bag:장착소지품, Cash:캐시소지품)"""

        item_equipment_slot_name: str
        """장착 아이템 슬롯 명"""

        item_name: str
        """장착 아이템 명"""


class GetCharacterStatRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterStat(BaseModel):
    stat: List[Stat]

    class Stat(BaseModel):
        stat_id: str
        """능력치 명"""

        stat_value: str
        """능력치 값"""


class GetCharacterGuildRequestParam(TypedDict, total=False):
    ocid: Required[str]


class MabinogiHeroesCharacterGuild(BaseModel):
    guild_name: str
    """가입/신청한 길드 명"""
