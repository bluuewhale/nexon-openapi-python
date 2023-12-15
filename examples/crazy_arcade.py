from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ouid = client.crazy_arcade.get_ouid(user_name="", world_name="해피")
    user_basic = client.crazy_arcade.get_user_basic(ouid=ouid)
    user_title = client.crazy_arcade.get_user_title(ouid=ouid)
    user_title_equipment = client.crazy_arcade.get_user_title_equipment(ouid=ouid)
    print(user_title_equipment)
