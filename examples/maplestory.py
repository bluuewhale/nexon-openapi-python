import asyncio
from devtools import debug
from nexon_openapi import NexonOpenAPI, NexonOpenAPIAsync

if __name__ == "__main__":
    client = NexonOpenAPI()

    # 캐릭터 정보 조회
    ocid = client.maplestory.get_ocid(character_name="")
    character_basic = client.maplestory.get_character_basic(ocid=ocid)
    character_popularity = client.maplestory.get_character_popularity(ocid=ocid)
    character_stat = client.maplestory.get_character_stat(ocid=ocid)
    character_hyper_stat = client.maplestory.get_character_hyper_stat(ocid=ocid)
    character_propensity = client.maplestory.get_character_propensity(ocid=ocid)
    character_ability = client.maplestory.get_character_ability(ocid=ocid)
    character_item_equipment = client.maplestory.get_character_item_equipment(ocid=ocid)
    character_cash_item_equipment = client.maplestory.get_character_cash_item_equipment(ocid=ocid)
    character_symbol_equipment = client.maplestory.get_character_symbol_equipment(ocid=ocid)
    character_set_effect = client.maplestory.get_character_set_effect(ocid=ocid)
    character_beauty_equipment = client.maplestory.get_character_beauty_equipment(ocid=ocid)
    character_android_equipment = client.maplestory.get_character_android_equipment(ocid=ocid)
    character_pet_equipment = client.maplestory.get_character_pet_equipment(ocid=ocid)
    character_skill = client.maplestory.get_character_skill(ocid=ocid, character_skill_grade="5")
    character_link_skill = client.maplestory.get_character_link_skill(ocid=ocid)
    character_vmatrix = client.maplestory.get_character_vmatrix(ocid=ocid)
    character_hexa_matrix = client.maplestory.get_character_hexa_matrix(ocid=ocid)
    character_hexa_matrix_stat = client.maplestory.get_character_hexa_matrix_stat(ocid=ocid)
    character_dojang = client.maplestory.get_character_dojang(ocid=ocid)

    # # 유니온 정보 조회
    user_union = client.maplestory.get_user_union(ocid=ocid)
    user_union_raider = client.maplestory.get_user_union_raider(ocid=ocid)
    user_union_artifact = client.maplestory.get_user_union_artifact(ocid=ocid)

    # # 길드 정보 조회
    guild_id = client.maplestory.get_guild_id(world_name="", guild_name="")
    guild_basic = client.maplestory.get_guild_basic(guild_id=guild_id)

    # # 랭킹 정보 조회
    overall_ranking = client.maplestory.get_overall_ranking()
    union_ranking = client.maplestory.get_union_ranking()
    guild_ranking = client.maplestory.get_guild_ranking(ranking_type="0")
    dojang_ranking = client.maplestory.get_dojang_ranking(difficulty="1")
    the_seed_ranking = client.maplestory.get_the_seed_ranking()
    achievement_ranking = client.maplestory.get_achievement_ranking()

    # # 확률 정보 조회
    startforce_history = client.maplestory.get_starforce_history(count=10)

    # # Async
    async def async_main():
        client = NexonOpenAPIAsync()

        # 캐릭터 정보 조회
        ocid = await client.maplestory.get_ocid(character_name="")
        character_basic = await client.maplestory.get_character_basic(ocid=ocid)
        character_popularity = await client.maplestory.get_character_popularity(ocid=ocid)
        character_stat = await client.maplestory.get_character_stat(ocid=ocid)
        character_hyper_stat = await client.maplestory.get_character_hyper_stat(ocid=ocid)
        character_propensity = await client.maplestory.get_character_propensity(ocid=ocid)
        character_ability = await client.maplestory.get_character_ability(ocid=ocid)
        character_item_equipment = await client.maplestory.get_character_item_equipment(ocid=ocid)
        character_cash_item_equipment = await client.maplestory.get_character_cash_item_equipment(ocid=ocid)
        character_symbol_equipment = await client.maplestory.get_character_symbol_equipment(ocid=ocid)
        character_set_effect = await client.maplestory.get_character_set_effect(ocid=ocid)
        character_beauty_equipment = await client.maplestory.get_character_beauty_equipment(ocid=ocid)
        character_android_equipment = await client.maplestory.get_character_android_equipment(ocid=ocid)
        character_pet_equipment = await client.maplestory.get_character_pet_equipment(ocid=ocid)
        character_skill = await client.maplestory.get_character_skill(ocid=ocid, character_skill_grade="5")
        character_link_skill = await client.maplestory.get_character_link_skill(ocid=ocid)
        character_vmatrix = await client.maplestory.get_character_vmatrix(ocid=ocid)
        character_hexa_matrix = await client.maplestory.get_character_hexa_matrix(ocid=ocid)
        character_hexa_matrix_stat = await client.maplestory.get_character_hexa_matrix_stat(ocid=ocid)
        character_dojang = await client.maplestory.get_character_dojang(ocid=ocid)

        # 유니온 정보 조회
        user_union = await client.maplestory.get_user_union(ocid=ocid)
        user_union_raider = await client.maplestory.get_user_union_raider(ocid=ocid)
        user_union_artifact = await client.maplestory.get_user_union_artifact(ocid=ocid)

        # 길드 정보 조회
        guild_id = await client.maplestory.get_guild_id(world_name="", guild_name="")
        guild_basic = await client.maplestory.get_guild_basic(guild_id=guild_id)

        # 랭킹 정보 조회
        overall_ranking = await client.maplestory.get_overall_ranking()
        union_ranking = await client.maplestory.get_union_ranking()
        guild_ranking = await client.maplestory.get_guild_ranking(ranking_type="0")
        dojang_ranking = await client.maplestory.get_dojang_ranking(difficulty="1")
        the_seed_ranking = await client.maplestory.get_the_seed_ranking()
        achievement_ranking = await client.maplestory.get_achievement_ranking()

        # 확률 정보 조회
        startforce_history = await client.maplestory.get_starforce_history(count=10)

    asyncio.run(async_main())
