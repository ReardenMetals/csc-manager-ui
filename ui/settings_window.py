import tkinter
from tkinter import Toplevel, ttk
from tkinter.ttk import Label

from dependency_injector.wiring import Provide

from app_tools.config_loader import ConfigLoader
from app_tools.config_updater import ConfigUpdater
from app_tools.os_utils import restart_program


class SettingsWindow:

    def __init__(self, parent, config_loader: ConfigLoader = Provide['config_loader']):

        current_scan_mode = config_loader.get_general("scan_mode")
        current_word_separator = config_loader.get_barcode_scanner("word_separator")

        self.root = Toplevel(parent)

        self.root.title("Settings")

        self.root.geometry("300x300")
        self.root.resizable(False, False)

        main_container = tkinter.Frame(self.root)

        scan_modes = ['barcode_scanner', 'webcam']
        scan_mode_frame = tkinter.Frame(main_container, pady=15)
        Label(scan_mode_frame, text="Scan mode").pack()
        self.scan_mode_combobox = ttk.Combobox(scan_mode_frame, state="readonly", values=scan_modes)
        self.scan_mode_combobox.current(scan_modes.index(current_scan_mode))
        self.scan_mode_combobox.pack()
        scan_mode_frame.pack()

        scanner_separators = ['enter', 'tab']
        scanner_separator_frame = tkinter.Frame(main_container, pady=15)
        Label(scanner_separator_frame, text="Scanner word separator").pack()
        self.scanner_separator_combobox = ttk.Combobox(scanner_separator_frame, state="readonly",
                                                       values=scanner_separators)
        self.scanner_separator_combobox.current(scanner_separators.index(current_word_separator))
        self.scanner_separator_combobox.pack()
        scanner_separator_frame.pack()

        btn_frame = tkinter.Frame(main_container, pady=15)
        save_btn = tkinter.Button(btn_frame, text="Save & Restart", width=20, height=2)
        save_btn.config(command=self.on_save_clicked)
        save_btn.pack()
        btn_frame.pack()

        main_container.pack()

    def on_save_clicked(self):
        ConfigUpdater.set_values_in_property_file([
            ('general', 'scan_mode', self.scan_mode_combobox.get()),
            ('barcode_scanner', 'word_separator', self.scanner_separator_combobox.get())
        ])
        restart_program()
