from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Union
from typing_extensions import Required, TypedDict


import httpx

from .._types import NOT_GIVEN, Body, ModelBuilderProtocol, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI, NexonOpenAPIAsync


class TFD(SyncAPIResource):
    """
    link: https://openapi.nexon.com/game/tfd/?id=20

    - Game data for The First Descendant becomes available after 10 minutes on average.
    - Please note that the OUID may change due to game content updates. Be cautious when renewing services based on the OUID.
    - For the interpretation of various ID values such as those for descendants, weapons, etc., please refer to the separately provided metadata API (/meta/).
    - Nickname must distinguish between uppercase and lowercase letters.
    """

    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ouid(
        self,
        *,
        user_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDOuid:
        """Retrieves the account identifier (OUID)"""

        return self._get(
            "tfd/v1/id",
            options=make_request_options(
                query=maybe_transform({"user_name": user_name}, GetOuidRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDOuid,
        )

    def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserBasic:
        """Retrieves basic information of the user"""

        return self._get(
            "tfd/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserBasic,
        )

    def get_user_descendant(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserDescendant:
        """Retrieves information about the equipped descendant."""

        return self._get(
            "tfd/v1/user/descendant",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserDescendantRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserDescendant,
        )

    def get_user_weapon(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserWeapon:
        """Retrieves information about the equipped weapon.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es


        """

        return self._get(
            "tfd/v1/user/weapon",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "language_code": language_code}, GetUserWeaponRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserWeapon,
        )

    def get_user_reactor(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserReactor:
        """Retrieves information about the equipped reactor.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es


        """

        return self._get(
            "tfd/v1/user/reactor",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "language_code": language_code}, GetUserReactorRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserReactor,
        )

    def get_user_external_component(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserExternalComponent:
        """Retrieves information about external components equipped in all slots.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            "tfd/v1/user/external-component",
            options=make_request_options(
                query=maybe_transform(
                    {"ouid": ouid, "language_code": language_code}, GetUserExternalComponentRequestParam
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserExternalComponent,
        )

    # metadata
    def get_descendant_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDDescendantMetadata]:
        """Retrieves descendant metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/descendant.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDDescendantMetadata],
        )

    def get_weapon_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDWeaponMetadata]:
        """Retrieves weapon metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/weapon.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDWeaponMetadata],
        )

    def get_module_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDModuleMetadata]:
        """Retrieves module metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/module.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDModuleMetadata],
        )

    def get_reactor_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDReactorMetadata]:
        """Retrieves reactor metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/reactor.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDReactorMetadata],
        )

    def get_external_component_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDExternalComponentMetadata]:
        """Retrieves external component metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/external-component.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDExternalComponentMetadata],
        )

    def get_reward_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDRewardMetadata]:
        """Retrieves reward metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/reward.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDRewardMetadata],
        )

    def get_stat_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDStatMetadata]:
        """Retrieves stat metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/stat.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDStatMetadata],
        )

    def get_void_battle_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDVoidBattleMetadata]:
        """Retrieves void battle metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/void-battle.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDVoidBattleMetadata],
        )

    def get_title_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDTitleMetadata]:
        """Retrieves title metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return self._get(
            f"static/tfd/meta/{language_code}/title.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDTitleMetadata],
        )


class TFDAsync(AsyncAPIResource):
    """
    link: https://openapi.nexon.com/game/tfd/?id=20

    - Game data for The First Descendant becomes available after 10 minutes on average.
    - Please note that the OUID may change due to game content updates. Be cautious when renewing services based on the OUID.
    - For the interpretation of various ID values such as those for descendants, weapons, etc., please refer to the separately provided metadata API (/meta/).
    - Nickname must distinguish between uppercase and lowercase letters.
    """

    def __init__(self, client: NexonOpenAPIAsync) -> None:
        super().__init__(client)

    async def get_ouid(
        self,
        *,
        user_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDOuid:
        """Retrieves the account identifier (OUID)"""
        return await self._get(
            "tfd/v1/id",
            options=make_request_options(
                query=maybe_transform({"user_name": user_name}, GetOuidRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDOuid,
        )

    async def get_user_basic(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserBasic:
        """Retrieves basic information of the user"""

        return await self._get(
            "tfd/v1/user/basic",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserBasic,
        )

    async def get_user_descendant(
        self,
        *,
        ouid: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserDescendant:
        """Retrieves information about the equipped descendant."""

        return await self._get(
            "tfd/v1/user/descendant",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid}, GetUserDescendantRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserDescendant,
        )

    async def get_user_weapon(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserWeapon:
        """Retrieves information about the equipped weapon.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es


        """

        return await self._get(
            "tfd/v1/user/weapon",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "language_code": language_code}, GetUserWeaponRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserWeapon,
        )

    async def get_user_reactor(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserReactor:
        """Retrieves information about the equipped reactor.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es


        """

        return await self._get(
            "tfd/v1/user/reactor",
            options=make_request_options(
                query=maybe_transform({"ouid": ouid, "language_code": language_code}, GetUserReactorRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserReactor,
        )

    async def get_user_external_component(
        self,
        *,
        ouid: str,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TFDUserExternalComponent:
        """Retrieves information about external components equipped in all slots.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            "tfd/v1/user/external-component",
            options=make_request_options(
                query=maybe_transform(
                    {"ouid": ouid, "language_code": language_code}, GetUserExternalComponentRequestParam
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=TFDUserExternalComponent,
        )

    # metadata
    async def get_descendant_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDDescendantMetadata]:
        """Retrieves descendant metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/descendant.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDDescendantMetadata],
        )

    async def get_weapon_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDWeaponMetadata]:
        """Retrieves weapon metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/weapon.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDWeaponMetadata],
        )

    async def get_module_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDModuleMetadata]:
        """Retrieves module metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/module.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDModuleMetadata],
        )

    async def get_reactor_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDReactorMetadata]:
        """Retrieves reactor metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/reactor.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDReactorMetadata],
        )

    async def get_external_component_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDExternalComponentMetadata]:
        """Retrieves external component metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/external-component.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDExternalComponentMetadata],
        )

    async def get_reward_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDRewardMetadata]:
        """Retrieves reward metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/reward.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDRewardMetadata],
        )

    async def get_stat_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDStatMetadata]:
        """Retrieves stat metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/stat.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDStatMetadata],
        )

    async def get_void_battle_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDVoidBattleMetadata]:
        """Retrieves void battle metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/void-battle.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDVoidBattleMetadata],
        )

    async def get_title_metadata(
        self,
        *,
        language_code: str = "en",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> List[TFDTitleMetadata]:
        """Retrieves title metadata.

        language code
            Available values : ko, en, de, fr, ja, zh-CN, zh-TW, it, pl, pt, ru, es
        """

        return await self._get(
            f"static/tfd/meta/{language_code}/title.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=List[TFDTitleMetadata],
        )


# common
class TFDModule(BaseModel):
    module_slot_id: str
    """ module slot identifier """

    module_id: str
    """ module identifier (refer to /meta/module) API """

    module_enchant_level: int
    """ module enchantment level """


class TFDAdditionalStat(BaseModel):
    additional_stat_name: str
    """Weapon random option name"""

    additional_stat_value: str
    """ Weapon random option value """


# ouid
class GetOuidRequestParam(TypedDict, total=True):
    user_name: Required[str]


class TFDOuid(BaseModel):
    ouid: str


# user basic
class GetUserBasicRequestParam(TypedDict, total=True):
    ouid: Required[str]


class TFDUserBasic(BaseModel):
    ouid: str
    """ OUID """

    user_name: str
    """ Nickname
    example: Nickname#1234
    """

    platform_type: str
    """ platform type """

    mastery_rank_level: int
    """ mastry rank """

    mastery_rank_exp: int
    """ mastry rank exp """

    title_prefix_id: str
    """ prefix title identifier (refer to /meta/title API) """

    title_suffix_id: str
    """ suffix title identifier (refer to /meta/title API) """

    os_language: str
    """ OS language settings """

    game_language: str
    """ game language settings """


# user descendant
class GetUserDescendantRequestParam(TypedDict, total=True):
    ouid: Required[str]


class TFDUserDescendant(BaseModel):
    ouid: str
    """ OUID """

    user_name: str
    """ Nickname
    example: Nickname#1234
    """

    descendant_id: str
    """ descendant identifier (refer to /meta/descendan API) """

    descendant_slot_id: str
    """ descendant slot identifier """

    descendant_level: int
    """ descendant level """

    descendant_max_capacity: Optional[int]
    """ max equippable module capacity """

    module_max_capacity: int
    module_capacity: int
    module: List[TFDModule]


# user weapon
class GetUserWeaponRequestParam(TypedDict, total=True):
    ouid: Required[str]
    language_code: Required[str]


class TFDUserWeapon(BaseModel):
    ouid: str
    """ OUID """

    user_name: str
    """ Nickname
    example: Nickname#1234
    """

    weapon: List[TFDWeapon]

    class TFDWeapon(BaseModel):
        module_max_capacity: int
        """ max equippable module capacity """

        module_capacity: int
        """ equipped capacity """

        weapon_slot_id: str
        """ weapon slot identifier """

        weapon_id: str
        """ weapon identifier (refer to /meta/weapon API) """

        weapon_level: int
        """ weapon level """

        perk_ability_enchant_level: Optional[int]
        """ weapon unique ability enchantment level """

        weapon_additional_stat: List[TFDAdditionalStat]
        """ weapon random option information """

        module: List[TFDModule]


# user reactor
class GetUserReactorRequestParam(TypedDict, total=True):
    ouid: Required[str]
    language_code: Required[str]


class TFDUserReactor(BaseModel):
    ouid: str
    """ OUID """

    user_name: str
    """ Nickname
    example: Nickname#1234
    """

    reactor_id: str
    """ reactor identifier (refer to /meta/reactor API) """

    reactor_slot_id: str
    """ reactor slot id """

    reactor_level: int
    """ reactor level """

    reactor_additional_stat: List[TFDAdditionalStat]
    """ reactor additional stat """

    reactor_enchant_level: int
    """ reactor enchantment level """


# user external componenet
class GetUserExternalComponentRequestParam(TypedDict, total=True):
    ouid: Required[str]


class TFDUserExternalComponent(BaseModel):
    ouid: str
    """ OUID """

    user_name: str
    """ Nickname
    example: Nickname#1234
    """

    external_component: List[TFDExternalComponent]

    class TFDExternalComponent(BaseModel):
        external_component_slot_id: str
        """ External component slot identifier """

        external_component_id: str
        """ External component identifier (refer to /meta/external-component) API """

        external_component_level: int
        """ External component level """

        external_component_additional_stat: List[TFDAdditionalStat]


# descendant metadata
class TFDDescendantMetadata(BaseModel):
    descendant_id: str
    descendant_name: str
    descendant_image_url: str
    descendant_stat: List[DescendantStat]
    descendant_skill: List[DescendantSkill]

    class DescendantStat(BaseModel):
        level: int
        stat_detail: List[StatDetail]

        class StatDetail(BaseModel):
            stat_type: str
            stat_value: int

    class DescendantSkill(BaseModel):
        skill_type: str
        skill_name: str
        element_type: str
        arche_type: str
        skill_image_url: str
        skill_description: str


# class TFDDescendantMetadataParser(ModelBuilderProtocol):
#     @classmethod
#     def build(
#         cls: Type[_T],
#         *,
#         response: Response,
#         data: object,
#     ) -> _T:
#         ...


# weapon metadata
class TFDWeaponMetadata(BaseModel):
    weapon_name: str
    weapon_id: str
    image_url: str
    weapon_type: str
    weapon_tier: str
    weapon_rounds_type: str
    base_stat: List[WeaponStat]
    firearm_atk: List[FirearmAttackPower]
    weapon_perk_ability_name: Optional[str]
    weapon_perk_ability_description: Optional[str]

    class WeaponStat(BaseModel):
        stat_type: str
        stat_value: int

    class FirearmAttackPower(BaseModel):
        level: int
        firearm: List[FireArmAttackPowerDetail]

        class FireArmAttackPowerDetail(BaseModel):
            firearm_atk_type: str
            firearm_atk_value: int


class TFDMetadataEnchantDetail(BaseModel):
    enchant_level: int
    stat_type: str
    value: int


# module metadata
class TFDModuleMetadata(BaseModel):
    module_name: str
    module_id: str
    image_url: str
    module_type: Optional[str]
    module_tier: str
    module_socket_type: str
    module_class: str
    module_stat: List[ModuleStat]

    class ModuleStat(BaseModel):
        level: int
        module_capacity: int
        value: str


# reactor metadata
class TFDReactorMetadata(BaseModel):
    reactor_id: str
    reactor_name: str
    image_url: str
    reactor_tier: str
    reactor_skill_power: List[ReactorSkillPower]
    optimized_condition_type: str

    class ReactorSkillPower(BaseModel):
        level: int
        skill_atk_power: int
        sub_skill_atk_power: int
        skill_power_coefficient: List[ReactorSkillPowerCoefficient]
        enchant_effect: List[TFDMetadataEnchantDetail]

        class ReactorSkillPowerCoefficient(BaseModel):
            coefficient_stat_id: str
            coefficient_stat_value: int


# external component metadata
class TFDExternalComponentMetadata(BaseModel):
    external_component_id: str
    external_component_name: str
    image_url: str
    external_component_equipment_type: str
    external_component_tier: str
    base_stat: List[ExternalComponentBaseStat]
    set_option_detail: List[ExternalComponentSetOptionDetail]

    class ExternalComponentBaseStat(BaseModel):
        level: int
        stat_id: str
        stat_value: int

    class ExternalComponentSetOptionDetail(BaseModel):
        set_option: str
        set_count: int
        set_option_effect: str


# reward metadata
class TFDRewardMetadata(BaseModel):
    map_id: str
    map_name: str
    battle_zone: List[BattleZoneMetadata]

    class BattleZoneMetadata(BaseModel):
        battle_zone_id: str
        battle_zone_name: str
        reward: List[BattleZoneRewardMetadata]

        class BattleZoneRewardMetadata(BaseModel):
            rotation: int
            reward_type: str
            reactor_element_type: str
            weapon_rounds_type: str
            arche_type: str


# stat metadata
class TFDStatMetadata(BaseModel):
    stat_id: str
    stat_name: str


# void battle metadata
class TFDVoidBattleMetadata(BaseModel):
    void_battle_id: str
    void_battle_name: str


# title metadata
class TFDTitleMetadata(BaseModel):
    title_id: str
    title_name: str
