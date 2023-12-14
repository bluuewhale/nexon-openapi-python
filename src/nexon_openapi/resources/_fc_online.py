from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union
from typing_extensions import Required, TypedDict

import httpx

from ._types import Ouid
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI


__all__ = ["FCOnline"]


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
    ) -> Ouid:
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
        )

    def get_character_basic(
        self,
        *,
        ouid: Ouid,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FCOnlineUserBasic:
        return self._get(
            path="wp/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid.ouid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=FCOnlineUserBasic,
        )


class GetOuidRequestParam(TypedDict, total=True):
    world_name: Required[str]
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ouid: Required[Ouid]


class FCOnlineUserBasic(BaseModel):
    ouid: str
    """계정 식별자"""

    nickname: str
    """유저 닉네임"""

    level: int
    """유저 레벨"""
