from flask import Flask, request
import requests
import google as g


URL = "https://api.groupme.com/v3/bots/post"
BOT_NAME = "Marvin"
BOT_ID = "f87bbd9f6df8ce5e1cc15e677a"

ME = "33065426"
PREFIX = "."


def gprint(x):
    requests.post(URL, {"bot_id": BOT_ID, "text": str(x)})


"""
def ginput():
    getInput = True
"""


def execCommand(cmd):
    try:
        exec(cmd)
        globals().update(locals())
    except:
        gprint("Error")



def google(query, limit=2):
    i = 0
    for url in g.search(query):
        gprint(url)
        if i >= limit - 1:
            break
        i += 1


def googleImage(query, limit=2):
    i = 0
    for url in g.search_images(query):
        gprint(url)
        if i >= limit - 1:
            break
        i += 1


def help():
    pass


app = Flask(__name__)
commands = []
# manatees = g.search_images("manatee")


@app.route("/", methods=["POST"])
def result():
    global commands

    data = request.json
    text = data["text"]

    if commands and data["sender_id"] == ME:
        if text[0] == "%":
            text = text[1:]

            if not text:
                while commands:
                    execCommand(commands[0])
                    commands = commands[1:]

            for char in text:
                if not commands:
                    break
                if char in "Yy":
                    execCommand(commands[0])
                commands = commands[1:]
            return "received"

    lines = text.split("\n")

    for line in lines:
        if line and line.startswith(PREFIX):
            print(data["name"] + ", " + data["sender_id"] + ": " + line)

            line = line[len(PREFIX):]

            if data["sender_id"] == ME:
                execCommand(line)
            else:
                commands.append(line)
    return "received"

app.run(host="0.0.0.0", port=54003)
