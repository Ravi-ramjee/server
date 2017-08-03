from flask import Flask, request
import requests  # different from the flask request, this just lets u post to the bot link


# groupme api's link for bots to talk to
POST_URL = "https://api.groupme.com/v3/bots/post"
BOT_NAME = "Marvin"
# can be found in the bot's info
BOT_ID = "f87bbd9f6df8ce5e1cc15e677a"
PORT = 54003


app = Flask(__name__)

@app.route("/", methods=["POST"])
def result():
    data = request.json

    # make sure that the bot doesn't echo itself
    if data["name"] != BOT_NAME:
        # tell the groupme api to post a message to the group with your bot
        requests.post(POST_URL, {"bot_id": BOT_ID, "text": data["text"]})
        # you could return any kind of string from here, it just tells
        # the app it got the data

    return "received"

app.run(host="0.0.0.0", port=PORT)
