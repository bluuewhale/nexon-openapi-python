from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ocid = client.maplestorym.get_ocid(world_name="", character_name="")
    character_basic = client.maplestorym.get_character_basic(ocid=ocid)
    character_item_equipment = client.maplestorym.get_character_item_equipment(ocid=ocid)
    character_stat = client.maplestorym.get_character_stat(ocid=ocid)
    character_guild = client.maplestorym.get_character_guild(ocid=ocid)
