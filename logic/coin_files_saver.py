import json


class CoinFilesSaver:

    def __init__(self):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            self.base_file_name = config_json['base_file_name']
            self.asset_id_file_name = config_json['asset_id_file_name']
            self.private_file_name = config_json['private_file_name']
            self.public_file_name = config_json['public_file_name']
            self.sequence_file_name = config_json['sequence_file_name']
            self.recovered_file_name = config_json['recovered_file_name']
            self.recovered_keys_file_name = config_json['recovered_keys_file_name']

    def save_coins_list(self, lines):
        self.__save_to_file(lines, self.base_file_name)

    def save_asset_ids(self, lines):
        self.__save_to_file(lines, self.asset_id_file_name)

    def save_private_keys(self, lines):
        self.__save_to_file(lines, self.private_file_name)

    def save_public_keys(self, lines):
        self.__save_to_file(lines, self.public_file_name)

    def save_sequence_coin_id(self, lines):
        self.__save_to_file(lines, self.sequence_file_name)

    def save_recovered_labels(self, lines):
        self.__save_to_file(lines, self.recovered_file_name)

    def save_recovered_keys(self, lines):
        self.__save_to_file(lines, self.recovered_keys_file_name)

    @staticmethod
    def __save_to_file(lines, filename):
        with open(filename, 'w') as file:
            file.writelines(lines)
            file.flush()
            file.close()
