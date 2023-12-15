from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ocid = client.v4.get_ocid(character_name="")
    character_basic = client.v4.get_character_basic(ocid=ocid)
    character_honor = client.v4.get_character_honor(ocid=ocid)
    character_honor_equipment = client.v4.get_character_honor_equipment(ocid=ocid)
