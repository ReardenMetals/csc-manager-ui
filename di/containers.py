"""Containers module."""

import logging.config

from dependency_injector import containers, providers

from app_tools.app_config import AppConfig
from app_tools.config_loader import ConfigLoader
from app_tools.my_video_capture import MyVideoCapture
from app_tools.qr.keyboard_scanner import KeyboardScanner
from app_tools.qr.zbar_qr_code_scaner import ZbarQrCodeScanner
from keygen.crypto_coin_factory import CoinFactory
from logic.coin_files_saver import CoinFilesSaver
from logic.keygen import KeygenProcessor
from logic.recovery import RecoveryProcessor
from logic.update import UpdateProcessor


class MyContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    logging = providers.Resource(
        logging.config.fileConfig,
        fname='logging.ini',
    )

    default_video_capture = providers.Singleton(MyVideoCapture)

    coin_factory = providers.Singleton(CoinFactory)

    qr_code_scanner = providers.Singleton(ZbarQrCodeScanner)

    keyboard_scanner = providers.Singleton(KeyboardScanner, word_separator=config.barcode_scanner.word_separator)

    config_loader = providers.Singleton(ConfigLoader, config)

    app_config = providers.Singleton(AppConfig)

    coin_files_saver = providers.Singleton(CoinFilesSaver, app_config=app_config)

    keygen_processor = providers.Singleton(KeygenProcessor, coin_factory=coin_factory, coin_file_saver=coin_files_saver)

    recovery_processor = providers.Singleton(RecoveryProcessor, coin_file_saver=coin_files_saver)

    update_processor = providers.Singleton(UpdateProcessor, coin_file_saver=coin_files_saver)
