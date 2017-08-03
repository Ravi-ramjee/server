import copy
import requests


API_URL = "https://api.groupme.com/v3/bots/post"
CHAR_LIMIT = 1000


class GroupMeBot (object):
    def __init__(self, id, postTo=API_URL):
        self.id = id
        self.postTo = postTo

    def post(self, msg):
        msg1 = copy.deepcopy(msg)
        msg1.update({"bot_id": self.id})
        requests.post(self.postTo, msg1)

    def print(self, text):
        text = str(text)
        while text:
            if len(text) >= CHAR_LIMIT:
                head = text[:CHAR_LIMIT]
                self.post({"text": head})
                text = text[CHAR_LIMIT:]
            else:
                self.post({"text": text})
                break


    def onPost(self, msg):
        pass
