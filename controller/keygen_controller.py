import asynctkinter as at

import logging

from logic.keygen import KeygenProcessor


class KeygenController:
    def __init__(self, root, window):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.root = root
        self.window = window
        self.keygen = KeygenProcessor()

    def generate_keys(self, count, coin, laser):
        self.start_async(self.generate_keys_async(count, coin, laser))

    async def generate_keys_async(self, count, coin, laser):
        await self.run_in_thread(lambda: self.keygen.generate_keys(count, coin, laser))
        self.logger.debug("self.root.show_success()")
        self.window.after(10, lambda: self.root.show_success())

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after, polling_interval=10, daemon=True)

