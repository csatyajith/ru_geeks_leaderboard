import json

import requests

from config import Config


class GithubRetriever:
    def __init__(self, participants, config):
        self.config = config
        self.participants = participants
        self.scores = {i: 0 for i in self.participants}

    def reset_scores(self):
        self.scores = {i: 0 for i in self.participants}

    def get_scores(self):
        self.reset_scores()
        for participant in self.participants:
            response = requests.get(self.config["api_call_uri"].format(participant, "master"))
            if response.status_code == 404:
                response = requests.get(self.config["api_call_uri"].format(participant, "main"))
            if response.status_code in [404, 409]:
                self.scores[participant] = -1
                continue
            files = json.loads(response.text)
            for f in files["tree"]:
                if "geeks_practice/" in f["path"] and ".py" in f["path"]:
                    self.scores[participant] += 1
        return self.scores


if __name__ == '__main__':
    conf = Config("config/local-config.json").get_config()
    g = GithubRetriever(conf["participants"], conf)
    print(g.get_scores())
