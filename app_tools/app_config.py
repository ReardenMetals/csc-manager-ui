import json


class AppConfig:

    def __init__(self):
        with open('config.json') as json_file:
            self.__config_json = json.load(json_file)

    def get_property(self, key: str):
        return self.__config_json[key]
