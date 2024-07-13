import asyncio
from nexon_openapi import NexonOpenAPI, NexonOpenAPIAsync

if __name__ == "__main__":

    def main():
        client = NexonOpenAPI()

        ouid = client.tfd.get_ouid(user_name="")
        user_basic = client.tfd.get_user_basic(ouid=ouid.ouid)
        descendant = client.tfd.get_user_descendant(ouid=ouid.ouid)
        weapon = client.tfd.get_user_weapon(ouid=ouid.ouid)
        reactor = client.tfd.get_user_reactor(ouid=ouid.ouid)
        external_component = client.tfd.get_user_external_component(ouid=ouid.ouid)
        descendant_metadata = client.tfd.get_descendant_metadata()
        weapon_metadata = client.tfd.get_weapon_metadata()
        module_metadata = client.tfd.get_module_metadata()
        reactor_metadata = client.tfd.get_reactor_metadata()  # this is heavy (contains million rows)
        external_component_metadata = client.tfd.get_external_component_metadata()
        reward_metadata = client.tfd.get_reward_metadata()
        stat_metadata = client.tfd.get_stat_metadata()
        void_battle_metadata = client.tfd.get_void_battle_metadata()
        title_metadata = client.tfd.get_title_metadata()

    # main()

    # # Async
    async def async_main():
        client = NexonOpenAPIAsync()

        ouid = await client.tfd.get_ouid(user_name="란즈미#3630")
        user_basic = await client.tfd.get_user_basic(ouid=ouid.ouid)
        descendant = await client.tfd.get_user_descendant(ouid=ouid.ouid)
        weapon = await client.tfd.get_user_weapon(ouid=ouid.ouid)
        reactor = await client.tfd.get_user_reactor(ouid=ouid.ouid)
        external_component = await client.tfd.get_user_external_component(ouid=ouid.ouid)
        descendant_metadata = await client.tfd.get_descendant_metadata()
        weapon_metadata = await client.tfd.get_weapon_metadata()
        module_metadata = await client.tfd.get_module_metadata()
        reactor_metadata = await client.tfd.get_reactor_metadata()  # this is heavy (contains million rows)
        external_component_metadata = await client.tfd.get_external_component_metadata()
        reward_metadata = await client.tfd.get_reward_metadata()
        stat_metadata = await client.tfd.get_stat_metadata()
        void_battle_metadata = await client.tfd.get_void_battle_metadata()
        title_metadata = await client.tfd.get_title_metadata()

    asyncio.run(async_main())
