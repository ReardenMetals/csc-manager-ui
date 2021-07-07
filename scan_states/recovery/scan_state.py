from scan_states.recovery.context import Context
from scan_states.recovery.states_enum import States
import logging


class ScanState:

    def __init__(self, context: Context):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.context = context

    def init_state(self):
        pass

    def change_state(self, new_state: States):
        self.context.change_state(new_state)

    def on_qr_code_scanned(self, qr_code_text):
        self.logger.info("on_qr_code_scanned: %s", qr_code_text)
