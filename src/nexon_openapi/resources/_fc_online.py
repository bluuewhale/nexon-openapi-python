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


class FCOnline(SyncAPIResource):
    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ouid(
        self,
        *,
        nickname: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        return self._get(
            "fconline/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"nickname": nickname},
                    GetOuidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ouid,
        ).ouid

    def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserBasic:
        return self._get(
            path="fconline/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=FCOnlineUserBasic,
        )

    def get_user_max_division(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[FCOnlineUserMaxDivision]:
        return self._get(
            path="fconline/v1/user/maxdivision",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserMaxDivisionRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[FCOnlineUserMaxDivision],
        )

    def get_user_match_history(
        self,
        *,
        ouid: str,
        matchtype: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserMatchHistory:
        matches = self._get(
            path="fconline/v1/user/match",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "matchtype": matchtype, "offset": offset, "limit": limit}, GetUserMatchHistoryRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[str],
        )

        return FCOnlineUserMatchHistory(matches=matches)

    def get_user_trade_history(
        self,
        *,
        ouid: str,
        tradetype: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserTradeHistory:
        """
        거래 종류{tradetype}로 유저의 이적시장 거래 종류별 기록을 조회합니다. (본인 거래 기록만 조회 가능)

        유저가 거래한 선수의 아이디와 등급, 가치가 반환됩니다
        반환되는 매치 정보는 가장 최근 거래이력부터 내림차순입니다
        {offset} 과 {limit}을 사용하여 pagination이 가능합니다
        """
        trades = self._get(
            path="fconline/v1/user/trade",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "tradetype": tradetype, "offset": offset, "limit": limit}, GetUserTradeHistoryRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[FCOnlineUserTradeHistory.Trade],
        )

        return FCOnlineUserTradeHistory(trades=trades)

class FCOnlineAsync(AsyncAPIResource):
    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ouid(
        self,
        *,
        nickname: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "fconline/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"nickname": nickname},
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
    ) -> FCOnlineUserBasic:
        return await self._get(
            path="fconline/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=FCOnlineUserBasic,
        )

    async def get_user_max_division(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[FCOnlineUserMaxDivision]:
        return await self._get(
            path="fconline/v1/user/maxdivision",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserMaxDivisionRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[FCOnlineUserMaxDivision],
        )

    async def get_user_match_history(
        self,
        *,
        ouid: str,
        matchtype: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserMatchHistory:
        matches = await self._get(
            path="fconline/v1/user/match",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "matchtype": matchtype, "offset": offset, "limit": limit}, GetUserMatchHistoryRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[str],
        )

        return FCOnlineUserMatchHistory(matches=matches)

    async def get_user_trade_history(
        self,
        *,
        ouid: str,
        tradetype: int,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserTradeHistory:
        """
        거래 종류{tradetype}로 유저의 이적시장 거래 종류별 기록을 조회합니다. (본인 거래 기록만 조회 가능)

        유저가 거래한 선수의 아이디와 등급, 가치가 반환됩니다
        반환되는 매치 정보는 가장 최근 거래이력부터 내림차순입니다
        {offset} 과 {limit}을 사용하여 pagination이 가능합니다
        """
        trades = await self._get(
            path="fconline/v1/user/trade",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "tradetype": tradetype, "offset": offset, "limit": limit}, GetUserTradeHistoryRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[FCOnlineUserTradeHistory.Trade],
        )

        return FCOnlineUserTradeHistory(trades=trades)

class GetOuidRequestParam(TypedDict, total=True):
    nickname: Required[str]

class GetUserBasicRequestParam(TypedDict, total=False):
    ouid: Required[str]


class FCOnlineUserBasic(BaseModel):
    ouid: str
    """계정 식별자"""

    nickname: str
    """유저 닉네임"""

    level: int
    """유저 레벨"""

class GetUserMaxDivisionRequestParam(TypedDict, total=False):
    ouid: Required[Ouid]

class FCOnlineUserMaxDivision(BaseModel):
    matchType: int 
    """ 매치 종류(/metadata/matchtype API 참고) """

    division: int 
    """등급 식별자 (공식경기 /metadata/division API, 볼타모드 /metadata/division_volta API 참고)"""

    achievementDate: str
    """최그 등급 달성 일자 (UTC0)"""


class GetUserMatchHistoryRequestParam(TypedDict, total=False):
    ouid: Required[str]
    """ 계정 식별자 """

    matchtype: Required[int]
    """ 매치 종류 (/metadata/matchtype API 참고) """

    offset: Optional[int]
    """ 리스트에서 가져올 시작 위치 """

    limit: Optional[int]
    """ 리스트에서 가져올 갯수(최대 100개) """


class FCOnlineUserMatchHistory(BaseModel):
    matches: List[str]


class GetUserTradeHistoryRequestParam(TypedDict, total=False):
    ouid: Required[str]
    """ 계정 식별자 """

    matchtype: Required[str]
    """ 거래 종류 (구입 buy, 판매 sell) """

    offset: Optional[int]
    """ 리스트에서 가져올 시작 위치 """

    limit: Optional[int]
    """ 리스트에서 가져올 갯수(최대 100개) """


class FCOnlineUserTradeHistory(BaseModel):
    trades: List[Trade]

    class Trade(BaseModel):
        tradeDate: str
        """ 거래 일자 (UTC0) (구매일 경우, 구매 등록 시점 / 판매일 경우, 판매 완료 시점) """

        saleSn: str
        """ 거래 고유 식별자 """

        spid: int 
        """ 선수 고유 식별자 (/metadata/spid API 참고) """

        grade: int
        """ 거래 선수 강화 등급 """

        value: int
        """ 거래 선수 가치(BP) """
