import tkinter
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar

from dependency_injector.wiring import Provide

from app_tools.app_config import AppConfig
from controller.keygen_controller import KeygenController

import logging

from keygen.crypto_coin_factory import CoinFactory


class KeygenWidget:

    def __init__(self, root,
                 coin_factory: CoinFactory = Provide['coin_factory'],
                 app_config: AppConfig = Provide['app_config'],
                 ):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.root = root
        self.app_config = app_config
        self.currencies = coin_factory.get_available_currencies()

        combo_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(combo_frame, text="Select currency").pack()
        self.crypto_chosen = ttk.Combobox(combo_frame, state="readonly", width=27, values=self.currencies)
        self.crypto_chosen.current(0)
        self.crypto_chosen.pack()
        combo_frame.pack()

        count_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(count_frame, text="Select count").pack()
        default_count = tkinter.StringVar()
        default_count.set(10)
        self.count_spin = tkinter.Spinbox(count_frame, from_=1, to=1000, textvariable=default_count)
        self.count_spin.pack()
        count_frame.pack()

        self.lasers = self.app_config.get_property("lasers")
        laser_frame = tkinter.Frame(root, pady=15)
        tkinter.Label(laser_frame, text="Select laser").pack()
        self.laser_chosen = ttk.Combobox(laser_frame, width=27, values=self.lasers)
        self.laser_chosen.current(0)
        self.laser_chosen.pack()
        laser_frame.pack()

        btn_frame = tkinter.Frame(root, pady=15)
        generate_btn = tkinter.Button(btn_frame, text="Generate", width=20, height=2)
        generate_btn.config(command=self.on_generate_clicked)
        generate_btn.pack()
        btn_frame.pack()

        # Progress bar widget
        progress_frame = tkinter.Frame(root)
        self.progress = Progressbar(progress_frame, orient=tkinter.HORIZONTAL, length=100, mode='indeterminate')
        self.progress.pack()
        progress_frame.pack()

        self.keygen_controller = KeygenController(self, root)

    def on_generate_clicked(self):
        crypto_chosen = self.crypto_chosen.get()
        chosen_laser = self.laser_chosen.get()
        count = self.count_spin.get()
        self.logger.info("Generate...")
        self.logger.info("Crypto chosen: " + crypto_chosen)
        self.logger.info("Laser chosen: " + chosen_laser)
        self.logger.info("Count: " + count)
        self.progress['value'] = 100
        self.keygen_controller.generate_keys(count=count, coin=crypto_chosen, laser=chosen_laser)

    def show_success(self):
        messagebox.showinfo("Generate success", "Crypto successfully generated!", parent=self.root)
        self.progress['value'] = 0
        self.root.update()
