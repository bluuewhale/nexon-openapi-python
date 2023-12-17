from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union
from typing_extensions import Required, TypedDict


import httpx

from ._types import Ouid
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI, NexonOpenAPIAsync


class CrazyArcade(SyncAPIResource):
    """
    link: https://openapi.nexon.com/game/ca/?id=12&shallow=true

    - 크레이지 아케이드의 게임 데이터는 평균 10분 후 확인 가능합니다.
    - 2022년 1월 1일 이후 데이터를 조회할 수 있습니다. (단, 2022년 1월 이전에 발생한 데이터는 응답 결과에 포함되지 않을 수 있음)
    - 게임 콘텐츠 변경으로 ouid가 변경될 수 있습니다. ouid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
    """

    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ouid(
        self,
        *,
        user_name: str,
        world_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = self._get(
            "ca/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"world_name": world_name, "user_name": user_name},
                    GetOuidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ouid,
        )

        return response.ouid

    def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserBasic:
        return self._get(
            path="ca/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserBasic,
        )

    def get_user_title(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserTitle:
        return self._get(
            path="ca/v1/user/title",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserTitle,
        )

    def get_user_title_equipment(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserTitleEquipment:
        return self._get(
            path="ca/v1/user/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserTitleEquipment,
        )


class CrazyArcadeAsync(AsyncAPIResource):
    """
    link: https://openapi.nexon.com/game/ca/?id=12&shallow=true

    - 크레이지 아케이드의 게임 데이터는 평균 10분 후 확인 가능합니다.
    - 2022년 1월 1일 이후 데이터를 조회할 수 있습니다. (단, 2022년 1월 이전에 발생한 데이터는 응답 결과에 포함되지 않을 수 있음)
    - 게임 콘텐츠 변경으로 ouid가 변경될 수 있습니다. ouid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
    """

    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ouid(
        self,
        *,
        user_name: str,
        world_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "ca/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"world_name": world_name, "user_name": user_name},
                    GetOuidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ouid,
        )

        return response.ouid

    async def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserBasic:
        return await self._get(
            path="ca/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserBasic,
        )

    async def get_user_title(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserTitle:
        return await self._get(
            path="ca/v1/user/title",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserTitle,
        )

    async def get_user_title_equipment(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CrazyArcadeUserTitleEquipment:
        return await self._get(
            path="ca/v1/user/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=CrazyArcadeUserTitleEquipment,
        )


class GetOuidRequestParam(TypedDict, total=True):
    user_name: Required[str]
    world_name: Required[str]


class GetUserBasicRequestParam(TypedDict, total=False):
    ouid: Required[str]


class CrazyArcadeUserBasic(BaseModel):
    user_name: str
    """계정 명"""

    user_date_create: str
    """계정 생성 일(시) (UTC0)"""

    user_date_last_login: str
    """계정 마지막 로그인 일(시) (UTC0)"""

    user_date_last_logout: str
    """계정 마지막 로그아웃 일(시) (UTC0)"""

    user_exp: int
    """계정 경험치"""

    user_level: int
    """계정 레벨"""


class GetUserTitleRequestParam(TypedDict, total=False):
    ouid: Required[str]


class CrazyArcadeUserTitle(BaseModel):
    title: List[Title]

    class Title(BaseModel):
        title_id: str
        """ 칭호 명 """

        title_grade_name: str
        """ 칭호 등급 명 (event: 획득 한정 칭호) """


class GetUserTitleEquipmentRequestParam(TypedDict, total=False):
    ouid: Required[str]


class CrazyArcadeUserTitleEquipment(BaseModel):
    title_equipment: List[TitleEquip]

    class TitleEquip(BaseModel):
        titme_equipment_type: str
        """ 장착 칭호 타입 (Prefix:접두, Postfix:접미) """

        title_id: str
        """ 장착 칭호 명 """

        title_grade_name: str
        """ 장착 칭호 등급 명 (event:획득 한정 칭호) """
