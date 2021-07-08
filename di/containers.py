"""Containers module."""

import logging.config

from dependency_injector import containers, providers
from app_tools.my_video_capture import MyVideoCapture
# from app_tools.qr.dynamsoft_qr_code_scaner import DynamsoftQrCodeScanner
from app_tools.qr.zbar_qr_code_scaner import ZbarQrCodeScanner
from crypto_coin_factory import CoinFactoryExtended
from keygen.crypto_coin_factory import CoinFactory


class MyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.fileConfig,
        fname='logging.ini',
    )

    default_video_capture = providers.Singleton(MyVideoCapture)

    # coin_factory = providers.Singleton(CoinFactory)
    coin_factory = providers.Singleton(CoinFactoryExtended)

    # qr_code_scanner = providers.Singleton(DynamsoftQrCodeScanner, config.dynamo_soft.license_key)
    qr_code_scanner = providers.Singleton(ZbarQrCodeScanner)

