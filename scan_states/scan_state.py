from scan_states.context import Context
from scan_states.states_enum import States
import logging


class ScanState:

    def __init__(self, context: Context):
        self.logger = logging.getLogger(f'{self.__class__.__name__}',)
        self.context = context

    def init_state(self):
        self.logger.info("Init new state")

    def change_state(self, new_state: States):
        self.context.change_state(new_state)

    def on_qr_code_scanned(self, qr_code_text):
        self.logger.info("Received on_qr_code_scanned: %s", qr_code_text)

    def get_config(self, key: str):
        return self.context.get_config(key)
