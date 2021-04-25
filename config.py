import json


class Config:
    def __init__(self, config_path):
        with open(config_path) as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

