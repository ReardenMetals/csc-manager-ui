import logging


class QrCodeScanner:
    def __init__(self, ):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )

    def read_barcodes(self, frame, callback=None):
        pass
