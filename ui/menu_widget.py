from tkinter import Menu
import webbrowser

from app_tools.config_updater import ConfigUpdater
from app_tools.os_utils import restart_program
from ui.settings_window import SettingsWindow


class MenuWidget:

    def __init__(self, root):
        self.root = root

        self.menu_bar = Menu(root)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Settings", command=self.open_settings)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        view_menu = Menu(self.menu_bar)
        # https://stackoverflow.com/questions/45921703/how-to-add-radiobuttons-to-a-submenu-in-tkinter
        view_menu.add_radiobutton(label="barcode_scanner", command=self.activate_barcode_scanner, var=1, value=1)
        view_menu.add_radiobutton(label="webcam", command=self.activate_webcam, var=1, value=2)
        self.menu_bar.add_cascade(label='Scan Mode', menu=view_menu)

        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="Help Index", command=self.help_index_action)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=self.menu_bar)

    def activate_barcode_scanner(self):
        ConfigUpdater.set_value_in_property_file('general', 'scan_mode', 'barcode_scanner')
        restart_program()

    def activate_webcam(self):
        ConfigUpdater.set_value_in_property_file('general', 'scan_mode', 'webcam')
        restart_program()

    def help_index_action(self):
        webbrowser.open("https://github.com/ReardenMetals/csc-manager-ui", new=1)

    def open_settings(self):
        print('Open settings')
        SettingsWindow(self.root)
