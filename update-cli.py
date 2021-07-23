from dependency_injector.wiring import Provide

from logic.update import UpdateProcessor

import sys
from di.containers import MyContainer
import logic


def main(update_processor: UpdateProcessor = Provide['update_processor']):
    good_coin = input("Enter the last good coin id : ")
    update_processor.update(good_coin)


if __name__ == "__main__":
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]], packages=[logic])
    main()
