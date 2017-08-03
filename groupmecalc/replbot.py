from groupmebot import GroupMeBot, API_URL


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


if __name__ == "__main__":
    import sys
    from flask import Flask, request
    import google as g


    if len(sys.argv) > 1:
        botId, ownerId, port = sys.argv[1:]
        bot = ReplBot(sys.argv[1], sys.argv[2])

        if len(sys.argv) >= 4:
            bot.commandPrefix = sys.argv[3]
        if len(sys.argv) >= 5:
            bot.authPrefix = sys.argv[4]
    else:
        port = 54000
        bot = ReplBot("f87bbd9f6df8ce5e1cc15e677a", "33065426") # marvin
        #bot = ReplBot("524c2fe2165cd94a7a8f35f5b5", "33065426") # frank
    gprint = bot.print


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


    @app.route("/", methods=["POST"])
    def onPost():
        bot.onPost(request.json)
        return "received"


    app.run("0.0.0.0", port=int(port))
