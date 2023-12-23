import asyncio
from nexon_openapi import NexonOpenAPI, NexonOpenAPIAsync

if __name__ == "__main__":
    client = NexonOpenAPI()

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

    # Async
    async def async_main():
        client = NexonOpenAPIAsync()

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
        print(character_dojang)

    asyncio.run(async_main())
