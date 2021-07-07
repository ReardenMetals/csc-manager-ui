import json
import os
import logging


class UpdateProcessor:

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    def update(self, last_good_coin):
        with open('config.json') as json_file:
            config_json = json.load(json_file)

            config_files = [
                config_json['sequence_file_name'],
                config_json['base_file_name'],
                config_json['asset_id_file_name'],
                config_json['private_file_name'],
                config_json['public_file_name']
            ]
            self.logger.info("Loaded config files")
            self.logger.info(config_files)

        good_coin_pos = self.__get_coin_position(config_files[0], last_good_coin)
        self.logger.info("good_coin_pos: " + str(good_coin_pos))

        for file_name in config_files:
            self.__copy_file(file_name)
            self.__remove_lines_in_file(file_name, good_coin_pos)

        self.logger.info("Successfully updated!")

    # saving for backup
    def __copy_file(self, old_file):
        # new_file = old_file + "tmp"
        # shutil.copy(old_file, new_file)
        # print("Make copy {}. Done!".format(new_file))
        self.logger.warning("__copy_file inactive")
        pass

    def __get_coin_position(self, filename, good_coin):
        self.logger.debug("get_coin_position")
        with open(filename, 'r') as file:
            coin_list_id = file.read().splitlines()
            coin_id = coin_list_id.index(good_coin)
            file.close()
        return coin_id

    def __remove_lines_in_file(self, filename, good_coin_pos):
        self.logger.debug("remove_lines_in_file")
        with open(filename, 'r+') as file:
            coin_list = file.read().splitlines()
        file.close()
        for i in range(good_coin_pos + 1):
            if os.path.basename(filename) != "address.csv":
                coin_list.pop(0)
            else:
                coin_list.pop(1)
        with open(filename, 'w') as file:
            for item in coin_list:
                line = "{}\n".format(item)
                file.write(line)
        file.close()
