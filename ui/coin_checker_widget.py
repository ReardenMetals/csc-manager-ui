import tkinter

from dependency_injector.wiring import Provide

from controller.coin_checker_controller import CoinCheckerController
from keygen.crypto_coin_factory import CoinFactory
from ui.footer_widget import FooterWidget
from ui.header_widget import HeaderWidget
import logging


class CoinCheckerWidget:
    def __init__(self, coin_checker_frame,
                 coin_factory: CoinFactory = Provide['coin_factory'], ):
        self.coin_factory = coin_factory
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

        self.coin_checker_frame = coin_checker_frame

        top_frame = tkinter.Frame(self.coin_checker_frame, borderwidth=3)

        currencies = self.coin_factory.get_available_currencies()
        self.currencies = currencies

        self.coin_checker_controller = CoinCheckerController(self, coin_checker_frame)

        self.header_widget = HeaderWidget(top_frame,
                                          currencies=self.currencies,
                                          on_currency_selected=self.coin_checker_controller.on_currency_selected,
                                          on_refreshed=self.coin_checker_controller.on_refreshed)
        top_frame.pack(fill=tkinter.X)

        bottom_frame_width = 650
        bottom_frame_height = 350

        bottom_frame = tkinter.Frame(self.coin_checker_frame, height=bottom_frame_height, width=bottom_frame_width,
                                     borderwidth=3)
        self.footer_widget = FooterWidget(bottom_frame, frame_width=bottom_frame_width,
                                          frame_height=bottom_frame_height,
                                          on_qr_code_scanned=self.coin_checker_controller.on_qr_code_scanned)
        bottom_frame.pack(fill=tkinter.BOTH, expand=True)
        self.bottom_frame = bottom_frame

        self.coin_checker_controller.init()
        coin_checker_frame.out_callback = self.release_camera
        coin_checker_frame.in_callback = self.init_camera

    def set_currency(self, currency):
        self.footer_widget.set_currency(currency)

    def set_action_title(self, title):
        self.footer_widget.set_action_title(title)

    def show_none(self):
        self.footer_widget.show_none()

    def show_correct(self):
        self.footer_widget.show_correct()

    def show_incorrect(self):
        self.footer_widget.show_incorrect()

    def show_coin_details_info(self, private_key, snip, address):
        self.footer_widget.show_coin_details_info(private_key, snip, address)

    def init_camera(self):
        self.logger.info("Initialized CoinChecker scanner...")
        self.coin_checker_controller.scanning_start()
        self.footer_widget.resume_camera_widget()

    def release_camera(self):
        self.coin_checker_controller.scanning_stop()
        self.logger.info("Released CoinChecker scanner.")
        self.footer_widget.pause_camera_widget()
