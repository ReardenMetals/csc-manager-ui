import asynctkinter as at
import pygame
from dependency_injector.wiring import Provide

from app_tools.config_loader import ConfigLoader
from app_tools.qr.keyboard_scanner import KeyboardScanner
from keygen.crypto_coin_factory import CoinFactory
from scan_states.context import Context
from scan_states.state_factory import get_state
from scan_states.states_enum import States
import logging

FAILURE_SONG_CONFIG = 'failure_song'
SUCCESS_SONG_CONFIG = 'success_song'


class CoinCheckerController(Context):
    def __init__(self, root, window,
                 coin_factory: CoinFactory = Provide['coin_factory'],
                 keyboard_scanner: KeyboardScanner = Provide['keyboard_scanner'],
                 config_loader: ConfigLoader = Provide['config_loader'],
                 ):
        super().__init__()
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.coin_factory = coin_factory
        self.config_loader = config_loader
        self.keyboard_scanner = keyboard_scanner
        self.root = root
        self.window = window

        self.state = None
        self.coin_service = None
        self.currency = None

        self.fetched_address = None
        self.private_key = None
        self.snip = None

        self.music = pygame.mixer.music

    def init(self):
        currencies = self.coin_factory.get_available_currencies()
        self.currency = currencies[0]
        self.select_currency(self.currency)

    def keyboard_scanning_enabled(self):
        return self.config_loader.get_general('scan_mode') == 'BARCODE_SCANNER'

    def scanning_start(self):
        if self.keyboard_scanning_enabled() and self.keyboard_scanner is not None:
            self.logger.info("Scanning started...")
            self.keyboard_scanner.scan_text(self.on_qr_code_scanned)

    def scanning_stop(self):
        if self.keyboard_scanning_enabled() and self.keyboard_scanner is not None:
            self.logger.info("Scanning stopped")
            self.keyboard_scanner.scanning_release()

    def on_currency_selected(self, currency):
        self.select_currency(currency)

    def on_refreshed(self):
        self.scanning_start()
        self.change_state(States.SCAN_COIN_STATE)

    def select_currency(self, currency):
        self.currency = currency
        self.coin_service = self.coin_factory.get_coin_service(self.currency)
        self.change_state(States.SCAN_COIN_STATE)
        self.root.set_currency(currency)
        self.logger.info("Selected currency: %s", self.currency)

    def on_qr_code_scanned(self, qr_code_text):
        self.state.on_qr_code_scanned(qr_code_text)

    def clear_data(self):
        self.fetched_address = None
        self.private_key = None
        self.snip = None

    def change_state(self, new_state: States):
        self.logger.info("New state: %s", new_state)
        self.state = get_state(new_state, self)
        self.state.init_state()

    def get_private_key(self):
        return self.private_key

    def set_coin_private_key(self, private_key):
        self.private_key = private_key

    def get_fetched_address(self):
        return self.fetched_address

    def set_fetched_address(self, fetched_address):
        self.fetched_address = fetched_address

    def set_fetched_snip(self, snip):
        self.snip = snip

    def load_address_and_id(self, private_key):
        return self.coin_service.get_address_and_id(private_key)

    def set_action_title(self, title: str):
        self.root.set_action_title(title)

    def show_none(self):
        self.root.show_none()

    def show_correct(self):
        self.root.show_correct()

    def show_incorrect(self):
        self.root.show_incorrect()

    def show_coin_info(self):
        private_key = self.private_key
        snip = self.snip
        address = self.fetched_address
        self.root.show_coin_details_info(private_key=private_key, snip=snip, address=address)

    def show_error(self):
        self.root.show_coin_details_info('error', 'error', 'error')

    def show_coin_private_key(self):
        private_key = self.private_key
        self.root.show_coin_details_info(private_key, "...", "...")

    def play_success_song(self):
        success_song = self.get_config(SUCCESS_SONG_CONFIG)
        self.logger.info("Success song: %s", success_song)
        self._play_song(success_song)

    def play_error_song(self):
        failure_song = self.get_config(FAILURE_SONG_CONFIG)
        self.logger.info("Failure song: %s", failure_song)
        self._play_song(failure_song)

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)

    def sleep(self, milliseconds):
        return at.sleep(milliseconds, after=self.window.after)

    def _play_song(self, file_name: str):
        if file_name:
            self.music.load(file_name)
            self.music.play()

    def get_config(self, key: str):
        return self.config_loader.get_coin_checker(key)
