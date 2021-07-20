from scan_states.scan_state import ScanState
from scan_states.states_enum import States

STATE_DELAY_CONFIG = 'apply_sticker_state_delay'


class ApplyStickerState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.logger.info("State: <ApplyStickerState>")
        self.context.set_action_title("Apply Sticker")
        self.context.show_correct()
        self.context.play_success_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        delay_config = self.get_config(STATE_DELAY_CONFIG)
        self.logger.info("CoinChecker %s: %s (ms)", STATE_DELAY_CONFIG, delay_config)
        await self.context.sleep(delay_config)  # Default 2400
        self.logger.info("Changing state to: <SCAN_COIN_STATE>")
        self.change_state(States.SCAN_COIN_STATE)
