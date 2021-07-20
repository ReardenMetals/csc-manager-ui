import logging

from logic.coin_files_saver import CoinFilesSaver


class RecoveryProcessor:

    def __init__(self, coin_file_saver=CoinFilesSaver()):
        super().__init__()
        self.coin_file_saver = coin_file_saver
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    # coin = tuple of (coin,asset_id)
    def save_recovered_coins(self, coins):
        self.logger.info("Saving recovered public keys & asset IDs to file...\n")
        self.__save_public_keys(coins)
        self.logger.info("Recovered public keys & asset IDs saved to file!\n")

        self.logger.info("Saving recovered private keys to file...\n")
        self.__save_private_keys(coins)
        self.logger.info("Recovered private keys saved to file!\n")


    # coin = tuple of (coin,asset_id)
    def __save_public_keys(self, coins):
        lines = []
        for coin in coins:
            line = "{},{}".format(coin[0].address, coin[1])
            lines.append("{}\n".format(line))
            self.logger.info(line)
            self.logger.info("Recovered public keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))
        self.coin_file_saver.save_recovered_labels(lines)

    # coin = tuple of (coin,asset_id)
    def __save_private_keys(self, coins):
        lines = []
        for coin in coins:
            line = "{}".format(coin[0].wif)
            lines.append("{}\n".format(line))
            self.logger.info(line)
            self.logger.info("Recovered private keys {}/{}\n".format(coins.index(coin) + 1, len(coins)))
        self.coin_file_saver.save_recovered_keys(lines)
