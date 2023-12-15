from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ocid = client.baramy.get_ocid(server_name="", character_name="")
    character_basic = client.baramy.get_character_basic(ocid=ocid)
    character_title = client.baramy.get_character_title(ocid=ocid)
    character_title_equipment = client.baramy.get_character_title_equipment(ocid=ocid)
