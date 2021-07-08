from dbr import BarcodeReader, BarcodeReaderError, EnumBarcodeFormat

from app_tools.qr.qr_code_scaner import QrCodeScanner


class DynamsoftQrCodeScanner(QrCodeScanner):
    def __init__(self, license_key):
        super().__init__()
        self.reader = BarcodeReader()
        self.reader.init_license(license_key)
        self.reader.reset_runtime_settings()
        settings = self.reader.get_runtime_settings()
        settings.barcode_format_ids = EnumBarcodeFormat.BF_QR_CODE
        settings.expected_barcodes_count = 1
        settings.timeout = 100
        self.reader.update_runtime_settings(settings)
        self.barcode_info = None
        self.barcode_increment = 0  # Timestamp at the moment of the last barcode info callback
        self.increment = 0  # Current timestamp

    def read_barcodes(self, frame, callback=None):
        try:

            if callback is not None:
                self.increment += 1
                if self.increment - self.barcode_increment > 30:

                    self.logger.debug("reader.decode_buffer")
                    text_results = self.reader.decode_buffer(frame)
                    self.logger.debug("DECODED reader.decode_buffer")

                    if (text_results is not None) and (len(text_results) > 0):
                        self.logger.info("Scanned text_results")
                        text_result = text_results[0]
                        barcode_info = text_result.barcode_text

                        # if self.barcode_info != barcode_info:
                        self.logger.info("Barcode Format :")
                        self.logger.info(text_result.barcode_format_string)
                        self.logger.info("Barcode Text :")
                        self.logger.info(text_result.barcode_text)
                        self.logger.info("Localization Points : ")
                        self.logger.info(text_result.localization_result.localization_points)
                        self.logger.info("-------------")

                        self.logger.info("QR Code fetched: %s", barcode_info)
                        self.barcode_info = barcode_info
                        self.barcode_increment = self.increment
                        callback(barcode_info)

        except BarcodeReaderError as bre:
            self.logger.error(bre)

        return frame
