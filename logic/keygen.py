import json

import logging

from keygen.crypto_coin_factory import CoinFactory


class KeygenProcessor:

    def __init__(self, coin_factory: CoinFactory):
        super().__init__()
        self.coin_factory = coin_factory
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    def generate_keys(self, count, coin, laser):
        with open('config.json') as json_file:
            config_json = json.load(json_file)
            base_file_name = config_json['base_file_name']
            asset_id_file_name = config_json['asset_id_file_name']
            private_file_name = config_json['private_file_name']
            public_file_name = config_json['public_file_name']
            sequence_file_name = config_json['sequence_file_name']

        max_iterator_count = int(count)

        try:
            crypto_keygen_service = self.coin_factory.get_coin_service(coin)

            if max_iterator_count > 0:
                coin_list = crypto_keygen_service.generate_list(max_iterator_count)
                self.__save_coins_list(crypto_keygen_service, coin_list, base_file_name)
                self.__save_asset_ids(crypto_keygen_service, coin_list, asset_id_file_name)
                self.__save_private_keys(crypto_keygen_service, coin_list, private_file_name)
                self.__save_public_keys(crypto_keygen_service, coin_list, public_file_name)
                self.__save_sequence_coin_id(laser, coin_list, sequence_file_name)
            else:
                self.logger.info("Iterator count should be > 0")
        except Exception as e:
            self.logger.error(e)

    def __save_coins_list(self, crypto_keygen_service, coin_list=[], filename='address.csv'):
        with open(filename, 'w') as file:
            file.write(crypto_keygen_service.get_csv_header())
            for coin in coin_list:
                line = crypto_keygen_service.format(coin)
                self.logger.info("Address.csv {}/{}".format(coin_list.index(coin), len(coin_list)))
                file.write(line)
            file.flush()
            file.close()
            self.logger.info("Done!")

    def __save_asset_ids(self, crypto_keygen_service, coin_list=[], filename='assetid.txt'):
        with open(filename, 'w') as file:
            for coin in coin_list:
                asset = crypto_keygen_service.generate_asset_id(coin)
                line = "{}\n".format(asset)
                file.write(line)
                self.logger.info("Asset IDs {}/{}".format(coin_list.index(coin), len(coin_list)))
            file.flush()
            file.close()
            self.logger.info("Done!")

    def __save_private_keys(self, crypto_keygen_service, coin_list=[], filename='private.txt'):
        with open(filename, 'w') as file:
            for coin in coin_list:
                line = "{}\n".format(coin.wif)
                file.write(line)
                self.logger.info("PrivateKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
            file.flush()
            file.close()
            self.logger.info("Done!")

    def __save_public_keys(self, crypto_keygen_service, coin_list=[], filename='public.txt'):
        with open(filename, 'w') as file:
            for coin in coin_list:
                line = "{},{}\n".format(coin.address, crypto_keygen_service.generate_asset_id(coin))
                file.write(line)
                self.logger.info("PublicKeys {}/{}".format(coin_list.index(coin), len(coin_list)))
            file.flush()
            file.close()
            self.logger.info("Done!")

    def __save_sequence_coin_id(self, lazer_type, coin_list=[], filename='sequence.txt'):
        with open(filename, 'w') as file:
            for coin_item in coin_list:
                line = "{}{}\n".format(lazer_type, coin_list.index(coin_item).__format__('04'))
                file.write(line)
                self.logger.info("CoinId Laser Type {}, Number {}".format(lazer_type, coin_list.index(coin_item).__format__('04')))
            file.flush()
            file.close()
            self.logger.info("Done!")
