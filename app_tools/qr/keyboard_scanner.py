from pynput import keyboard
from pynput.keyboard import Key
import logging


class KeyboardScanner:

    def __init__(self):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.__chars_list = []
        self.__text_listener = None
        self.__keyboard_listener = None

    def scan_text(self, text_listener):
        if self.__keyboard_listener is not None:
            self.scanning_release()
        self.__text_listener = text_listener
        self.__chars_list = []
        self.__keyboard_listener = keyboard.Listener(
            on_press=self.__on_press,
            on_release=self.__on_release)
        self.__keyboard_listener.start()

    def scanning_release(self):
        self.__text_listener = None
        if self.__keyboard_listener is not None:
            self.__keyboard_listener.stop()
            self.__keyboard_listener = None
        self.logger.info("Scanning engine released...")

    def __on_press(self, key: Key):
        try:
            if len(self.__chars_list) == 0:
                self.logger.info("Scanning new word...")
            self.logger.debug('alphanumeric key {0} pressed'.format(key.char))
            self.__chars_list.append(key.char)
        except AttributeError:
            self.logger.debug('special key {0} pressed'.format(
                key))

    def __on_release(self, key: Key):
        self.logger.debug('{0} released'.format(
            key))
        if key == keyboard.Key.enter:
            # Stop listener
            text = ''.join(map(str, self.__chars_list))
            self.__chars_list = []
            if self.__text_listener is not None:
                self.logger.info("Scanned word: %s", text)
                self.__text_listener(text)
        if key == keyboard.Key.esc:
            return False
