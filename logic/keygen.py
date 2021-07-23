import logging

from keygen.crypto_coin_factory import CoinFactory
from logic.coin_files_saver import CoinFilesSaver


class KeygenProcessor:

    def __init__(self, coin_factory: CoinFactory, coin_file_saver: CoinFilesSaver):
        super().__init__()
        self.coin_factory = coin_factory
        self.coin_file_saver = coin_file_saver
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    def generate_keys(self, count, coin, laser):

        max_iterator_count = int(count)

        try:
            crypto_keygen_service = self.coin_factory.get_coin_service(coin)

            if max_iterator_count > 0:
                coin_list = crypto_keygen_service.generate_list(max_iterator_count)
                self.__save_coins_list(crypto_keygen_service, coin_list)
                self.__save_asset_ids(crypto_keygen_service, coin_list)
                self.__save_private_keys(coin_list)
                self.__save_public_keys(crypto_keygen_service, coin_list)
                self.__save_sequence_coin_id(laser, coin_list)
            else:
                self.logger.info("Iterator count should be > 0")
        except Exception as e:
            self.logger.error("Error keys generating!")
            self.logger.error(e)

    def __save_coins_list(self, crypto_keygen_service, coin_list=[]):
        lines = [crypto_keygen_service.get_csv_header()]
        for coin in coin_list:
            line = crypto_keygen_service.format(coin)
            self.logger.info("Address.csv: {}/{}".format(coin_list.index(coin), len(coin_list)))
            lines.append(line)
        self.coin_file_saver.save_coins_list(lines)
        self.logger.info("Coins List (CSV): Done!")

    def __save_asset_ids(self, crypto_keygen_service, coin_list=[]):
        lines = []
        for coin in coin_list:
            asset = crypto_keygen_service.generate_asset_id(coin)
            line = "{}\n".format(asset)
            self.logger.info("Asset IDs {}/{}".format(coin_list.index(coin), len(coin_list)))
            lines.append(line)
        self.coin_file_saver.save_asset_ids(lines)
        self.logger.info("Snips Done!")

    def __save_private_keys(self, coin_list=[]):
        lines = []
        for coin in coin_list:
            line = "{}\n".format(coin.wif)
            self.logger.info("PrivateKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
            lines.append(line)
        self.coin_file_saver.save_private_keys(lines)
        self.logger.info("Private keys: Done!")

    def __save_public_keys(self, crypto_keygen_service, coin_list=[]):
        lines = []
        for coin in coin_list:
            line = "{},{}\n".format(coin.address, crypto_keygen_service.generate_asset_id(coin))
            self.logger.info("PublicKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
            lines.append(line)
        self.coin_file_saver.save_public_keys(lines)
        self.logger.info("Public keys: Done!")

    def __save_sequence_coin_id(self, lazer_type, coin_list=[]):
        lines = []
        for coin_item in coin_list:
            line = "{}{}\n".format(lazer_type, coin_list.index(coin_item).__format__('04'))
            self.logger.info(
                "CoinId Laser Type {}, Number {}".format(lazer_type, coin_list.index(coin_item).__format__('04')))
            lines.append(line)
        self.coin_file_saver.save_sequence_coin_id(lines)
        self.logger.info("Numbers: Done!")
