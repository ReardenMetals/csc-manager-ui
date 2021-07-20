
class ConfigLoader:

    def __init__(self, config) -> None:
        super().__init__()
        self.__config = config

    def get_general(self, key: str):
        return self.__config['general'][key.lower()]

    def get_coin_checker(self, key: str):
        return self.__config['coin_checker'][key.lower()]

    def get_recovery_scanner(self, key: str):
        return self.__config['recovery_scanner'][key.lower()]

    def get_barcode_scanner(self, key: str):
        return self.__config['barcode_scanner'][key.lower()]