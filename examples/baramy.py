import asyncio
from nexon_openapi import NexonOpenAPI, NexonOpenAPIAsync

if __name__ == "__main__":
    # Sync
    client = NexonOpenAPI()

    ocid = client.baramy.get_ocid(server_name="", character_name="")
    character_basic = client.baramy.get_character_basic(ocid=ocid)
    character_title = client.baramy.get_character_title(ocid=ocid)
    character_title_equipment = client.baramy.get_character_title_equipment(ocid=ocid)

    # Async
    async def async_main():
        client = NexonOpenAPIAsync()

        ocid = await client.baram.get_ocid(server_name="", character_name="")
        _character_basic = client.baramy.get_character_basic(ocid=ocid)
        _character_title = client.baramy.get_character_title(ocid=ocid)
        _character_title_equipment = client.baramy.get_character_title_equipment(ocid=ocid)

    asyncio.run(async_main())
