from scan_states.context import Context
from scan_states.scan_state import ScanState
from scan_states.states_enum import States


class ScanCoinState(ScanState):

    def __init__(self, context: Context):
        super().__init__(context)
        self.private_key_text = None
        self.coin_processing = False

    def init_state(self):
        super().init_state()
        self.context.set_action_title("Scan Coin")
        self.context.show_none()
        self.context.clear_data()

    def on_qr_code_scanned(self, qr_code_text):
        super().on_qr_code_scanned(qr_code_text)
        if not self.coin_processing:
            self.coin_processing = True
            self.on_private_key_scanned(qr_code_text)

    def on_private_key_scanned(self, private_key_text):
        if private_key_text != self.private_key_text:
            self.logger.info("Start processing: get_address_and_id")
            self.private_key_text = private_key_text
            self.logger.info('private_key: %s', self.private_key_text)
            private_key = self.private_key_text
            self.context.set_coin_private_key(private_key)
            self.context.show_coin_private_key()
            self.context.start_async(self.load_address_from_private_async(private_key))

    async def load_address_from_private_async(self, private_key):
        address, asset_id, error = await self.context.run_in_thread(lambda: self.load_address_and_id(private_key))
        if error is None:
            self.logger.info('address, asset_id, private_key')
            self.logger.info('%s %s %s', address, asset_id, private_key)
            if address is not None and asset_id is not None:
                self.context.set_fetched_address(address)
                self.context.set_fetched_snip(asset_id)
                self.context.show_coin_info()
                self.context.play_success_song()
                self.change_state(States.SCAN_STICKER_STATE)
        else:
            self.logger.error('Error scanning coin')
            self.context.set_fetched_address('error')
            self.context.set_fetched_snip('error')
            self.context.show_error()
            self.change_state(States.SCAN_COIN_ERROR_STATE)

    def load_address_and_id(self, private_key):
        try:
            address, asset_id = self.context.load_address_and_id(private_key)
            return address, asset_id, None
        except Exception as e:
            address = None
            asset_id = None
            error = "Error loading address"
            self.logger.error(error)
            self.logger.error(e)
            return address, asset_id, error
