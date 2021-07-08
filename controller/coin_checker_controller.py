import asynctkinter as at
import pygame
from dependency_injector.wiring import Provide

from keygen.crypto_coin_factory import CoinFactory
from scan_states.context import Context
from scan_states.state_factory import get_state
from scan_states.states_enum import States
import logging

from pynput import keyboard
from pynput.keyboard import Key


class CoinCheckerController(Context):
    def __init__(self, root, window, coin_factory: CoinFactory = Provide['coin_factory']):
        super().__init__()
        self.coin_factory = coin_factory
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.root = root
        self.window = window

        self.state = None
        self.coin_service = None
        self.currency = None

        self.fetched_address = None
        self.private_key = None
        self.snip = None
        self.qr_text1 = ''

    def init(self):
        currencies = self.coin_factory.get_available_currencies()
        self.currency = currencies[0]

        self.select_currency(self.currency)
        self.start_async(self.test_async())

    async def test_async(self):
        await self.run_in_thread(lambda: self.test())

    def test(self):
        while True:
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

    def on_press(self, key):
        if key != Key.enter:
            self.qr_text1 = self.qr_text1 + key.char
        # print(self.qr_text1)

    def on_release(self, key):
        if key == Key.enter:
            print(self.qr_text1)
            self.on_qr_code_scanned(self.qr_text1)
            self.qr_text1 = ''
            return False

    def on_currency_selected(self, currency):
        self.select_currency(currency)

    def on_refreshed(self):
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
        self._play_song("./resources/audio/definite.mp3")

    def play_error_song(self):
        self._play_song("./resources/audio/no-trespassing.mp3")

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)

    def sleep(self, milliseconds):
        return at.sleep(milliseconds, after=self.window.after)

    @staticmethod
    def _play_song(file_name: str):
        music = pygame.mixer.music
        music.load(file_name)
        music.play()
