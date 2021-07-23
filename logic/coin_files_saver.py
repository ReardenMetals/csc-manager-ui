from enum import Enum

from app_tools.app_config import AppConfig
from app_tools.os_utils import copy_tmp_file


class FileKey(Enum):
    BASE_FILE_KEY = 'base_file_name'
    SNIP_FILE_KEY = 'asset_id_file_name'
    PRIVATE_FILE_KEY = 'private_file_name'
    LABELS_FILE_KEY = 'public_file_name'
    NUMBERS_FILE_KEY = 'sequence_file_name'
    RECOVERED_FILE_KEY = 'recovered_file_name'
    RECOVERED_KEYS_FILE_KEY = 'recovered_keys_file_name'


class CoinFilesSaver:

    def __init__(self, app_config: AppConfig):
        self.app_config = app_config

    def read_coins_list(self):
        return self.read_from_file_by_key(FileKey.BASE_FILE_KEY)

    def save_coins_list(self, lines):
        self.save_to_file_by_key(lines, FileKey.BASE_FILE_KEY)

    def read_asset_ids(self):
        return self.read_from_file_by_key(FileKey.SNIP_FILE_KEY)

    def save_asset_ids(self, lines):
        self.save_to_file_by_key(lines, FileKey.SNIP_FILE_KEY)

    def read_private_keys(self):
        return self.read_from_file_by_key(FileKey.PRIVATE_FILE_KEY)

    def save_private_keys(self, lines):
        self.save_to_file_by_key(lines, FileKey.PRIVATE_FILE_KEY)

    def read_public_keys(self):
        return self.read_from_file_by_key(FileKey.LABELS_FILE_KEY)

    def save_public_keys(self, lines):
        self.save_to_file_by_key(lines, FileKey.LABELS_FILE_KEY)

    def read_sequence_coin_id(self):
        return self.read_from_file_by_key(FileKey.NUMBERS_FILE_KEY)

    def save_sequence_coin_id(self, lines):
        self.save_to_file_by_key(lines, FileKey.NUMBERS_FILE_KEY)

    def save_recovered_labels(self, lines):
        self.save_to_file_by_key(lines, FileKey.RECOVERED_FILE_KEY)

    def save_recovered_keys(self, lines):
        self.save_to_file_by_key(lines, FileKey.RECOVERED_KEYS_FILE_KEY)

    def read_from_file_by_key(self, key: FileKey):
        return self.__read_from_file(self.app_config.get_property(key.value))

    def save_to_file_by_key(self, lines, key: FileKey):
        self.__save_to_file(lines, self.app_config.get_property(key.value))

    def copy_tmp_file_by_key(self, key: FileKey):
        copy_tmp_file(self.app_config.get_property(key.value))

    @staticmethod
    def __read_from_file(filename):
        with open(filename, 'r+') as file:
            lines = file.read().splitlines()
            file.close()
        return lines

    @staticmethod
    def __save_to_file(lines, filename):
        with open(filename, 'w') as file:
            file.writelines(lines)
            file.flush()
            file.close()
