from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union
from typing_extensions import Required, TypedDict


import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI, NexonOpenAPIAsync


class KartRiderRushPlus(SyncAPIResource):
    """
    link: https://openapi.nexon.com/game/kartrush/?id=11&shallow=true

    - 크레이지 아케이드의 게임 데이터는 평균 10분 후 확인 가능합니다.
    - 2022년 1월 1일 이후 데이터를 조회할 수 있습니다. (단, 2022년 1월 이전에 발생한 데이터는 응답 결과에 포함되지 않을 수 있음)
    - 게임 콘텐츠 변경으로 ouid가 변경될 수 있습니다. ouid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
    """

    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ouid(
        self,
        *,
        racer_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> OuidInfo:
        """계정 식별자(ouid)를 조회합니다.

        라이더(계정) 명에 특수문자 '|'를 포함하는 경우 '_'로 변환 후 입력해주시길 바랍니다.
        예시) |카러플라이더| → _카러플라이더_
        """
        return self._get(
            "kartrush/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"racer_name": racer_name},
                    GetOuidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=OuidInfo,
        )

    def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> KartRiderRushPlushUserBasic:
        return self._get(
            path="kartrush/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KartRiderRushPlushUserBasic,
        )

    def get_user_title_equipment(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> KartRiderRushPlushUserTitleEquipment:
        return self._get(
            path="kartrush/v1/user/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KartRiderRushPlushUserTitleEquipment,
        )


class KartRiderRushPlusAsync(AsyncAPIResource):
    """
    link: https://openapi.nexon.com/game/kartrush/?id=11&shallow=true

    - 크레이지 아케이드의 게임 데이터는 평균 10분 후 확인 가능합니다.
    - 2022년 1월 1일 이후 데이터를 조회할 수 있습니다. (단, 2022년 1월 이전에 발생한 데이터는 응답 결과에 포함되지 않을 수 있음)
    - 게임 콘텐츠 변경으로 ouid가 변경될 수 있습니다. ouid 기반 서비스 갱신 시 유의해 주시길 바랍니다.
    """

    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ouid(
        self,
        *,
        racer_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> OuidInfo:
        """계정 식별자(ouid)를 조회합니다.

        라이더(계정) 명에 특수문자 '|'를 포함하는 경우 '_'로 변환 후 입력해주시길 바랍니다.
        예시) |카러플라이더| → _카러플라이더_
        """
        return await self._get(
            "kartrush/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"racer_name": racer_name},
                    GetOuidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=OuidInfo,
        )

    async def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> KartRiderRushPlushUserBasic:
        return await self._get(
            path="kartrush/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KartRiderRushPlushUserBasic,
        )

    async def get_user_title_equipment(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> KartRiderRushPlushUserTitleEquipment:
        return await self._get(
            path="kartrush/v1/user/title-equipment",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserTitleEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=KartRiderRushPlushUserTitleEquipment,
        )


class GetOuidRequestParam(TypedDict, total=True):
    racer_name: Required[str]


class OuidInfo(BaseModel):
    ouid_info: List[_Inner]

    class _Inner(BaseModel):
        ouid: str
        racer_date_create: str
        racer_level: str


class GetUserBasicRequestParam(TypedDict, total=False):
    ouid: Required[str]


class KartRiderRushPlushUserBasic(BaseModel):
    racer_name: str
    """계정 명"""

    racer_date_create: str
    """계정 생성 일(시) (UTC0)"""

    racer_date_last_login: str
    """계정 마지막 로그인 일(시) (UTC0)"""

    racer_date_last_logout: str
    """계정 마지막 로그아웃 일(시) (UTC0)"""

    racer_level: int
    """계정 레벨"""


class GetUserTitleEquipmentRequestParam(TypedDict, total=False):
    ouid: Required[str]


class KartRiderRushPlushUserTitleEquipment(BaseModel):
    title_equipment: List[Title]

    class Title(BaseModel):
        title_name: Optional[str]
        """ 칭호 명 """
