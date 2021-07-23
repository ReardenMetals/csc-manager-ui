from dependency_injector.wiring import Provide

import logic
from keygen.crypto_coin_factory import CoinFactory
from logic.coin_files_saver import CoinFilesSaver
from logic.recovery import RecoveryProcessor

import sys
from di.containers import MyContainer


def default_input(message, default_val):
    if default_val:
        return input("%s [%s] : " % (message, default_val)) or default_val
    else:
        return input("%s " % message)


def main(coin_factory: CoinFactory = Provide['coin_factory'],
         recovery_processor: RecoveryProcessor = Provide['recovery_processor'],
         coin_files_saver: CoinFilesSaver = Provide['coin_files_saver']):
    private_keys = coin_files_saver.read_private_keys()
    coin_currency = default_input("What crypto you making (BTC, ETH, ...)? ", "BTC").upper()
    service = coin_factory.get_coin_service(coin_currency)

    coins = [service.get_coin(private_key) for private_key in private_keys]
    coin_tuples = [(coin, service.generate_asset_id(coin)) for coin in coins]
    recovery_processor.save_recovered_coins(coin_tuples)


if __name__ == "__main__":
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]], packages=[logic])
    main()
