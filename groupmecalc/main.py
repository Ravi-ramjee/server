import requests
# from BaseHTTPServer import


SEND = "https://api.groupme.com/v3/bots/post"
RECV = "https://friedchicken.mynetgear.com"
BOT_ID = "f87bbd9f6df8ce5e1cc15e677a"


data = {
    "bot_id": BOT_ID,
    "text": "this is an automated post",
}

requests.post(SEND, data)




