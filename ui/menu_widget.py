import os
import sys
from tkinter import Menu
import webbrowser
from configparser import ConfigParser


class MenuWidget:

    def __init__(self, root):
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
        self.set_value_in_property_file('general', 'scan_mode', 'barcode_scanner')
        print("activate_barcode_scanner")
        self.restart_program()

    def activate_webcam(self):
        self.set_value_in_property_file('general', 'scan_mode', 'webcam')
        print("activate_webcam")
        self.restart_program()

    def help_index_action(self):
        webbrowser.open("https://github.com/ReardenMetals/csc-manager-ui", new=1)

    def open_settings(self):
        print('Open settings')

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def set_value_in_property_file(self, section, key, value):
        file_path = 'config.ini'
        config = ConfigParser(comment_prefixes="/", allow_no_value=True)
        config.read(file_path)
        config.set(section, key, value)
        cfgfile = open(file_path, 'w')
        config.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
        cfgfile.close()