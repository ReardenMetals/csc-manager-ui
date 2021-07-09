from dependency_injector.wiring import Provide

import logic
from keygen.crypto_coin_factory import CoinFactory
from logic.recovery import RecoveryProcessor
import json

import sys
from di.containers import MyContainer


def default_input(message, default_val):
    if default_val:
        return input("%s [%s] : " % (message, default_val)) or default_val
    else:
        return input("%s " % message)


def main(coin_factory: CoinFactory = Provide['coin_factory']):
    private_keys = load_private_keys()
    recovery_processor = RecoveryProcessor()
    coin_currency = default_input("What crypto you making (BTC, ETH, ...)? ", "BTC").upper()
    service = coin_factory.get_coin_service(coin_currency)

    coins = [service.get_coin(private_key) for private_key in private_keys]
    coin_tuples = [(coin, service.generate_asset_id(coin)) for coin in coins]
    recovery_processor.save_recovered_coins(coin_tuples)


def load_private_keys():
    with open('config.json') as json_file:
        config_json = json.load(json_file)
        private_file_name = config_json['private_file_name']
    with open(private_file_name, 'r') as file:
        private_keys = file.read().splitlines()
        return private_keys


if __name__ == "__main__":
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]], packages=[logic])
    main()
