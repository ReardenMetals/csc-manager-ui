import logging

from logic.coin_files_saver import CoinFilesSaver, FileKey


class UpdateProcessor:
    __file_keys = [
        FileKey.BASE_FILE_KEY,
        FileKey.SNIP_FILE_KEY,
        FileKey.PRIVATE_FILE_KEY,
        FileKey.LABELS_FILE_KEY,
        FileKey.NUMBERS_FILE_KEY,
    ]

    __allow_copy = False

    def __init__(self, coin_file_saver: CoinFilesSaver):
        super().__init__()
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.coin_file_saver = coin_file_saver

    def update(self, last_good_coin):

        good_coin_pos = self.__get_coin_position(last_good_coin)
        self.logger.info("Last good coin position: " + str(good_coin_pos))

        for file_key in self.__file_keys:
            if self.__allow_copy:
                self.coin_file_saver.copy_tmp_file_by_key(file_key)
            else:
                self.logger.warning("File backup inactive!")
            self.__remove_lines_in_file(file_key, good_coin_pos)

        self.logger.info("Successfully updated!")

    def __get_coin_position(self, good_coin):
        self.logger.debug("Searching last good coin position")
        coin_list_id = self.coin_file_saver.read_sequence_coin_id()
        good_coin_pos = coin_list_id.index(good_coin)
        return good_coin_pos

    def __remove_lines_in_file(self, file_key: FileKey, good_coin_pos):
        self.logger.debug("Removing lines in file: %s", file_key.value)
        coin_list = [x + '\n' for x in self.coin_file_saver.read_from_file_by_key(file_key)]

        for i in range(good_coin_pos + 1):
            if file_key != FileKey.BASE_FILE_KEY:
                coin_list.pop(0)
            else:
                coin_list.pop(1)

        self.coin_file_saver.save_to_file_by_key(coin_list, file_key)
