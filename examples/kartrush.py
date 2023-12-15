from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ouid = client.kartrush.get_ouid(racer_name="").ouid_info[0].ouid
    user_basic = client.kartrush.get_user_basic(ouid=ouid)
    user_title_equipment = client.kartrush.get_user_title_equipment(ouid=ouid)
