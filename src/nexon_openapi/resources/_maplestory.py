from __future__ import annotations
from datetime import datetime, timezone, timedelta
import httpx
from typing import TYPE_CHECKING, List, Optional, Tuple, Union
from typing_extensions import Required, TypedDict, Annotated

from pydantic import Field

from ._types import Ocid, Ouid
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI, NexonOpenAPIAsync


KST_TIMEZONE = timezone(timedelta(hours=9))
ONE_DAY = timedelta(days=1)
TWO_DAY = timedelta(days=2)


class MapleStory(SyncAPIResource):
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
            "maplestory/v1/id",
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

    def get_ouid(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = self._get(
            "maplestory/v1/ouid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ouid,
        )

        return response.ouid

    def get_character_basic(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterBasic:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterBasic,
        )

    def get_character_list(
        self,
        *,
        ocid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterList:

        return self._get(
            path="maplestory/v1/character/list",
            options=make_request_options(
                query=maybe_transform({}, GetCharacterListRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterList,
        )

    def get_character_popularity(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPopularity:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/popularity",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPopularityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPopularity,
        )

    def get_character_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterStat:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterStat,
        )

    def get_character_hyper_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHyperStat:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/hyper-stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterHyperStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHyperStat,
        )

    def get_character_propensity(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPropensity:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/propensity",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPropensityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPropensity,
        )

    def get_character_ability(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterAbility:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/ability",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterAbilityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterAbility,
        )

    def get_character_item_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterItemEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterItemEquipment,
        )

    def get_character_cash_item_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterCashItemEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/cashitem-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterCashItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterCashItemEquipment,
        )

    def get_character_symbol_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSymbolEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/symbol-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterSymbolEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSymbolEquipment,
        )

    def get_character_set_effect(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSetEffect:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/set-effect",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterSetEffectRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSetEffect,
        )

    def get_character_beauty_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterBeautyEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/beauty-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterBeautyEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterBeautyEquipment,
        )

    def get_character_android_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterAndroidEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/android-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterAndroidEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterAndroidEquipment,
        )

    def get_character_pet_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPetEquipment:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/pet-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPetEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPetEquipment,
        )

    def get_character_skill(
        self,
        *,
        ocid: str,
        character_skill_grade: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSkill:
        """
        character_skill_grade: string
            조회하고자 하는 전직 차수

            0: 0차 스킬 및 제로 공용스킬
            1: 1차 스킬
            1.5: 1.5차 스킬
            2: 2차 스킬
            2.5: 2.5차 스킬
            3: 3차 스킬
            4: 4차 스킬 및 제로 알파/베타 스킬
            hyperpassive: 하이퍼 패시브 스킬
            hyperactive: 하이퍼 액티브 스킬
            5: 5차 스킬
            6: 6차 스킬

            Available values : 0, 1, 1.5, 2, 2.5, 3, 4, hyperpassive, hyperactive, 5, 6


        """
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/skill",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "character_skill_grade": character_skill_grade, "date": date},
                    GetCharacterSkillRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSkill,
        )

    def get_character_link_skill(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterLinkSkill:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/link-skill",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterLinkSkillRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterLinkSkill,
        )

    def get_character_vmatrix(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterVMatrix:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/vmatrix",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterVMatrixRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterVMatrix,
        )

    def get_character_hexa_matrix(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHexaMatrix:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/hexamatrix",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterHexaMatrixRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHexaMatrix,
        )

    def get_character_hexa_matrix_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHexaMatrixStat:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/hexamatrix-stat",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterHexaMatrixStatRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHexaMatrixStat,
        )

    def get_character_dojang(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterDojang:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/character/dojang",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterDojangRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterDojang,
        )

    def get_user_union(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnion:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/user/union",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnion,
        )

    def get_user_union_raider(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnionRaider:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/user/union-raider",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionRaiderRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnionRaider,
        )

    def get_user_union_artifact(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnionArtifact:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/user/union-artifact",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionArtifactRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnionArtifact,
        )

    def get_guild_id(
        self,
        *,
        world_name: str,
        guild_name: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/guild/id",
            options=make_request_options(
                query=maybe_transform({"world_name": world_name, "guild_name": guild_name}, GetGuildIdRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryGuildId,
        ).oguild_id

    def get_guild_basic(
        self,
        *,
        guild_id: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryGuildBasic:
        date = validate_date(date) if date is not None else date

        return self._get(
            path="maplestory/v1/guild/basic",
            options=make_request_options(
                query=maybe_transform({"oguild_id": guild_id, "date": date}, GetGuildBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryGuildBasic,
        )

    def get_overall_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        world_type: Optional[str] = None,
        class_: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryOverallRanking:
        """
        world_type: str
            월드 타입 (0:일반, 1:리부트) (기본 값은 0이며, world_name 입력 시 미 반영)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        class_: str
            - 초보자-전체 전직
            - 전사-전체 전직
            - 전사-검사
            - 전사-파이터
            - 전사-페이지
            - 전사-스피어맨
            - 전사-크루세이더
            - 전사-나이트
            - 전사-버서커
            - 전사-히어로
            - 전사-팔라딘
            - 전사-다크나이트
            - 마법사-전체 전직
            - 마법사-매지션
            - 마법사-위자드(불,독)
            - 마법사-위자드(썬,콜)
            - 마법사-클레릭
            - 마법사-메이지(불,독)
            - 마법사-메이지(썬,콜)
            - 마법사-프리스트
            - 마법사-아크메이지(불,독)
            - 마법사-아크메이지(썬,콜)
            - 마법사-비숍
            - 궁수-전체 전직
            - 궁수-아처
            - 궁수-헌터
            - 궁수-사수
            - 궁수-레인저
            - 궁수-저격수
            - 궁수-보우마스터
            - 궁수-신궁
            - 궁수-아처(패스파인더)
            - 궁수-에인션트아처
            - 궁수-체이서
            - 궁수-패스파인더
            - 도적-전체 전직
            - 도적-로그
            - 도적-어쌔신
            - 도적-시프
            - 도적-허밋
            - 도적-시프마스터
            - 도적-나이트로드
            - 도적-섀도어
            - 도적-세미듀어러
            - 도적-듀어러
            - 도적-듀얼마스터
            - 도적-슬래셔
            - 도적-듀얼블레이더
            - 해적-전체 전직
            - 해적-해적
            - 해적-인파이터
            - 해적-건슬링거
            - 해적-캐논슈터
            - 해적-버커니어
            - 해적-발키리
            - 해적-캐논블래스터
            - 해적-바이퍼
            - 해적-캡틴
            - 해적-캐논마스터
            - 기사단-전체 전직
            - 기사단-노블레스
            - 기사단-소울마스터
            - 기사단-플레임위자드
            - 기사단-윈드브레이커
            - 기사단-나이트워커
            - 기사단-스트라이커
            - 기사단-미하일
            - 아란-전체 전직
            - 에반-전체 전직
            - 레지스탕스-전체 전직
            - 레지스탕스-시티즌
            - 레지스탕스-배틀메이지
            - 레지스탕스-와일드헌터
            - 레지스탕스-메카닉
            - 레지스탕스-데몬슬레이어
            - 레지스탕스-데몬어벤져
            - 레지스탕스-제논
            - 레지스탕스-블래스터
            - 메르세데스-전체 전직
            - 팬텀-전체 전직
            - 루미너스-전체 전직
            - 카이저-전체 전직
            - 엔젤릭버스터-전체 전직
            - 초월자-전체 전직
            - 초월자-제로
            - 은월-전체 전직
            - 프렌즈 월드-전체 전직
            - 프렌즈 월드-키네시스
            - 카데나-전체 전직
            - 일리움-전체 전직
            - 아크-전체 전직
            - 호영-전체 전직
            - 아델-전체 전직
            - 카인-전체 전직
            - 라라-전체 전직
            - 칼리-전체 전직
        """

        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/overall",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "world_type": world_type,
                        "class": class_,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetOverallRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryOverallRanking,
        )

    def get_union_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUnionRanking:
        """
        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3
        """
        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/union",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetUnionRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUnionRanking,
        )

    def get_guild_ranking(
        self,
        *,
        ranking_type: str,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        guild_name: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryGuildRanking:
        """
        ranking_type: str
            랭킹 타입 (0:주간 명성치, 1:플래그 레이스, 2:지하 수로)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        """
        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/guild",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "ranking_type": ranking_type,
                        "date": date,
                        "world_name": world_name,
                        "guild_name": guild_name,
                        "page": page,
                    },
                    GetGuildRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryGuildRanking,
        )

    def get_dojang_ranking(
        self,
        *,
        difficulty: str,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        class_: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryDojangRanking:
        """
        difficulty: str
            구간 (0:일반, 1:통달)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        class_: str
            - 초보자-전체 전직
            - 전사-전체 전직
            - 전사-검사
            - 전사-파이터
            - 전사-페이지
            - 전사-스피어맨
            - 전사-크루세이더
            - 전사-나이트
            - 전사-버서커
            - 전사-히어로
            - 전사-팔라딘
            - 전사-다크나이트
            - 마법사-전체 전직
            - 마법사-매지션
            - 마법사-위자드(불,독)
            - 마법사-위자드(썬,콜)
            - 마법사-클레릭
            - 마법사-메이지(불,독)
            - 마법사-메이지(썬,콜)
            - 마법사-프리스트
            - 마법사-아크메이지(불,독)
            - 마법사-아크메이지(썬,콜)
            - 마법사-비숍
            - 궁수-전체 전직
            - 궁수-아처
            - 궁수-헌터
            - 궁수-사수
            - 궁수-레인저
            - 궁수-저격수
            - 궁수-보우마스터
            - 궁수-신궁
            - 궁수-아처(패스파인더)
            - 궁수-에인션트아처
            - 궁수-체이서
            - 궁수-패스파인더
            - 도적-전체 전직
            - 도적-로그
            - 도적-어쌔신
            - 도적-시프
            - 도적-허밋
            - 도적-시프마스터
            - 도적-나이트로드
            - 도적-섀도어
            - 도적-세미듀어러
            - 도적-듀어러
            - 도적-듀얼마스터
            - 도적-슬래셔
            - 도적-듀얼블레이더
            - 해적-전체 전직
            - 해적-해적
            - 해적-인파이터
            - 해적-건슬링거
            - 해적-캐논슈터
            - 해적-버커니어
            - 해적-발키리
            - 해적-캐논블래스터
            - 해적-바이퍼
            - 해적-캡틴
            - 해적-캐논마스터
            - 기사단-전체 전직
            - 기사단-노블레스
            - 기사단-소울마스터
            - 기사단-플레임위자드
            - 기사단-윈드브레이커
            - 기사단-나이트워커
            - 기사단-스트라이커
            - 기사단-미하일
            - 아란-전체 전직
            - 에반-전체 전직
            - 레지스탕스-전체 전직
            - 레지스탕스-시티즌
            - 레지스탕스-배틀메이지
            - 레지스탕스-와일드헌터
            - 레지스탕스-메카닉
            - 레지스탕스-데몬슬레이어
            - 레지스탕스-데몬어벤져
            - 레지스탕스-제논
            - 레지스탕스-블래스터
            - 메르세데스-전체 전직
            - 팬텀-전체 전직
            - 루미너스-전체 전직
            - 카이저-전체 전직
            - 엔젤릭버스터-전체 전직
            - 초월자-전체 전직
            - 초월자-제로
            - 은월-전체 전직
            - 프렌즈 월드-전체 전직
            - 프렌즈 월드-키네시스
            - 카데나-전체 전직
            - 일리움-전체 전직
            - 아크-전체 전직
            - 호영-전체 전직
            - 아델-전체 전직
            - 카인-전체 전직
            - 라라-전체 전직
            - 칼리-전체 전직

        """
        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/dojang",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "difficulty": difficulty,
                        "date": date,
                        "world_name": world_name,
                        "class": class_,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetDojangRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryDojangRanking,
        )

    def get_the_seed_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryTheSeedRanking:
        """
        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3
        """
        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/theseed",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetTheSeedRankingRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryTheSeedRanking,
        )

    def get_achievement_ranking(
        self,
        *,
        date: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryAchievementRanking:
        date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/ranking/achievement",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetAchievementRankingRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryAchievementRanking,
        )

    def get_starforce_history(
        self,
        *,
        count: int,
        date: Optional[str] = None,
        cursor: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryStartForceHistory:
        if date is not None and cursor is not None:
            raise ValueError("either 'date' or 'cursor' must be None")

        if cursor is None:
            date = validate_date(date) if date is not None else get_latest_date_available()

        return self._get(
            path="maplestory/v1/history/starforce",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "count": count,
                        "cursor": cursor,
                    },
                    GetStartforceHistoryRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryStartForceHistory,
        )


class MapleStoryAsync(AsyncAPIResource):
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
            "maplestory/v1/id",
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

    async def get_ouid(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        response = await self._get(
            "maplestory/v1/ouid",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ouid,
        )

        return response.ouid

    async def get_character_basic(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterBasic:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterBasic,
        )

    async def get_character_list(
        self,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterList:
        return await self._get(
            path="maplestory/v1/character/list",
            options=make_request_options(
                query=maybe_transform({}, GetCharacterListRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterList,
        )

    async def get_character_popularity(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPopularity:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/popularity",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPopularityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPopularity,
        )

    async def get_character_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterStat:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterStat,
        )

    async def get_character_hyper_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHyperStat:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/hyper-stat",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterHyperStatRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHyperStat,
        )

    async def get_character_propensity(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPropensity:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/propensity",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPropensityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPropensity,
        )

    async def get_character_ability(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterAbility:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/ability",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterAbilityRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterAbility,
        )

    async def get_character_item_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterItemEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/item-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterItemEquipment,
        )

    async def get_character_cash_item_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterCashItemEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/cashitem-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterCashItemEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterCashItemEquipment,
        )

    async def get_character_symbol_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSymbolEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/symbol-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterSymbolEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSymbolEquipment,
        )

    async def get_character_set_effect(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSetEffect:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/set-effect",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterSetEffectRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSetEffect,
        )

    async def get_character_beauty_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterBeautyEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/beauty-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterBeautyEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterBeautyEquipment,
        )

    async def get_character_android_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterAndroidEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/android-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterAndroidEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterAndroidEquipment,
        )

    async def get_character_pet_equipment(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterPetEquipment:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/pet-equipment",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetCharacterPetEquipmentRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterPetEquipment,
        )

    async def get_character_skill(
        self,
        *,
        ocid: str,
        character_skill_grade: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterSkill:
        """
        character_skill_grade: string
            조회하고자 하는 전직 차수

            0: 0차 스킬 및 제로 공용스킬
            1: 1차 스킬
            1.5: 1.5차 스킬
            2: 2차 스킬
            2.5: 2.5차 스킬
            3: 3차 스킬
            4: 4차 스킬 및 제로 알파/베타 스킬
            hyperpassive: 하이퍼 패시브 스킬
            hyperactive: 하이퍼 액티브 스킬
            5: 5차 스킬
            6: 6차 스킬

            Available values : 0, 1, 1.5, 2, 2.5, 3, 4, hyperpassive, hyperactive, 5, 6


        """
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/skill",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "character_skill_grade": character_skill_grade, "date": date},
                    GetCharacterSkillRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterSkill,
        )

    async def get_character_link_skill(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterLinkSkill:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/link-skill",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterLinkSkillRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterLinkSkill,
        )

    async def get_character_vmatrix(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterVMatrix:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/vmatrix",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterVMatrixRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterVMatrix,
        )

    async def get_character_hexa_matrix(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHexaMatrix:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/hexamatrix",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterHexaMatrixRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHexaMatrix,
        )

    async def get_character_hexa_matrix_stat(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterHexaMatrixStat:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/hexamatrix-stat",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterHexaMatrixStatRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterHexaMatrixStat,
        )

    async def get_character_dojang(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryCharacterDojang:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/character/dojang",
            options=make_request_options(
                query=maybe_transform(
                    {"ocid": ocid, "date": date},
                    GetCharacterDojangRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryCharacterDojang,
        )

    async def get_user_union(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnion:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/user/union",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnion,
        )

    async def get_user_union_raider(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnionRaider:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/user/union-raider",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionRaiderRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnionRaider,
        )

    async def get_user_union_artifact(
        self,
        *,
        ocid: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUserUnionArtifact:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/user/union-artifact",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid, "date": date}, GetUserUnionArtifactRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUserUnionArtifact,
        )

    async def get_guild_id(
        self,
        *,
        world_name: str,
        guild_name: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> str:
        date = validate_date(date) if date is not None else date

        return (
            await self._get(
                path="maplestory/v1/guild/id",
                options=make_request_options(
                    query=maybe_transform({"world_name": world_name, "guild_name": guild_name}, GetGuildIdRequestParam),
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                ),
                cast_to=MapleStoryGuildId,
            )
        ).oguild_id

    async def get_guild_basic(
        self,
        *,
        guild_id: str,
        date: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryGuildBasic:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/guild/basic",
            options=make_request_options(
                query=maybe_transform({"oguild_id": guild_id, "date": date}, GetGuildBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryGuildBasic,
        )

    async def get_overall_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        world_type: Optional[str] = None,
        class_: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryOverallRanking:
        """
        world_type: str
            월드 타입 (0:일반, 1:리부트) (기본 값은 0이며, world_name 입력 시 미 반영)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        class_: str
            - 초보자-전체 전직
            - 전사-전체 전직
            - 전사-검사
            - 전사-파이터
            - 전사-페이지
            - 전사-스피어맨
            - 전사-크루세이더
            - 전사-나이트
            - 전사-버서커
            - 전사-히어로
            - 전사-팔라딘
            - 전사-다크나이트
            - 마법사-전체 전직
            - 마법사-매지션
            - 마법사-위자드(불,독)
            - 마법사-위자드(썬,콜)
            - 마법사-클레릭
            - 마법사-메이지(불,독)
            - 마법사-메이지(썬,콜)
            - 마법사-프리스트
            - 마법사-아크메이지(불,독)
            - 마법사-아크메이지(썬,콜)
            - 마법사-비숍
            - 궁수-전체 전직
            - 궁수-아처
            - 궁수-헌터
            - 궁수-사수
            - 궁수-레인저
            - 궁수-저격수
            - 궁수-보우마스터
            - 궁수-신궁
            - 궁수-아처(패스파인더)
            - 궁수-에인션트아처
            - 궁수-체이서
            - 궁수-패스파인더
            - 도적-전체 전직
            - 도적-로그
            - 도적-어쌔신
            - 도적-시프
            - 도적-허밋
            - 도적-시프마스터
            - 도적-나이트로드
            - 도적-섀도어
            - 도적-세미듀어러
            - 도적-듀어러
            - 도적-듀얼마스터
            - 도적-슬래셔
            - 도적-듀얼블레이더
            - 해적-전체 전직
            - 해적-해적
            - 해적-인파이터
            - 해적-건슬링거
            - 해적-캐논슈터
            - 해적-버커니어
            - 해적-발키리
            - 해적-캐논블래스터
            - 해적-바이퍼
            - 해적-캡틴
            - 해적-캐논마스터
            - 기사단-전체 전직
            - 기사단-노블레스
            - 기사단-소울마스터
            - 기사단-플레임위자드
            - 기사단-윈드브레이커
            - 기사단-나이트워커
            - 기사단-스트라이커
            - 기사단-미하일
            - 아란-전체 전직
            - 에반-전체 전직
            - 레지스탕스-전체 전직
            - 레지스탕스-시티즌
            - 레지스탕스-배틀메이지
            - 레지스탕스-와일드헌터
            - 레지스탕스-메카닉
            - 레지스탕스-데몬슬레이어
            - 레지스탕스-데몬어벤져
            - 레지스탕스-제논
            - 레지스탕스-블래스터
            - 메르세데스-전체 전직
            - 팬텀-전체 전직
            - 루미너스-전체 전직
            - 카이저-전체 전직
            - 엔젤릭버스터-전체 전직
            - 초월자-전체 전직
            - 초월자-제로
            - 은월-전체 전직
            - 프렌즈 월드-전체 전직
            - 프렌즈 월드-키네시스
            - 카데나-전체 전직
            - 일리움-전체 전직
            - 아크-전체 전직
            - 호영-전체 전직
            - 아델-전체 전직
            - 카인-전체 전직
            - 라라-전체 전직
            - 칼리-전체 전직
        """

        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/overall",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "world_type": world_type,
                        "class": class_,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetOverallRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryOverallRanking,
        )

    async def get_union_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryUnionRanking:
        """
        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3
        """
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/union",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetUnionRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryUnionRanking,
        )

    async def get_guild_ranking(
        self,
        *,
        ranking_type: str,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        guild_name: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryGuildRanking:
        """
        ranking_type: str
            랭킹 타입 (0:주간 명성치, 1:플래그 레이스, 2:지하 수로)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        """
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/guild",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "ranking_type": ranking_type,
                        "date": date,
                        "world_name": world_name,
                        "guild_name": guild_name,
                        "page": page,
                    },
                    GetGuildRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryGuildRanking,
        )

    async def get_dojang_ranking(
        self,
        *,
        difficulty: str,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        class_: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryDojangRanking:
        """
        difficulty: str
            구간 (0:일반, 1:통달)

        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3

        class_: str
            - 초보자-전체 전직
            - 전사-전체 전직
            - 전사-검사
            - 전사-파이터
            - 전사-페이지
            - 전사-스피어맨
            - 전사-크루세이더
            - 전사-나이트
            - 전사-버서커
            - 전사-히어로
            - 전사-팔라딘
            - 전사-다크나이트
            - 마법사-전체 전직
            - 마법사-매지션
            - 마법사-위자드(불,독)
            - 마법사-위자드(썬,콜)
            - 마법사-클레릭
            - 마법사-메이지(불,독)
            - 마법사-메이지(썬,콜)
            - 마법사-프리스트
            - 마법사-아크메이지(불,독)
            - 마법사-아크메이지(썬,콜)
            - 마법사-비숍
            - 궁수-전체 전직
            - 궁수-아처
            - 궁수-헌터
            - 궁수-사수
            - 궁수-레인저
            - 궁수-저격수
            - 궁수-보우마스터
            - 궁수-신궁
            - 궁수-아처(패스파인더)
            - 궁수-에인션트아처
            - 궁수-체이서
            - 궁수-패스파인더
            - 도적-전체 전직
            - 도적-로그
            - 도적-어쌔신
            - 도적-시프
            - 도적-허밋
            - 도적-시프마스터
            - 도적-나이트로드
            - 도적-섀도어
            - 도적-세미듀어러
            - 도적-듀어러
            - 도적-듀얼마스터
            - 도적-슬래셔
            - 도적-듀얼블레이더
            - 해적-전체 전직
            - 해적-해적
            - 해적-인파이터
            - 해적-건슬링거
            - 해적-캐논슈터
            - 해적-버커니어
            - 해적-발키리
            - 해적-캐논블래스터
            - 해적-바이퍼
            - 해적-캡틴
            - 해적-캐논마스터
            - 기사단-전체 전직
            - 기사단-노블레스
            - 기사단-소울마스터
            - 기사단-플레임위자드
            - 기사단-윈드브레이커
            - 기사단-나이트워커
            - 기사단-스트라이커
            - 기사단-미하일
            - 아란-전체 전직
            - 에반-전체 전직
            - 레지스탕스-전체 전직
            - 레지스탕스-시티즌
            - 레지스탕스-배틀메이지
            - 레지스탕스-와일드헌터
            - 레지스탕스-메카닉
            - 레지스탕스-데몬슬레이어
            - 레지스탕스-데몬어벤져
            - 레지스탕스-제논
            - 레지스탕스-블래스터
            - 메르세데스-전체 전직
            - 팬텀-전체 전직
            - 루미너스-전체 전직
            - 카이저-전체 전직
            - 엔젤릭버스터-전체 전직
            - 초월자-전체 전직
            - 초월자-제로
            - 은월-전체 전직
            - 프렌즈 월드-전체 전직
            - 프렌즈 월드-키네시스
            - 카데나-전체 전직
            - 일리움-전체 전직
            - 아크-전체 전직
            - 호영-전체 전직
            - 아델-전체 전직
            - 카인-전체 전직
            - 라라-전체 전직
            - 칼리-전체 전직

        """
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/dojang",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "difficulty": difficulty,
                        "date": date,
                        "world_name": world_name,
                        "class": class_,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetDojangRankingRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryDojangRanking,
        )

    async def get_the_seed_ranking(
        self,
        *,
        date: Optional[str] = None,
        world_name: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryTheSeedRanking:
        """
        world_name: 월드 명
            - 스카니아
            - 베라
            - 루나
            - 제니스
            - 크로아
            - 유니온
            - 엘리시움
            - 이노시스
            - 레드
            - 오로라
            - 아케인
            - 노바
            - 리부트
            - 리부트2
            - 버닝
            - 버닝2
            - 버닝3
        """
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/theseed",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "world_name": world_name,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetTheSeedRankingRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryTheSeedRanking,
        )

    async def get_achievement_ranking(
        self,
        *,
        date: Optional[str] = None,
        ocid: Optional[str] = None,
        page: Optional[int] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryAchievementRanking:
        date = validate_date(date) if date is not None else date

        return await self._get(
            path="maplestory/v1/ranking/achievement",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "ocid": ocid,
                        "page": page,
                    },
                    GetAchievementRankingRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryAchievementRanking,
        )

    async def get_starforce_history(
        self,
        *,
        count: int,
        date: Optional[str] = None,
        cursor: Optional[str] = None,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MapleStoryStartForceHistory:
        if date is not None and cursor is not None:
            raise ValueError("either 'date' or 'cursor' must be None")

        if cursor is None:
            date = validate_date(date) if date is not None else get_latest_date_available()

        return await self._get(
            path="maplestory/v1/history/starforce",
            options=make_request_options(
                query=maybe_transform(
                    {
                        "date": date,
                        "count": count,
                        "cursor": cursor,
                    },
                    GetStartforceHistoryRequestParam,
                ),
                extra_query=extra_query,
                extra_headers=extra_headers,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MapleStoryStartForceHistory,
        )


def validate_date(date: str) -> str:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        raise ValueError("date must be in YYYY-mm-dd format")


def get_latest_date_available() -> str:
    now = datetime.now(KST_TIMEZONE)

    if now.hour == 0:  # data is being updated between 0:00 ~ 1:00, we have to look up the day before yesterday
        return (now - TWO_DAY).strftime("%Y-%m-%d")

    return (now - ONE_DAY).strftime("%Y-%m-%d")


class CashItemEquipment(BaseModel):
    cash_item_equipment_part: str
    """ 캐시 장비 부위 명 """

    cash_item_equipment_slot: str
    """ 캐시 장비 슬롯 위치 """

    cash_item_name: str
    """ 캐시 장비 명 """

    cash_item_icon: str
    """ 캐시 장비 아이콘 """

    cash_item_description: Optional[str]
    """ 캐시 장비 설명 """

    cash_item_option: List[CashItemOption]
    """ 캐시 장비 옵션 """

    date_expire: Optional[str]
    """ 캐시 장비 유효 기간 (KST) """

    date_option_expire: Optional[str]
    """ 캐시 장비 옵션 유효 기간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    cash_item_label: Optional[str]
    """ 캐시 장비 라벨 정보 """

    cash_item_coloring_prism: Optional[CashItemColoringPrism]
    """ 캐시 장비 컬러링 프리즘 정보 """

    class CashItemOption(BaseModel):
        option_type: str
        """ 옵션 타입 """

        option_value: str
        """ 옵션 값 """

    class CashItemColoringPrism(BaseModel):
        color_range: str
        """ 컬러링프리즘 색상 범위 """

        hue: int
        """ 컬러링프리즘 색조 """

        saturation: int
        """ 컬러링프리즘 채도 """

        value: int
        """ 컬러링프리즘 명도 """


class CharacterCashItemEquipment(CashItemEquipment):
    item_gender: Optional[str]
    """ 아이템 장착 가능 성별 """


class AndroidCashItemEquipment(CashItemEquipment):
    android_item_gender: Optional[str]
    """ 아이템 장착 가능 성별 """


class CharacterHair(BaseModel):
    hair_name: str
    """ 헤어 명"""

    base_color: str
    """ 헤어 베이스 컬러 """

    mix_color: Optional[str]
    """ 헤어 믹스 컬러 """

    mix_rate: str
    """ 헤어 믹스 컬러의 염색 비율 """


class CharacterFace(BaseModel):
    face_name: str
    """ 성형 명"""

    base_color: str
    """ 성형 베이스 컬러 """

    mix_color: Optional[str]
    """ 성형 믹스 컬러 """

    mix_rate: str
    """ 성형 믹스 컬러의 염색 비율 """


class GetOcidRequestParam(TypedDict, total=True):
    character_name: Required[str]


class GetOuidRequestParam(TypedDict, total=True):
    pass


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterBasic(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_name: str
    """ 캐릭터 명 """

    world_name: str
    """ 월드 명 """

    character_gender: str
    """ 캐릭터 성별"""

    character_class: str
    """ 캐릭터 직업 """

    character_class_level: str
    """ 캐릭터 전직 차수 """

    character_level: int
    """ 캐릭터 레벨 """

    character_exp: int
    """ 현재 레벨에서 보유한 경험치 """

    character_exp_rate: int
    """ 현재 레벨에서 경험치 퍼센트 """

    character_guild_name: int
    """ 캐릭터 소속 길드 명 """

    character_image: int
    """ 캐릭터 외형 이미지 """

    character_date_create: str
    """ 캐릭터 생성일 (KST) """

    access_flag: str
    """ 최근 7일간 접속 여부 (true: 접속, false: 미접속) """

    liberation_quest_clear_flag: str
    """ 해방 퀘스트 완료 여부 (true: 완료, false: 미완료) """



# character list
class GetCharacterListRequestParam(TypedDict, total=False):
    pass


class MapleStoryCharacterList(BaseModel):
    account_id: str
    """ 메이플스토리 계정 식별자 """

    character_list: List[CharacterInfo]
    """ 캐릭터 목록 """

    class CharacterInfo(BaseModel):
        ocid: str
        """ 캐릭터 식별자 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        character_class: str
        """ 캐릭터 직업 """

        character_level: int
        """ 캐릭터 레벨 """


# character popularity
class GetCharacterPopularityRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterPopularity(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    popularity: int
    """ 캐릭터 인기도 """


class GetCharacterStatRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterStat(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    final_stat: List[Stat]
    """ 현재 스탯 정보 """

    remain_ap: int
    """ 잔여 AP """

    class Stat(BaseModel):
        stat_name: str
        """ 스텟 명
        ex) 최소 스탯 공격력 
        """

        stat_name: str
        """ 스텟 값
        ex) 43.75 
        """


class GetCharacterHyperStatRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterHyperStat(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    use_preset_no: str
    """ 적용 중인 프리셋 번호 """

    use_available_hyper_stat: int
    """ 사용 가능한 최대 하이퍼스탯 포인트 """

    hyper_stat_preset_1: HyperStatPreset
    """ 프리셋 1번 하이퍼 스탯 정보 """

    hyper_stat_preset_1_remain_point: int
    """ 프리셋 1번 하이퍼 스탯 잔여 포인트 """

    hyper_stat_preset_2: HyperStatPreset
    """ 프리셋 2번 하이퍼 스탯 정보 """

    hyper_stat_preset_2_remain_point: int
    """ 프리셋 2번 하이퍼 스탯 잔여 포인트 """

    hyper_stat_preset_3: HyperStatPreset
    """ 프리셋 3번 하이퍼 스탯 정보 """

    hyper_stat_preset_3_remain_point: int
    """ 프리셋 3번 하이퍼 스탯 잔여 포인트 """

    class HyperStatPreset(BaseModel):
        stat_type: str
        """ 스텟 종류 """

        stat_name: int
        """ 스탯 투자 포인트 """

        stat_level: int
        """ 스탯 레벨 """

        stat_increase: int
        """ 스탯 상승량 """


class GetCharacterPropensityRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterPropensity(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    charisma_level: int
    """ 카리스마 레벨 """

    sensibility_level: int
    """ 감성 레벨 """

    insight_level: int
    """ 통찰력 레벨 """

    willingness_level: int
    """ 의지 레벨 """

    handicraft_level: int
    """ 손재주 레벨 """

    charm_level: int
    """ 매력 레벨 """


class GetCharacterAbilityRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterAbility(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    ability_grade: str
    """ 어빌리티 등급 """

    ability_info: List[AbilityInfo]
    """ 어빌리티 정보 """

    remain_fame: int
    """ 보유 명성치 """

    preset_no: Optional[int]
    """ 적용 중인 어빌리티 프리셋 번호 """

    ability_preset_1: Optional[AbilityPreset]
    """ 어빌리티 1번 프리셋 전체 정보 """

    ability_preset_2: Optional[AbilityPreset]
    """ 어빌리티 2번 프리셋 전체 정보 """

    ability_preset_3: Optional[AbilityPreset]
    """ 어빌리티 3번 프리셋 전체 정보 """

    class AbilityInfo(BaseModel):
        ability_no: str
        """ 어빌리티 번호 """

        ability_grade: str
        """ 어빌리티 등급 """

        ability_value: str
        """ 어빌리티 옵션 및 수치 """

    class AbilityPreset(BaseModel):
        ability_preset_grade: str
        """ 어빌리티 프리셋의 어빌리티 등급 """

        ability_info: List["AbilityInfo"]


class GetCharacterItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterItemEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_gender: str
    """ 캐릭터 성별 """

    character_class: str
    """ 캐릭터 직업 """

    preset_no: Optional[int]
    """ 적용 중인 프리셋 번호 """

    item_equipment: List[ItemEquipment]
    """ 장비 정보 """

    item_equipment_preset_1: Optional[List[ItemEquipment]] = Field(None, alias="item_equipment_preset1")
    """ 1번 프리셋 장비 정보 """

    item_equipment_preset_2: Optional[List[ItemEquipment]] = Field(None, alias="item_equipment_preset1")
    """ 2번 프리셋 장비 정보 """

    item_equipment_preset_3: Optional[List[ItemEquipment]] = Field(None, alias="item_equipment_preset1")
    """ 3번 프리셋 장비 정보 """

    title: Title
    """ 칭호 정보 """

    dragon_equipment: List[ItemEquipment]
    """ 에반 드래곤 장비 정보 (에반인 경우 응답) """

    mechanic_equipment: List[ItemEquipment]
    """ 메카닉 장비 정보 (메카닉인 경우 응답) """

    class Title(BaseModel):
        title_name: str
        """ 칭호 장비 명 """

        title_icon: str
        """ 칭호 아이콘 """

        title_description: List[str]
        """ 칭호 설명 """

        date_expire: str
        """ 칭호 유효 기간 (KST) """

        date_option_expire: str
        """ 칭호 옵션 유효 기간 (expired: 만료, null: 무제한) (KST) """

    class ItemEquipment(BaseModel):
        item_equipment_part: str
        """ 장비 부위 명 """

        equipment_slot: str
        """ 장비 슬롯 위치 """

        item_name: str
        """ 장비 명 """

        item_icon: str
        """ 장비 아이콘 """

        item_description: Optional[str]
        """ 장비 설명 """

        item_shape_name: str
        """ 장비 외형 """

        item_shape_icon: str
        """ 장비 외형 아이콘 """

        item_gender: Optional[str]
        """ 전용 성별 """

        potential_option_grade: Optional[str]
        """ 잠재능력 등급 """

        additional_potential_option_grade: Optional[str]
        """ 에디셔널 잠재능력 등급 """

        potential_option_1: Optional[str]
        """ 잠재능력 첫 번째 옵션 """

        potential_option_2: Optional[str]
        """ 잠재능력 두 번째 옵션 """

        potential_option_3: Optional[str]
        """ 잠재능력 세 번째 옵션 """

        addtional_potential_option_1: Optional[str]
        """ 에디셔널 잠재능력 첫 번째 옵션 """

        addtional_potential_option_2: Optional[str]
        """ 에디셔널 잠재능력 두 번째 옵션 """

        addtional_potential_option_3: Optional[str]
        """ 에디셔널 잠재능력 세 번째 옵션 """

        equipment_level_increase: int
        """ 착용 레벨 증가 """

        growth_exp: int
        """ 성장 경험치 """

        growth_level: int
        """ 성장 레벨 """

        scroll_upgrade: str
        """ 업그레이드 횟수 """

        cuttable_count: str
        """ 가위 사용 가능 횟수 (교환 불가 장비, 가위 횟수가 없는 교환 가능 장비는 255)"""

        golden_hammer_flag: str
        """ 황금 망치 제련 적용 (1:적용, 이외 미 적용)"""

        scroll_resilience_count: str
        """ 복구 가능 횟수 """

        scroll_upgradeable_count: str
        """ 업그레이드 가능 횟수 """

        soul_name: Optional[str]
        """ 소울 명 """

        soul_option: Optional[str]
        """ 소울 옵션 """

        starforce: str
        """ 강화 단계 """

        starforce_scroll_flag: str
        """ 놀라운 장비 강화 주문서 사용 여부 (0: 미사용, 1: 사용)"""

        special_ring_level: int
        """ 특수 반지 레벨 """

        date_expire: Optional[str]
        """ 장비 유효 기간(KST) """

        item_total_option: MapleStoryCharacterItemEquipment.ItemTotalOption
        item_base_option: MapleStoryCharacterItemEquipment.ItemBaseOption
        item_exceptional_option: MapleStoryCharacterItemEquipment.ItemExceptionalOption
        item_add_option: MapleStoryCharacterItemEquipment.ItemAddOption
        item_etc_option: MapleStoryCharacterItemEquipment.ItemEtcOption
        item_starforce_option: MapleStoryCharacterItemEquipment.ItemEtcOption

    class ItemExceptionalOption(BaseModel):
        str: str
        """ STR """

        dex: str
        """ DEX """

        int: str
        """ INT """

        luk: str
        """ LUK """

        max_hp: str
        """ 최대 HP """

        max_mp: str
        """ 최대 MP """

        attack_power: str
        """ 공격력 """

        magic_power: str
        """ 마력 """

    class ItemEtcOption(ItemExceptionalOption):
        armor: str
        """ 방어력 """

        speed: str
        """ 이동속도 """

        jump: str
        """ 점프력 """

    class ItemAddOption(ItemEtcOption):
        boss_damage: str
        """ 보스 공격 시 데미지 증가(%) """

        damage: str
        """ 데미지(%) """

        all_stat: str
        """ 올스탯(%) """

        equipment_level_decrease: int
        """ 착용 레벨 감소 """

    class ItemBaseOption(ItemEtcOption):
        boss_damage: str
        """ 보스 공격 시 데미지 증가(%) """

        ignore_monster_armor: str
        """ 몬스터 방어율 무시(%) """

        all_stat: str
        """ 올스탯(%) """

        max_hp_rate: str
        """ 최대 HP(%) """

        max_mp_rate: str
        """ 최대 MP(%) """

        base_equipment_level: int
        """ 기본 착용 레벨 """

    class ItemTotalOption(ItemAddOption):
        ignore_monster_armor: str
        """ 몬스터 방어율 무시(%) """

        max_hp_rate: str
        """ 최대 HP(%) """

        max_mp_rate: str
        """ 최대 MP(%) """


class GetCharacterCashItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterCashItemEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_gender: str
    """ 캐릭터 성별 """

    character_class: str
    """ 캐릭터 직업 """

    preset_no: int
    """ 적용 중인 캐시 장비 프리셋 번호 """

    cash_item_equipment_base: Optional[List[CharacterCashItemEquipment]]
    """ 장착 중인 캐시 장비 정보 """

    cash_item_equipment_preset_1: List[CharacterCashItemEquipment]
    """ 1번 프리셋 장착 캐시 장비 정보 """

    cash_item_equipment_preset_2: List[CharacterCashItemEquipment]
    """ 2번 프리셋 장착 캐시 장비 정보 """

    cash_item_equipment_preset_3: List[CharacterCashItemEquipment]
    """ 3번 프리셋 장착 캐시 장비 정보 """

    additional_cash_item_equipment_preset_1: Optional[List[CharacterCashItemEquipment]]
    """ 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 1번 프리셋 장착 캐시 장비 정보 """

    additional_cash_item_equipment_preset_2: Optional[List[CharacterCashItemEquipment]]
    """ 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 2번 프리셋 장착 캐시 장비 정보 """

    additional_cash_item_equipment_preset_3: Optional[List[CharacterCashItemEquipment]]
    """ 제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드의 3번 프리셋 장착 캐시 장비 정보 """


class GetCharacterSymbolEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterSymbolEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    symbol: List[Symbol]

    class Symbol(BaseModel):
        symbol_name: str
        """ 심볼 명 """

        symbol_icon: str
        """ 심볼 아이콘 """

        symbol_description: str
        """ 심볼 설명 """

        symbol_force: str
        """ 심볼로 인한 증가 수치 """

        symbol_level: int
        """ 심볼 레벨 """

        symbol_str: str
        """ 심볼로 증가한 힘 """

        symbol_dex: str
        """ 심볼로 증가한 민첩 """

        symbol_int: str
        """ 심볼로 증가한 지력 """

        symbol_luk: str
        """ 심볼로 증가한 운 """

        symbol_hp: str
        """ 심볼로 증가한 체력 """

        symbol_growth_count: int
        """ 현재 보유 성장치 """

        symbol_require_growth_count: int
        """ 성장 시 필요한 성장치 """


class GetCharacterSetEffectRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterSetEffect(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    set_effect: List[SetEffect]

    class SetEffect(BaseModel):
        set_name: str
        """ 세트 효과 명 """

        total_set_count: int
        """ 세트 개수 (럭키 아이템 포함) """

        set_effect_info: List[SetEffectInfo]

        class SetEffectInfo(BaseModel):
            set_count: int
            """ 세트 효과 레벨 (장비 수) """

            set_option: str
            """ 적용 중인 세트 효과 """


class GetCharacterBeautyEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterBeautyEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_gender: str
    """ 캐릭터 성별 """

    character_class: str
    """ 캐릭터 직업 """

    character_hair: CharacterHair
    """ 캐릭터 헤어 정보 """

    character_face: CharacterFace
    """ 캐릭터 성형 정보 """

    character_skin_name: str
    """ 피부 명 (제로인 경우 알파, 엔젤릭버스터인 경우 일반 모드) """

    additional_character_hair: Optional[CharacterHair]
    """ 캐릭터 헤어 정보 (제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 헤어 정보) """

    additional_character_face: Optional[CharacterFace]
    """ 캐릭터 성형 정보 (제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 헤어 정보) """

    additional_character_skin_name: Optional[str]
    """ 피부 명 (제로인 경우 베타, 엔젤릭버스터인 경우 드레스 업 모드에 적용 중인 헤어 정보) """


class GetCharacterAndroidEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterAndroidEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    android_name: str
    """ 안드로이드 명 """

    android_nickname: str
    """ 안드로이드 닉네임 """

    android_icon: str
    """ 안드로이드 아이콘 """

    android_description: Optional[Tuple[str]]
    """ 안드로이드 설명 """

    android_hair: CharacterHair
    """ 안드로이드 헤어 정보 """

    android_face: CharacterFace
    """ 안드로이드 성형 정보 """

    android_skin_name: str
    """ 안드로이드 피부 명 """

    android_cash_item_equipment: List[AndroidCashItemEquipment]
    """ 안드로이드 캐시 아이템 장착 정보 """

    android_ear_sensor_clip_flag: Optional[str]
    """ 안드로이드 이어센서 클립 적용 여부 """

    android_gender: Optional[str]
    """ 안드로이드 성별 """

    android_grade: Optional[str]
    """ 안드로이드 등급 """

    android_non_humanoid_flag: Optional[str]
    """ 비인간형 안드로이드 여부 """

    android_shop_usable_flag: Optional[str]
    """ 잡화상점 가능 이용 가능 여부 """

    preset_no: Optional[str]
    """ 적용 중인 장비 프리셋 번호 """

    android_preset_1: Optional[AndroidInfo]
    """ 1번 프리셋 안드로이드 정보 """

    android_preset_2: Optional[AndroidInfo]
    """ 2번 프리셋 안드로이드 정보 """

    android_preset_3: Optional[AndroidInfo]
    """ 3번 프리셋 안드로이드 정보 """

    class AndroidInfo(BaseModel):
        android_name: str
        """ 안드로이드 명 """

        android_nickname: str
        """ 안드로이드 닉네임 """

        android_icon: str
        """ 안드로이드 아이콘 """

        android_description: Optional[str]
        """ 안드로이드 설명 """

        android_gender: Optional[str]
        """ 안드로이드 성별 """

        android_grade: Optional[str]
        """ 안드로이드 등급 """

        android_skin_name: str
        """ 안드로이드 피부 명 """

        android_hair: CharacterHair
        """ 안드로이드 헤어 정보 """

        android_face: CharacterFace
        """ 안드로이드 성형 정보 """

        android_ear_sensor_clip_flag: Optional[str]
        """ 안드로이드 이어센서 클립 적용 여부 """

        android_non_humanoid_flag: Optional[str]
        """ 비인간형 안드로이드 여부 """

        android_shop_usable_flag: Optional[str]
        """ 잡화상점 가능 이용 가능 여부 """


class GetCharacterPetEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterPetEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    pet_1_name: str
    """ 펫1 명 """

    pet_1_nickname: str
    """ 펫1 닉네임 """

    pet_1_icon: str
    """ 펫1 아이콘 """

    pet_1_description: Tuple[str]
    """ 펫1 설명 """

    pet_1_equipment: PetEquipment
    """ 펫1 장착 정보 """

    pet_1_auto_skill: PetAutoSkill
    """ 펫1 펫 버프 자동스킬 정보 """

    pet_1_skill: List[str]
    """ 펫1 펫 보유 스킬 """

    pet_1_pet_type: str
    """ 펫1 원더 펫 종류 """

    pet_1_date_expire: str
    """ 펫1 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    pet_1_appearance: str
    """ 펫1 외형 """

    pet_1_appearance_icon: str
    """ 펫1 외형 아이콘 """

    pet_2_name: str
    """ 펫2 명 """

    pet_2_nickname: str
    """ 펫2 닉네임 """

    pet_2_icon: str
    """ 펫2 아이콘 """

    pet_2_description: Tuple[str]
    """ 펫2 설명 """

    pet_2_equipment: PetEquipment
    """ 펫2 장착 정보 """

    pet_2_auto_skill: PetAutoSkill
    """ 펫2 펫 버프 자동스킬 정보 """

    pet_2_skill: List[str]
    """ 펫2 펫 보유 스킬 """

    pet_2_pet_type: str
    """ 펫2 원더 펫 종류 """

    pet_2_date_expire: str
    """ 펫2 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    pet_2_appearance: str
    """ 펫2 외형 """

    pet_2_appearance_icon: str
    """ 펫2 외형 아이콘 """

    pet_3_name: str
    """ 펫3 명 """

    pet_3_nickname: str
    """ 펫3 닉네임 """

    pet_3_icon: str
    """ 펫3 아이콘 """

    pet_3_description: Tuple[str]
    """ 펫3 설명 """

    pet_3_equipment: PetEquipment
    """ 펫3 장착 정보 """

    pet_3_auto_skill: PetAutoSkill
    """ 펫3 펫 버프 자동스킬 정보 """

    pet_3_skill: List[str]
    """ 펫3 펫 보유 스킬 """

    pet_3_pet_type: str
    """ 펫3 원더 펫 종류 """

    pet_3_date_expire: str
    """ 펫3 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    pet_3_appearance: str
    """ 펫3 외형 """

    pet_3_appearance_icon: str
    """ 펫3 외형 아이콘 """

    class PetEquipment(BaseModel):
        item_name: str
        """ 아이템 명 """

        item_icon: str
        """ 아이템 아이콘 """

        item_description: str
        """ 아이템 설명 """

        item_option: List[PetItemOption]
        """ 아이템 표기상 옵션 """

        scroll_upgrade: int
        """ 업그레이드 횟수 """

        scroll_upgradeable: int = Field(0, alias="scroll_upgradable")
        """ 업그레이드 가능 횟수 """

        item_shape: Optional[str]
        """ 아이템 외형 """

        item_shape_icon: Optional[str]
        """ 아이템 외형 아이콘 """

        class PetItemOption(BaseModel):
            option_type: str
            """ 옵션 타입 """

            option_value: str
            """ 옵션 값 """

    class PetAutoSkill(BaseModel):
        skill_1: str
        """ 첫 번째 슬롯에 등록된 자동 스킬 """

        skill_1_icon: str
        """ 첫 번째 슬롯에 등록된 자동 스킬 아이콘 """

        skill_2: str
        """ 두 번째 슬롯에 등록된 자동 스킬 """

        skill_2_icon: str
        """ 두 번째 슬롯에 등록된 자동 스킬 아이콘 """


class GetCharacterSkillRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterSkill(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    character_skill_grade: str
    """ 스킬 전직 차수 """

    character_skill: List[CharacterSkill]

    class CharacterSkill(BaseModel):
        skill_name: str
        """ 스킬 명 """

        skill_description: str
        """ 스킬 설명 """

        skill_level: int
        """ 스킬 레벨 """

        skill_effect: str
        """ 스킬 레벨 별 효과 설명 """

        skill_effect_next: str
        """ 다음 스킬 레벨 별 효과 설명 """

        skill_icon: str
        """ 스킬 아이콘 """


class GetCharacterLinkSkillRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterLinkSkill(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    character_link_skill: CharacterLinkSkill
    """ 링크 스킬 정보 """

    character_link_skill_preset_1: Optional[List[CharacterLinkSkill]]
    """ 링크 스킬 1번 프리셋 정보 """

    character_link_skill_preset_2: Optional[List[CharacterLinkSkill]]
    """ 링크 스킬 2번 프리셋 정보 """

    character_link_skill_preset_3: Optional[List[CharacterLinkSkill]]
    """ 링크 스킬 3번 프리셋 정보 """

    character_owned_link_skill: List[CharacterLinkSkill]
    """ 내 링크 스킬 정보 """

    character_owned_link_skill_preset_1: CharacterLinkSkill
    """ 내 링크 스킬 1번 프리셋 정보 """

    character_owned_link_skill_preset_2: CharacterLinkSkill
    """ 내 링크 스킬 2번 프리셋 정보 """

    character_owned_link_skill_preset_3: CharacterLinkSkill
    """ 내 링크 스킬 3번 프리셋 정보 """

    class CharacterLinkSkill(BaseModel):
        skill_name: Tuple[str]
        """ 스킬 명 """

        skill_description: str
        """ 스킬 설명 """

        skill_level: int
        """ 스킬 레벨 """

        skill_effect: str
        """ 스킬 효과 """

        skill_effect_next: str
        """ 다음 레벨의 스킬 효과 """

        skill_icon: str
        """ 스킬 아이콘 """


class GetCharacterVMatrixRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterVMatrix(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    character_v_core_equipment: List[CharacterVCoreEquipment]
    """ V코어 정보 """

    character_v_matrix_remain_slot_upgrade_point: int
    """ 캐릭터 잔여 매트릭스 강화 포인트 """

    class CharacterVCoreEquipment(BaseModel):
        slot_id: str
        """ 슬롯 인덱스 """

        slot_level: int
        """ 슬롯 레벨 """

        v_core_name: str
        """ 코어 명 """

        v_core_type: str
        """ 코어 타입 """

        v_core_level: int
        """ 코어 레벨 """

        v_core_skill_1: str
        """ 코어에 해당하는 스킬 명 """

        v_core_skill_2: Optional[str]
        """ (강화 코어인 경우) 코어에 해당하는 두 번째 스킬 명 """

        v_core_skill_3: Optional[str]
        """ (강화 코어인 경우) 코어에 해당하는 세 번째 스킬 명 """


class GetCharacterHexaMatrixRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterHexaMatrix(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_hexa_core_equipment: List[CharacterHexaCoreEquipment]
    """ HEXA 코어 정보 """

    class CharacterHexaCoreEquipment(BaseModel):
        hexa_core_name: str
        """ 코어 명 """

        hexa_core_level: int
        """ 코어 레벨 """

        hexa_core_type: str
        """ 코어 타입 """

        linked_skill: HexaCoreSkillLink
        """ 연결된 스킬"""

        class HexaCoreSkillLink(BaseModel):
            hexa_skill_id: str
            """ HEXA 스킬 명 """


class GetCharacterHexaMatrixStatRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterHexaMatrixStat(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    character_hexa_stat_core: CharacterHexaStatCore
    """ HEXA 스탯 코어 정보 """

    preset_hexa_stat_core: CharacterHexaStatCore
    """ 프리셋 HEXA 스탯 코어 정보 """

    class CharacterHexaStatCore(BaseModel):
        slot_id: str
        """ 슬롯 인덱스 """

        main_stat_name: str
        """ 메인 스탯 명 """

        sub_stat_name_1: str
        """ 첫 번째 서브 명 """

        sub_stat_name_2: str
        """ 두 번째 서브 명 """

        main_stat_level: int
        """ 메인 스탯 레벨 """

        sub_stat_level_1: str
        """ 첫 번째 서브 레벨 """

        sub_stat_level_2: str
        """ 두 번째 서브 레벨 """

        stat_grade: int
        """ 스탯 코어 등급 """


class GetCharacterDojangRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryCharacterDojang(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    world_name: str
    """ 월드 명 """

    dojang_best_floor: int
    """ 무릉도장 최고 기록 층수 """

    date_dojang_record: str
    """ 무릉도장 최고 기록 달성 일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    dojang_best_time: int
    """ 무릉도장 최고 층수 클리어에 걸린 시간 (초) """


class GetUserUnionRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryUserUnion(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    union_level: int
    """ 유니온 레벨 """

    union_grade: str
    """ 유니온 레벨 """

    union_artifact_level: Optional[int] = Field(None, alias="artifact_level")
    """ 아티팩트 레벨 """

    union_artifact_exp: Optional[int] = Field(None, alias="artifact_exp")
    """ 보유 아티팩트 경험치 """

    union_artifact_point: Optional[int] = Field(None, alias="artifact_point")
    """ 보유 아티팩트 포인트 """


class GetUserUnionRaiderRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryUserUnionRaider(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    union_raider_stat: List[str]
    """ 유니온 공격대원 효과 """

    union_occupied_stat: List[str]
    """ 유니온 공격대 점령 효과 """

    union_inner_stat: List[UnionInnerStat]
    """ 유니온 공격대 배치 """

    union_block: List[UnionBlock]
    """ 유니온 블록 정보 """

    class UnionInnerStat(BaseModel):
        stat_field_id: str
        """ 공격대 배치 위치 (11시 방향부터 시계 방향 순서대로 0~7) """

        stat_field_effect: str
        """ 해당 지역 점령 효과 """

    class UnionBlock(BaseModel):
        block_type: str
        """ 블록 모양 (전사, 마법사, 궁수, 도적, 해적, 메이플m, 하이브리드) """

        block_class: str
        """ 블록 해당 캐릭터 직업 """

        block_level: str
        """ 블록 해당 캐릭터 레벨 """

        block_control_point: BlockControlPoint
        """ 블록 기준점 좌표 """

        block_position: List[BlockPosition]
        """ 블록이 차지하고 있는 영역 좌표들 (null: 미 배치 시) """

        class BlockControlPoint(BaseModel):
            """
            블록 기준점 좌표

            중앙 4칸 중 오른쪽 아래 칸이 x : 0, y : 0 포지션
            좌측으로 1칸씩 이동하면 x가 1씩 감소
            우측으로 1칸씩 이동하면 x가 1씩 증가
            아래로 1칸씩 이동하면 y가 1씩 감소
            위로 1칸씩 이동하면 y가 1씩 증가
            """

            x: int
            """ 블록 기준점 X좌표"""

            y: int
            """ 블록 기준점 Y좌표"""

        class BlockPosition(BaseModel):
            """블록이 차지하고 있는 영역 좌표들 (null: 미 배치 시)"""

            x: int
            """ 블록 X좌표"""

            y: int
            """ 블록 Y좌표"""


class GetUserUnionArtifactRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Optional[str]


class MapleStoryUserUnionArtifact(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    union_artifact_effect: List[UnionArtifactEffect]
    """ 유니온 아티팩트 효과 정보 """

    union_artifact_crystal: List[UnionArtifactCrystal]
    """ 유니온 아티팩트 크리스탈 정보 """

    union_artifact_remain_ap: int
    """ 잔여 아티팩트 AP """

    class UnionArtifactEffect(BaseModel):
        name: str
        """ 아티팩트 효과 명 """

        name: str
        """ 아티팩트 효과 레벨 """

    class UnionArtifactCrystal(BaseModel):
        name: str
        """ 아티팩트 크리스탈 명 """

        validity_flag: str
        """ 능력치 유효 여부 (0:유효, 1:유효하지 않음) """

        date_expire: Optional[str]
        """ 능력치 유효 기간(KST) """

        level: int
        """ 아티팩트 크리스탈 등급 """

        crystal_option_name_1: str
        """ 아티팩트 크리스탈 첫 번째 옵션 명 """

        crystal_option_name_2: str
        """ 아티팩트 크리스탈 두 번째 옵션 명 """

        crystal_option_name_3: str
        """ 아티팩트 크리스탈 세 번째 옵션 명 """


class GetGuildIdRequestParam(TypedDict, total=False):
    world_name: Required[str]
    guild_name: Required[str]


class MapleStoryGuildId(BaseModel):
    oguild_id: str
    """ 길드 식별자 """


class GetGuildBasicRequestParam(TypedDict, total=False):
    oguild_id: Required[str]
    """ 길드 식별자 """


class MapleStoryGuildBasic(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    world_name: str
    """ 월드 명 """

    guild_name: str
    """ 길드 명 """

    guild_level: int
    """ 길드 레벨 """

    guild_fame: int
    """ 길드 명성치 """

    guild_point: int
    """ 길드 포인트(GP) """

    guild_master_name: str
    """ 길드 마스터 캐릭터 명 """

    guild_member_count: int
    """ 길드원 수 """

    guild_member: List[str]
    """ 길드원 목록 """

    guild_skill: List[GuildSkill]
    """ 길드 스킬 목록"""

    guild_noblesse_skill: List[GuildSkill]
    """ 노블레스 스킬 목록 """

    class GuildSkill(BaseModel):
        skill_name: str
        """ 스킬 명 """

        skill_description: str
        """ 스킬 설명 """

        skill_level: int
        """ 스킬 레벨 """

        skill_effect: str
        """ 스킬 레벨 별 효과 """

        skill_icon: str
        """ 스킬 아이콘 """


class GetOverallRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    world_name: str
    """ 월드 명 

    Available values : 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
    """

    world_type: str
    """ 월드 타입 (0: 일반, 1: 리부트) (기본 값은 0이며, world_name 입력 시 미 반영) """

    class_: Annotated[str, "class"]
    """ 직업 및 전직 

    Available values: 
        - 초보자-전체 전직 
        - 전사-전체 전직
        - 전사-검사
        - 전사-파이터
        - 전사-페이지
        - 전사-스피어맨
        - 전사-크루세이더
        - 전사-나이트
        - 전사-버서커
        - 전사-히어로
        - 전사-팔라딘
        - 전사-다크나이트
        - 마법사-전체 전직
        - 마법사-매지션
        - 마법사-위자드(불,독)
        - 마법사-위자드(썬,콜)
        - 마법사-클레릭
        - 마법사-메이지(불,독)
        - 마법사-메이지(썬,콜)
        - 마법사-프리스트
        - 마법사-아크메이지(불,독)
        - 마법사-아크메이지(썬,콜)
        - 마법사-비숍
        - 궁수-전체 전직
        - 궁수-아처
        - 궁수-헌터
        - 궁수-사수
        - 궁수-레인저
        - 궁수-저격수
        - 궁수-보우마스터
        - 궁수-신궁
        - 궁수-아처(패스파인더)
        - 궁수-에인션트아처
        - 궁수-체이서
        - 궁수-패스파인더
        - 도적-전체 전직
        - 도적-로그
        - 도적-어쌔신
        - 도적-시프
        - 도적-허밋
        - 도적-시프마스터
        - 도적-나이트로드
        - 도적-섀도어
        - 도적-세미듀어러
        - 도적-듀어러
        - 도적-듀얼마스터
        - 도적-슬래셔
        - 도적-듀얼블레이더
        - 해적-전체 전직
        - 해적-해적
        - 해적-인파이터
        - 해적-건슬링거
        - 해적-캐논슈터
        - 해적-버커니어
        - 해적-발키리
        - 해적-캐논블래스터
        - 해적-바이퍼
        - 해적-캡틴
        - 해적-캐논마스터
        - 기사단-전체 전직
        - 기사단-노블레스
        - 기사단-소울마스터
        - 기사단-플레임위자드
        - 기사단-윈드브레이커
        - 기사단-나이트워커
        - 기사단-스트라이커
        - 기사단-미하일
        - 아란-전체 전직
        - 에반-전체 전직
        - 레지스탕스-전체 전직
        - 레지스탕스-시티즌
        - 레지스탕스-배틀메이지
        - 레지스탕스-와일드헌터
        - 레지스탕스-메카닉
        - 레지스탕스-데몬슬레이어
        - 레지스탕스-데몬어벤져
        - 레지스탕스-제논
        - 레지스탕스-블래스터
        - 메르세데스-전체 전직
        - 팬텀-전체 전직
        - 루미너스-전체 전직
        - 카이저-전체 전직
        - 엔젤릭버스터-전체 전직
        - 초월자-전체 전직
        - 초월자-제로
        - 은월-전체 전직
        - 프렌즈 월드-전체 전직
        - 프렌즈 월드-키네시스
        - 카데나-전체 전직
        - 일리움-전체 전직
        - 아크-전체 전직
        - 호영-전체 전직
        - 아델-전체 전직
        - 카인-전체 전직
        - 라라-전체 전직
        - 칼리-전체 전직
    """

    ocid: str
    """ 캐릭터 식별자 """

    page: int
    """ 페이지 번호 """


class MapleStoryOverallRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        class_name: str
        """ 직업 명 """

        sub_class_name: str
        """ 전직 직업 명 """

        character_level: int
        """ 캐릭터 레벨 """

        character_exp: int
        """ 캐릭터 경험치 """

        character_popularity: int
        """ 캐릭터 인기도 """

        character_guildname: str
        """ 길드 명 """


class GetUnionRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    world_name: str
    """ 월드 명 

    Available values : 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
    """

    ocid: str
    """ 캐릭터 식별자 """

    page: int
    """ 페이지 번호 """


class MapleStoryUnionRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        class_name: str
        """ 직업 명 """

        sub_class_name: str
        """ 전직 직업 명 """

        union_level: int
        """ 유니온 레벨 """

        union_power: int
        """ 유니온 파워 """


class GetGuildRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    world_name: str
    """ 월드 명 

    Available values : 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
    """

    ranking_type: Required[str]
    """ 랭킹 타입 (0:주간 명성치, 1:플래그 레이스, 2:지하 수로) """

    guild_name: str
    """ 길드 명 """

    page: int
    """ 페이지 번호 """


class MapleStoryGuildRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        guild_name: str
        """ 길드 명 """

        world_name: str
        """ 월드 명 """

        guild_level: int
        """ 길드 레벨 """

        guild_master_name: str
        """ 길드 마스터 캐릭터 명 """

        guild_mark: str
        """ 길드 마크 """

        guild_point: int
        """ 길드 포인트 """


class GetDojangRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    world_name: str
    """ 월드 명 

    Available values : 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
    """

    difficulty: Required[str]
    """ 구간 (0:일반, 1:통달) """

    class_: Annotated[str, "class"]
    """ 직업 및 전직 

    Available values: 
        - 초보자-전체 전직 
        - 전사-전체 전직
        - 전사-검사
        - 전사-파이터
        - 전사-페이지
        - 전사-스피어맨
        - 전사-크루세이더
        - 전사-나이트
        - 전사-버서커
        - 전사-히어로
        - 전사-팔라딘
        - 전사-다크나이트
        - 마법사-전체 전직
        - 마법사-매지션
        - 마법사-위자드(불,독)
        - 마법사-위자드(썬,콜)
        - 마법사-클레릭
        - 마법사-메이지(불,독)
        - 마법사-메이지(썬,콜)
        - 마법사-프리스트
        - 마법사-아크메이지(불,독)
        - 마법사-아크메이지(썬,콜)
        - 마법사-비숍
        - 궁수-전체 전직
        - 궁수-아처
        - 궁수-헌터
        - 궁수-사수
        - 궁수-레인저
        - 궁수-저격수
        - 궁수-보우마스터
        - 궁수-신궁
        - 궁수-아처(패스파인더)
        - 궁수-에인션트아처
        - 궁수-체이서
        - 궁수-패스파인더
        - 도적-전체 전직
        - 도적-로그
        - 도적-어쌔신
        - 도적-시프
        - 도적-허밋
        - 도적-시프마스터
        - 도적-나이트로드
        - 도적-섀도어
        - 도적-세미듀어러
        - 도적-듀어러
        - 도적-듀얼마스터
        - 도적-슬래셔
        - 도적-듀얼블레이더
        - 해적-전체 전직
        - 해적-해적
        - 해적-인파이터
        - 해적-건슬링거
        - 해적-캐논슈터
        - 해적-버커니어
        - 해적-발키리
        - 해적-캐논블래스터
        - 해적-바이퍼
        - 해적-캡틴
        - 해적-캐논마스터
        - 기사단-전체 전직
        - 기사단-노블레스
        - 기사단-소울마스터
        - 기사단-플레임위자드
        - 기사단-윈드브레이커
        - 기사단-나이트워커
        - 기사단-스트라이커
        - 기사단-미하일
        - 아란-전체 전직
        - 에반-전체 전직
        - 레지스탕스-전체 전직
        - 레지스탕스-시티즌
        - 레지스탕스-배틀메이지
        - 레지스탕스-와일드헌터
        - 레지스탕스-메카닉
        - 레지스탕스-데몬슬레이어
        - 레지스탕스-데몬어벤져
        - 레지스탕스-제논
        - 레지스탕스-블래스터
        - 메르세데스-전체 전직
        - 팬텀-전체 전직
        - 루미너스-전체 전직
        - 카이저-전체 전직
        - 엔젤릭버스터-전체 전직
        - 초월자-전체 전직
        - 초월자-제로
        - 은월-전체 전직
        - 프렌즈 월드-전체 전직
        - 프렌즈 월드-키네시스
        - 카데나-전체 전직
        - 일리움-전체 전직
        - 아크-전체 전직
        - 호영-전체 전직
        - 아델-전체 전직
        - 카인-전체 전직
        - 라라-전체 전직
        - 칼리-전체 전직
    """

    ocid: str
    """ 캐릭터 식별자 """

    page: int
    """ 페이지 번호 """


class MapleStoryDojangRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        class_name: str
        """ 직업 명 """

        sub_class_name: str
        """ 전직 직업 명 """

        character_level: int
        """ 캐릭터 레벨 """

        dojang_floor: int
        """ 무릉도장 구간 """

        dojang_time_record: int
        """ 무릉도장 클리어 시간 기록 (초 단위) """


class GetTheSeedRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    world_name: str
    """ 월드 명 

    Available values: 스카니아, 베라, 루나, 제니스, 크로아, 유니온, 엘리시움, 이노시스, 레드, 오로라, 아케인, 노바, 리부트, 리부트2, 버닝, 버닝2, 버닝3
    """

    ocid: str
    """ 캐릭터 식별자 """

    page: int
    """ 페이지 번호 """


class MapleStoryTheSeedRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        class_name: str
        """ 직업 명 """

        sub_class_name: str
        """ 전직 직업 명 """

        character_level: int
        """ 캐릭터 레벨 """

        theseed_floor: int
        """ 더 시드 도달 층 """

        theseed_time_record: int
        """ 더 시드 클리어 시간 기록 (초 단위) """


class GetAchievementRankingRequestParam(TypedDict, total=False):
    date: Required[str]
    """ 조회 기준일 (KST) """

    ocid: str
    """ 캐릭터 식별자 """

    page: int
    """ 페이지 번호 """


class MapleStoryAchievementRanking(BaseModel):
    ranking: List[Ranking]

    class Ranking(BaseModel):
        date: str
        """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

        ranking: int
        """ 종합 랭킹 순위 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        class_name: str
        """ 직업 명 """

        sub_class_name: str
        """ 전직 직업 명 """

        trophy_grade: str
        """ 업적 등급 """

        trophy_score: int
        """ 업적 점수 """


class GetStartforceHistoryRequestParam(TypedDict, total=False):
    count: Required[int]
    """ 한번에 가져오려는 결과의 갯수(최소 10, 최대 1000) """

    date: Required[str]
    """ 조회 기준일 (KST) """

    cursor: str
    """ 페이징 처리를 위한 cursor (date가 없는 경우 필수이며 date와 함께 사용 불가) """


class MapleStoryStartForceHistory(BaseModel):
    count: int
    """ 결과 건 수 """

    next_cursor: str
    """ 페이징 처리를 위한 cursor """

    starforce_history: List[StartForceHistory]

    class StartForceHistory(BaseModel):
        id: str
        """ 스타포스 히스토리 식별자 """

        item_upgrade_result: str
        """ 강화 시도 결과 """

        before_starforce_count: int
        """ 강화 시도 전 스타포스 수치 """

        after_starforce_count: int
        """ 강화 시도 전 스타포스 수치 """

        starcatch_result: str
        """ 스타 캐치 """

        superior_item_flag: str
        """ 슈페리얼 장비 """

        destory_defence: str
        """ 파괴 방지 """

        chance_time: str
        """ 파괴 방지 """

        event_field_flag: str
        """ 파괴 방지 필드 이벤트 """

        upgrade_item: str
        """ 사용 주문서 명 """

        protect_shield: str
        """ 프로텍트 실드 """

        bonus_stat_upgrade: str
        """ 보너스 스탯 부여 아이템 여부 """

        character_name: str
        """ 캐릭터 명 """

        world_name: str
        """ 월드 명 """

        target_item: str
        """ 대상 장비 아이템 명 """

        date_create: str
        """ 강화 일시 (KST) """

        starforce_event_list: List[StartForceEvent]
        """ 진행 중인 스타포스 강화 이벤트 정보 """

        class StartForceEvent(BaseModel):
            success_rate: str
            """ 이벤트 성공 확률 """

            cost_discount_rate: str
            """ 이벤트 비용 할인율 """

            plus_value: str
            """ 이벤트 강화 수치 가중값 """

            starfoce_event_range: str
            """ 이벤트 적용 강화 시도 가능한 n성 범위 """
