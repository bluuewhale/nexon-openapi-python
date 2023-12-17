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


class Baram(SyncAPIResource):
    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ocid(
        self,
        *,
        server_name: str,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = self._get(
            "baram/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"server_name": server_name, "character_name": character_name},
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
    ) -> BaramCharacterBasic:
        return self._get(
            path="baram/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterBasic,
        )

    def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterTitle:
        return self._get(
            path="baram/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterTitle,
        )

    def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterTitleEquipment:
        return self._get(
            path="baram/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterTitleEquipment,
        )

    def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterItemEquipment:
        return self._get(
            path="baram/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterItemEquipment,
        )

    def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterStat:
        return self._get(
            path="baram/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterStat,
        )

    def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterGuild:
        return self._get(
            path="baram/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterGuild,
        )


class BaramAsync(AsyncAPIResource):
    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ocid(
        self,
        *,
        server_name: str,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "baram/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"server_name": server_name, "character_name": character_name},
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
    ) -> BaramCharacterBasic:
        return await self._get(
            path="baram/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterBasic,
        )

    async def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterTitle:
        return await self._get(
            path="baram/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterTitle,
        )

    async def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterTitleEquipment:
        return await self._get(
            path="baram/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterTitleEquipment,
        )

    async def get_character_item_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterItemEquipment:
        return await self._get(
            path="baram/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterItemEquipment,
        )

    async def get_character_stat(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterStat:
        return await self._get(
            path="baram/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterStat,
        )

    async def get_character_guild(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramCharacterGuild:
        return await self._get(
            path="baram/v1/character/guild",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterGuildRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramCharacterGuild,
        )


class GetOcidRequestParam(TypedDict, total=True):
    server_name: Required[str]
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterBasic(BaseModel):
    character_name: str
    """ 캐릭터 명 """

    character_date_create: str
    """ 캐릭터 생성 일(시) (UTC0) """

    character_date_last_login: str
    """ 캐릭터 마지막 로그인 일(시) (UTC0) """

    character_date_last_logout: str
    """ 캐릭터 마지막 로그아웃 일(시) (UTC0) """

    character_create_type_name: str
    """ 캐릭터 생성 타입 명 """

    character_class_name: str
    """캐릭터 직업 명"""

    character_nation_name: str
    """캐릭터 국가 명"""

    character_gender: str
    """ 캐릭터 성별 """

    character_level: int
    """ 캐릭터 레벨 """

    character_exp: int
    """ 캐릭터 경험치 """


class GetCharacterTitleRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterTitle(BaseModel):
    title: List[Title]

    class Title(BaseModel):
        title_id: str
        """ 칭호 명 """

        date_expire: Optional[str]
        """ 칭호 만료 일(시) (UTC0) """


class GetCharacterTitleEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterTitleEquipment(BaseModel):
    title_equipment: List[TitleEquipment]

    class TitleEquipment(BaseModel):
        title_id: str
        """ 장착 칭호 명 """

        date_expire: Optional[str]
        """ 칭호 만료 일(시) (UTC0) """


class GetCharacterItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterItemEquipment(BaseModel):
    item_equipment: List[ItemEquipment]

    class ItemEquipment(BaseModel):
        item_id: str
        """ 장착 아이템 명 """

        item_equipment_slot_name: str
        """ 장착 아이템 페이즈 슬롯 명 """


class GetCharacterStatRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterStat(BaseModel):
    stat: List[Stat]

    class Stat(BaseModel):
        stat_name: str
        """ 능력치 명 """

        stat_value: str
        """ 능력치 값 """


class GetCharacterGuildRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramCharacterGuild(BaseModel):
    guild_name: str
    """ 가입판 문파(길드) 명 """
