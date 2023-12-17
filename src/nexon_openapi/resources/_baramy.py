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


class BaramY(SyncAPIResource):
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
            "baramy/v1/id",
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
    ) -> BaramYCharacterBasic:
        return self._get(
            path="baramy/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterBasic,
        )

    def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramYCharacterTitle:
        return self._get(
            path="baramy/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterTitle,
        )

    def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramYCharacterTitleEquipment:
        return self._get(
            path="baramy/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterTitleEquipment,
        )


class BaramYAsync(AsyncAPIResource):
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
            "baramy/v1/id",
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
    ) -> BaramYCharacterBasic:
        return await self._get(
            path="baramy/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterBasic,
        )

    async def get_character_title(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramYCharacterTitle:
        return await self._get(
            path="baramy/v1/character/title",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterTitle,
        )

    async def get_character_title_equipment(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> BaramYCharacterTitleEquipment:
        return await self._get(
            path="baramy/v1/character/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=BaramYCharacterTitleEquipment,
        )


class GetOcidRequestParam(TypedDict, total=True):
    server_name: Required[str]
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramYCharacterBasic(BaseModel):
    server_name: str
    """ 서버 명 """

    character_name: str
    """ 캐릭터 명 """

    character_date_create: str
    """ 캐릭터 생성 일(시) (UTC0) """

    character_class_group_name: str
    """캐릭터 직업군 명"""

    character_class_name: str
    """캐릭터 직업 명"""

    character_nation: str
    """ 캐릭터 국적 """

    character_gender: str
    """ 캐릭터 성별 """

    character_level: int
    """ 캐릭터 레벨 """

    character_exp: int
    """ 캐릭터 경험치 """


class GetCharacterTitleRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramYCharacterTitle(BaseModel):
    title: List[Title]

    class Title(BaseModel):
        title_type_name: str
        """ 칭호 타입 명 """

        title_name: str
        """ 칭호 명 """


class GetCharacterTitleEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]


class BaramYCharacterTitleEquipment(BaseModel):
    title_equipment: List[Title]

    class Title(BaseModel):
        title_equipment_type: str
        """ 장착 칭호 장착 타입 (1:장착 칭호, 2:표시 칭호) """

        title_type_name: str
        """ 장착 칭호 타입 명 """

        title_name: str
        """ 장착 칭호 명 """
