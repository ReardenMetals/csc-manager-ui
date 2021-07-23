from scan_states.scan_state import ScanState
from scan_states.states_enum import States

STATE_DELAY_CONFIG = 'mismatch_state_delay'


class MismatchState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Mismatch")
        self.context.show_incorrect()
        self.context.play_error_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        delay_config = self.get_config(STATE_DELAY_CONFIG)
        self.logger.info("CoinChecker %s: %s (ms)", STATE_DELAY_CONFIG, delay_config)
        await self.context.sleep(delay_config)  # Default 2000
        self.logger.info("Changing state to: <SCAN_STICKER_STATE>")
        self.change_state(States.SCAN_STICKER_STATE)
