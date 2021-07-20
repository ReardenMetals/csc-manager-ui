from scan_states.recovery.scan_state import ScanState
from scan_states.recovery.states_enum import States

STATE_DELAY_CONFIG = 'apply_coin_state_delay'


class ApplyCoinState(ScanState):

    def __init__(self, context):
        super().__init__(context)

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Apply Coin")
        self.context.show_correct()
        self.context.play_success_song()
        self.context.start_async(self.delay_task())

    async def delay_task(self):
        delay_config = self.get_config(STATE_DELAY_CONFIG)
        self.logger.info("Recovery %s: %s (ms)", STATE_DELAY_CONFIG, delay_config)
        await self.context.sleep(delay_config)  # Default 1000
        self.logger.info("Changing state to: <SCAN_COIN_STATE>")
        self.change_state(States.SCAN_COIN_STATE)
