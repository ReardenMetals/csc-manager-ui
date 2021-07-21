from dependency_injector.wiring import Provide

from logic.keygen import KeygenProcessor

import sys
from di.containers import MyContainer
import logic


def default_input(message, defaultVal):
    if defaultVal:
        return input("%s [%s] : " % (message, defaultVal)) or defaultVal
    else:
        return input("%s " % message)


def init(keygen: KeygenProcessor = Provide['keygen_processor']):
    max_iterator_count = int(default_input("How many codes you want? ", "10"))
    coin = default_input("What crypto you making (BTC, ETH, ...)? ", "BTC").upper()
    laser_type = default_input("What laser is this (A, B, C)? ", "A").upper()
    keygen.generate_keys(count=max_iterator_count, coin=coin, laser=laser_type)


if __name__ == "__main__":
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]], packages=[logic])
    init()
