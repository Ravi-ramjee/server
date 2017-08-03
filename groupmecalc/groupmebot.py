import copy
import requests


API_URL = "https://api.groupme.com/v3/bots/post"


class GroupMeBot (object):
    def __init__(self, id, postTo=API_URL):
        self.id = id
        self.postTo = postTo

    def post(self, msg):
        msg1 = copy.deepcopy(msg)
        msg1.update({"bot_id": self.id})
        requests.post(self.postTo, msg1)

    def print(self, text):
        self.post({"text": str(text)})

    def onPost(self, msg):
        pass
