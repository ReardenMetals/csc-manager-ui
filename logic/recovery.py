import json
import logging


class RecoveryProcessor:

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    # coin = tuple of (coin,asset_id)
    def save_recovered_coins(self, coins):
        recovered_file_name, recovered_keys_file_name = self.__load_file_config()

        self.logger.info("Saving recovered public keys & asset IDs to file...\n")
        with open(recovered_file_name, 'w') as recovered_file:
            self.__save_public_keys(coins, recovered_file)
            recovered_file.flush()
            recovered_file.close()
            self.logger.info("Recovered public keys & asset IDs saved to file!\n")

        self.logger.info("Saving recovered private keys to file...\n")
        with open(recovered_keys_file_name, 'w') as recovered_keys_file:
            self.__save_private_keys(coins, recovered_keys_file)
            recovered_keys_file.flush()
            recovered_keys_file.close()
            self.logger.info("Recovered private keys saved to file!\n")

    def __load_file_config(self):
        try:
            with open('config.json') as json_file:
                config_json = json.load(json_file)
                recovered_file_name = config_json['recovered_file_name']
                recovered_keys_file_name = config_json['recovered_keys_file_name']
                return recovered_file_name, recovered_keys_file_name
        except Exception as e:
            self.logger.info(e)

    # coin = tuple of (coin,asset_id)
    def __save_public_keys(self, coins, file):
        for coin in coins:
            line = "{},{}".format(coin[0].address, coin[1])
            file.write("{}\n".format(line))
            self.logger.info(line)
            self.logger.info("Recovered public keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))

    # coin = tuple of (coin,asset_id)
    def __save_private_keys(self, coins, file):
        for coin in coins:
            line = "{}".format(coin[0].wif)
            file.write("{}\n".format(line))
            self.logger.info(line)
            self.logger.info("Recovered private keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))
