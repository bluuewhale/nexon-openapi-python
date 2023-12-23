from __future__ import annotations
from datetime import datetime, timezone, timedelta

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


KST_TIMEZONE = timezone(timedelta(hours=9))
ONE_DAY = timedelta(days=1)


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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

        return self._get(
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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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
        date = validate_date(date) if date is not None else get_date_yesterday_in_kst()

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


def validate_date(date: str) -> str:
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        raise ValueError("date must be in YYYY-mm-dd format")


def get_date_yesterday_in_kst() -> str:
    return (datetime.now(KST_TIMEZONE) - ONE_DAY).strftime("%Y-%m-%d")


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
        description: str
        """ 캐시 장비 컬러링 프리즘 정보 """

        color_range: str
        """ 컬러링프리즘 색상 범위 """

        hue: int
        """ 컬러링프리즘 색조 """

        saturation: int
        """ 컬러링프리즘 채도 """

        value: int
        """ 컬러링프리즘 명도 """


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


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


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


class GetCharacterPopularityRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


class MapleStoryCharacterPopularity(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    popularity: int
    """ 캐릭터 인기도 """


class GetCharacterStatRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


class MapleStoryCharacterAbility(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    ability_grade: str
    """ 어빌리티 등급 """

    ability_info: List[AbilityInfo]
    """ 어빌리티 정보 """

    remain_fame: int
    """ 보유 명성치 """

    class AbilityInfo(BaseModel):
        ability_no: str
        """ 어빌리티 번호 """

        ability_grade: str
        """ 어빌리티 등급 """

        ability_value: str
        """ 어빌리티 옵션 및 수치 """


class GetCharacterItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


class MapleStoryCharacterItemEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_gender: str
    """ 캐릭터 성별 """

    character_class: str
    """ 캐릭터 직업 """

    item_equipment: ItemEquipment
    """ 장비 정보 """

    title: Title
    """ 칭호 정보 """

    dragon_equipment: Optional[ItemEquipment]
    """ 에반 드래곤 장비 정보 (에반인 경우 응답) """

    mechanic_equipment: Optional[ItemEquipment]
    """ 메카닉 장비 정보 (메카닉인 경우 응답) """

    class Title(BaseModel):
        description: str
        """ 칭호 정보 """

        title_name: str
        """ 칭호 장비 명 """

        title_icon: str
        """ 칭호 아이콘 """

        title_description: str
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

        item_description: str
        """ 장비 설명 """

        item_shape_name: str
        """ 장비 외형 """

        item_shape_icon: str
        """ 장비 외형 아이콘 """

        gender: str
        """ 전용 성별 """

        potential_option_grade: str
        """ 잠재능력 등급 """

        additional_potential_option_grade: str
        """ 에디셔널 잠재능력 등급 """

        potential_option_1: str
        """ 잠재능력 첫 번째 옵션 """

        potential_option_2: str
        """ 잠재능력 두 번째 옵션 """

        potential_option_3: str
        """ 잠재능력 세 번째 옵션 """

        addtional_potential_option_1: str
        """ 에디셔널 잠재능력 첫 번째 옵션 """

        addtional_potential_option_2: str
        """ 에디셔널 잠재능력 두 번째 옵션 """

        addtional_potential_option_3: str
        """ 에디셔널 잠재능력 세 번째 옵션 """

        equipment_level_incrase: int
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

        scroll_upgradable_count: str
        """ 업그레이드 가능 횟수 
        TODO: 반환되는 정보가 실제 API 명세와 일치하지 않음, 해당 값은 응답 값을 기준으로 작성
        """

        soul_name: str
        """ 소울 명 """

        soul_option: str
        """ 소울 옵션 """

        starforce: str
        """ 강화 단계 """

        starforce_scroll_flag: str
        """ 놀라운 장비 강화 주문서 사용 여부 (0: 미사용, 1: 사용)"""

        special_ring_level: int
        """ 특수 반지 레벨 """

        date_expire: str
        """ 장비 유효 기간(KST) """

        item_total_option: MapleStoryCharacterItemEquipment.ItemTotalOption
        item_base_option: MapleStoryCharacterItemEquipment.ItemBaseOption
        item_exceptional_option: MapleStoryCharacterItemEquipment.ItemExceptionalOption
        item_add_option: MapleStoryCharacterItemEquipment.ItemAddOption
        item_etc_option: MapleStoryCharacterItemEquipment.ItemEtcOption
        item_starforce_option: MapleStoryCharacterItemEquipment.ItemEtcOption

    class ItemExceptionalOption(BaseModel):
        description: str
        """ 장비 최종 옵션 정보 """

        str: str
        """ STR """

        dex: str
        """ DEX """

        int: str
        """ INT """

        luck: str
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
        all_stat: str
        """ 올스탯(%) """

        damage: str
        """ 데미지(%) """

    class ItemTotalOption(ItemAddOption):
        ignore_monster_armot: str
        """ 몬스터 방어율 무시(%) """

        max_hp_rate: str
        """ 최대 HP(%) """

        max_mp_rate: str
        """ 최대 MP(%) """

        equipment_level_decrease: int
        """ 착용 레벨 감소 """

    class ItemBaseOption(ItemAddOption):
        ignore_monster_armot: str
        """ 몬스터 방어율 무시(%) """

        max_hp_rate: str
        """ 최대 HP(%) """

        max_mp_rate: str
        """ 최대 MP(%) """

        base_level_decrease: int
        """ 기본 착용 레벨 """


class GetCharacterCashItemEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


class MapleStoryCharacterCashItemEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_gender: str
    """ 캐릭터 성별 """

    character_class: str
    """ 캐릭터 직업 """

    preset_no: int
    """ 적용 중인 캐시 장비 프리셋 번호 """

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

    class CharacterCashItemEquipment(CashItemEquipment):
        base_preset_item_disable_flag: str
        """ 다른 프리셋에서 장비 추가 장착 없이 프리셋의 장비 공유를 비활성화 했는지 여부 """


class GetCharacterSymbolEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


class MapleStoryCharacterAndroidEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    android_name: str
    """ 안드로이드 명 """

    android_nickname: str
    """ 안드로이드 닉네임 """

    android_icon: str
    """ 안드로이드 아이콘 """

    android_description: Optional[str]
    """ 안드로이드 아이템 설명 """

    android_hair: CharacterHair
    """ 안드로이드 헤어 정보 """

    android_face: CharacterFace
    """ 안드로이드 성형 정보 """

    android_skin_name: str
    """ 안드로이드 피부 명 """

    android_cash_item_equipment: List[CashItemEquipment]
    """ 안드로이드 캐시 아이템 장착 정보 """


class GetCharacterPetEquipmentRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


class MapleStoryCharacterPetEquipment(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    pet_1_name: str
    """ 펫1 명 """

    pet_1_nickname: str
    """ 펫1 닉네임 """

    pet_1_icon: str
    """ 펫1 아이콘 """

    pet_1_description: str
    """ 펫1 설명 """

    pet_1_equipment: PetEquipment
    """ 펫1 장착 정보 """

    pet_1_skill: PetAutoSkill
    """ 펫1 펫 버프 자동스킬 정보 
    TODO: 반환되는 정보가 실제 API 명세와 일치하지 않음, 해당 값은 응답 값을 기준으로 작성
    """

    pet_1_pet_type: str
    """ 펫1 원더 펫 종류 """

    pet_1_date_expire: str
    """ 펫1 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    pet_2_name: str
    """ 펫2 명 """

    pet_2_nickname: str
    """ 펫2 닉네임 """

    pet_2_icon: str
    """ 펫2 아이콘 """

    pet_2_description: str
    """ 펫2 설명 """

    pet_2_equipment: PetEquipment
    """ 펫2 장착 정보 """

    pet_2_skill: PetAutoSkill
    """ 펫2 펫 버프 자동스킬 정보 
    TODO: 반환되는 정보가 실제 API 명세와 일치하지 않음, 해당 값은 응답 값을 기준으로 작성
    """

    pet_2_pet_type: str
    """ 펫2 원더 펫 종류 """

    pet_2_date_expire: str
    """ 펫2 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    pet_3_name: str
    """ 펫3 명 """

    pet_3_nickname: str
    """ 펫3 닉네임 """

    pet_3_icon: str
    """ 펫3 아이콘 """

    pet_3_description: str
    """ 펫3 설명 """

    pet_3_equipment: PetEquipment
    """ 펫3 장착 정보 """

    pet_3_skill: PetAutoSkill
    """ 펫3 펫 버프 자동스킬 정보 
    TODO: 반환되는 정보가 실제 API 명세와 일치하지 않음, 해당 값은 응답 값을 기준으로 작성
    """

    pet_3_pet_type: str
    """ 펫3 원더 펫 종류 """

    pet_3_date_expire: str
    """ 펫3 마법의 시간 (KST, 시간 단위 데이터로 분은 일괄 0으로 표기) """

    class PetEquipment(BaseModel):
        item_name: str
        """ 아이템 명 """

        item_icon: str
        """ 아이템 아이콘 """

        item_description: str
        """ 아이템 설명 """

        item_option: PetItemOption
        """ 아이템 표기상 옵션 """

        scroll_upgrade: int
        """ 업그레이드 횟수 """

        scroll_upgradable: int
        """ 업그레이드 가능 횟수 
        TODO: 반환되는 정보가 실제 API 명세와 일치하지 않음, 해당 값은 응답 값을 기준으로 작성
        """

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
    date: Required[str]


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

        skill_icon: str
        """ 스킬 아이콘 """


class GetCharacterLinkSkillRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


class MapleStoryCharacterLinkSkill(BaseModel):
    date: str
    """ 조회 기준일 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기) """

    character_class: str
    """ 캐릭터 직업 """

    character_skill_grade: str
    """ 스킬 전직 차수 """

    character_link_skill: List[CharacterLinkSkill]
    """ 링크 스킬 정보 """

    character_owned_link_skill: List[CharacterLinkSkill]
    """ 내 링크 스킬 정보 """

    class CharacterLinkSkill(BaseModel):
        skill_name: str
        """ 스킬 명 """

        skill_description: str
        """ 스킬 설명 """

        skill_level: int
        """ 스킬 레벨 """

        skill_effect: str
        """ 스킬 레벨 별 효과 설명 """

        skill_icon: str
        """ 스킬 아이콘 """


class GetCharacterVMatrixRequestParam(TypedDict, total=False):
    ocid: Required[str]
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


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
    date: Required[str]


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
