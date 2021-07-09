
class ConfigLoader:

    def __init__(self, config) -> None:
        super().__init__()
        self.__config = config

    def get_general(self, key: str):
        return self.__config['general'][key]
