"""Containers module."""

import logging.config

from dependency_injector import containers, providers
from app_tools.my_video_capture import MyVideoCapture
from crypto_coin_factory import CoinFactoryExtended


class MyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.fileConfig,
        fname='logging.ini',
    )

    default_video_capture = providers.Singleton(MyVideoCapture)

    coin_factory = providers.Singleton(CoinFactoryExtended)

