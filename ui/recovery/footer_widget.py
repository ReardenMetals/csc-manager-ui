import tkinter
from tkinter import LEFT, RIGHT

from dependency_injector.wiring import Provide

from app_tools.config_loader import ConfigLoader
from ui.camera_widget import CameraWidget
from ui.recovery.coin_widget import CoinWidget


class FooterWidget:

    def __init__(self, frame, frame_width, frame_height, on_qr_code_scanned,
                 config_loader: ConfigLoader = Provide['config_loader'],):
        self.frame = frame

        left_frame = tkinter.Frame(self.frame, width=frame_width, height=frame_height, bg="GREY", borderwidth=2)
        self.coin_widget = CoinWidget(left_frame, frame_width=frame_width, frame_height=frame_height)
        left_frame.pack(side=LEFT)

        camera_enabled = (config_loader.get_general('scan_mode') == 'webcam')

        camera_width = frame_width
        camera_height = frame_height

        if camera_enabled:
            camera_frame = tkinter.Frame(self.frame, width=camera_width, height=camera_height, borderwidth=2)
            self.camera_widget = CameraWidget(camera_frame=camera_frame, width=camera_width, height=camera_height,
                                              on_qr_scanned_callback=on_qr_code_scanned, paused=True)
            camera_frame.pack(side=RIGHT)
        else:
            tkinter.Frame(self.frame, width=camera_width, height=camera_height, borderwidth=2).pack(side=RIGHT)
            self.camera_widget = None

    def set_currency(self, currency):
        self.coin_widget.set_currency(currency)

    def set_action_title(self, title):
        self.coin_widget.set_action_title(title)

    def show_none(self):
        self.coin_widget.show_none()

    def show_correct(self):
        self.coin_widget.show_correct()

    def show_incorrect(self):
        self.coin_widget.show_incorrect()

    def show_coin_details_info(self, private_key, snip, address):
        self.coin_widget.show_coin_details_info(private_key, snip, address)

    def resume_camera_widget(self):
        if self.camera_widget is not None:
            self.camera_widget.resume()

    def pause_camera_widget(self):
        if self.camera_widget is not None:
            self.camera_widget.pause()