from nexon_openapi import NexonOpenAPI

if __name__ == "__main__":
    client = NexonOpenAPI()

    ouid = client.fc_online.get_ouid(nickname="")
    user_basic = client.fc_online.get_user_basic(ouid=ouid)
    user_max_division = client.fc_online.get_user_max_division(ouid=ouid)
    user_match_history = client.fc_online.get_user_match_history(ouid=ouid, matchtype=50)
    user_trade_history = client.fc_online.get_user_trade_history(ouid=ouid, tradetype="buy")
