from groupmebot import GroupMeBot, API_URL
from flask import Flask, request


class ReplBot (GroupMeBot):
    commandPrefix = "."
    authPrefix = "$"

    def __init__(self, id, ownerId, postTo=API_URL):
        super(self.__class__, self).__init__(id, postTo)
        self.ownerId = ownerId
        self.commands = []

    def onPost(self, msg):
        text = msg["text"]
        senderId = msg["sender_id"]

        for line in text.split("\n"):
            if line.startswith(self.commandPrefix):
                self.handleCommand(line[len(self.commandPrefix):], senderId)
            elif line.startswith(self.authPrefix) and senderId == self.ownerId:
                self.handleAuth(line[len(self.authPrefix):])

    def handleCommand(self, cmd, senderId):
        if senderId == self.ownerId:
            print(cmd)
            try:
                exec(cmd)
                globals().update(locals())
            except:
                self.print("Error")
        else:
            self.commands.append((cmd, senderId))

    def handleAuth(self, cmd):
        if cmd:
            for char in cmd:
                if not self.commands:
                    break
                if char in "Yy":
                    self.handleCommand(self.commands[0], self.ownerId)
                self.commands = self.commands[1:]
        else:
            while self.commands:
                self.handleCommand(self.commands[0], self.ownerId)
                self.commands = self.commands[1:]




bot = ReplBot("f87bbd9f6df8ce5e1cc15e677a", "33065426")
app = Flask(__name__)


@app.route("/", methods=["POST"])
def onPost():
    bot.onPost(request.json)
    return "received"


app.run("0.0.0.0", port=54003)



