from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ocid = client.mabinogi_heroes.get_ocid(character_name="")

    character_basic = client.mabinogi_heroes.get_character_basic(ocid=ocid)
    character_title = client.mabinogi_heroes.get_character_title(ocid=ocid)
    character_title_equipment = client.mabinogi_heroes.get_character_title_equipment(ocid=ocid)
    character_item_equipment = client.mabinogi_heroes.get_character_item_equipment(ocid=ocid)
    character_stat = client.mabinogi_heroes.get_character_stat(ocid=ocid)
    character_guild = client.mabinogi_heroes.get_character_guild(ocid=ocid)
    print(character_guild)
