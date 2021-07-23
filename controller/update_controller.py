import asynctkinter as at

import logging

from dependency_injector.wiring import Provide

from logic.update import UpdateProcessor


class UpdateController:
    def __init__(self, root, window, update_processor: UpdateProcessor = Provide['update_processor']):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.update_processor = update_processor
        self.root = root
        self.window = window

    def update(self, last_good_coin):
        self.start_async(self.update_async(last_good_coin))

    async def update_async(self, last_good_coin):
        await self.run_in_thread(lambda: self.update_processor.update(last_good_coin))
        self.logger.info('Update success!')
        self.root.show_success()

    def start_async(self, task):
        at.start(task)

    def run_in_thread(self, func):
        return at.run_in_thread(func, after=self.window.after)


