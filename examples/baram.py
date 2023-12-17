import asyncio
from nexon_openapi import NexonOpenAPI, NexonOpenAPIAsync

if __name__ == "__main__":
    # Sync
    client = NexonOpenAPI()

    ocid = client.baram.get_ocid(server_name="연", character_name="나비")
    character_basic = client.baram.get_character_basic(ocid=ocid)
    character_title = client.baram.get_character_title(ocid=ocid)
    character_title_equipment = client.baram.get_character_title_equipment(ocid=ocid)
    character_item_equipment = client.baram.get_character_item_equipment(ocid=ocid)
    character_stat = client.baram.get_character_stat(ocid=ocid)
    character_guild = client.baram.get_character_guild(ocid=ocid)

    # Async
    async def async_main():
        client = NexonOpenAPIAsync()

        ocid = await client.baram.get_ocid(server_name="연", character_name="나비")
        _character_basic = await client.baram.get_character_basic(ocid=ocid)
        _character_title = await client.baram.get_character_title(ocid=ocid)
        _character_title_equipment = await client.baram.get_character_title_equipment(ocid=ocid)
        _character_item_equipment = await client.baram.get_character_item_equipment(ocid=ocid)
        _character_stat = await client.baram.get_character_stat(ocid=ocid)
        _character_guild = await client.baram.get_character_guild(ocid=ocid)

    asyncio.run(async_main())
