from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ocid = client.hit2.get_ocid(character_name="")
    character_basic = client.hit2.get_character_basic(ocid=ocid)
