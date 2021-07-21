import tkinter
from tkinter import Toplevel, ttk
from tkinter.ttk import Label

from dependency_injector.wiring import Provide

from app_tools.config_loader import ConfigLoader
from app_tools.config_updater import ConfigUpdater
from app_tools.os_utils import restart_program

SCAN_MODES = ['barcode_scanner', 'webcam']
SCANNER_SEPARATORS = ['enter', 'tab']
LOG_LEVELS = ['critical', 'error', 'warning', 'info', 'debug']


class SettingsWindow:

    def __init__(self, parent, config_loader: ConfigLoader = Provide['config_loader']):
        current_scan_mode = config_loader.get_general("scan_mode")
        current_word_separator = config_loader.get_barcode_scanner("word_separator")

        self.root = Toplevel(parent)

        self.root.title("Settings")

        self.root.geometry("300x300")
        self.root.resizable(False, False)

        main_container = tkinter.Frame(self.root)

        scan_mode_frame = tkinter.Frame(main_container, pady=15)
        Label(scan_mode_frame, text="Scan mode").pack()
        self.scan_mode_combobox = ttk.Combobox(scan_mode_frame, state="readonly", values=SCAN_MODES)
        self.scan_mode_combobox.current(SCAN_MODES.index(current_scan_mode))
        self.scan_mode_combobox.pack()
        scan_mode_frame.pack()

        scanner_separator_frame = tkinter.Frame(main_container, pady=15)
        Label(scanner_separator_frame, text="Scanner word separator").pack()
        self.scanner_separator_combobox = ttk.Combobox(scanner_separator_frame, state="readonly",
                                                       values=SCANNER_SEPARATORS)
        self.scanner_separator_combobox.current(SCANNER_SEPARATORS.index(current_word_separator))
        self.scanner_separator_combobox.pack()
        scanner_separator_frame.pack()

        log_levels_frame = tkinter.Frame(main_container, pady=15)
        Label(log_levels_frame, text="Log level").pack()
        self.log_levels_combobox = ttk.Combobox(log_levels_frame, state="readonly", values=LOG_LEVELS)
        current_log_level = ConfigUpdater.get_property('logger_root', 'level', file_path='logging.ini')
        self.log_levels_combobox.current(LOG_LEVELS.index(current_log_level.lower()))
        self.log_levels_combobox.pack()
        log_levels_frame.pack()

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
        ConfigUpdater.set_values_in_property_file([
            ('logger_root', 'level', self.log_levels_combobox.get().upper()),
        ], file_path='logging.ini')
        restart_program()
