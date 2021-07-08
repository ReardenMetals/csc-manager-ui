
import PIL.Image
import PIL.ImageTk
from dependency_injector.wiring import Provide

from app_tools.my_video_capture import MyVideoCapture
from app_tools.qr.qr_code_scaner import QrCodeScanner
import tkinter
import imutils


class CameraWidget:
    def __init__(self, camera_frame, width, height, on_qr_scanned_callback=None, paused=False,
                 video_capture: MyVideoCapture = Provide['default_video_capture'],
                 qr_code_scanner: QrCodeScanner = Provide['qr_code_scanner']
                 ):

        self.video_capture = video_capture
        self.camera_frame = camera_frame
        self.qr_code_scanner = qr_code_scanner
        self.width = width
        self.height = height
        self.on_qr_scanned_callback = on_qr_scanned_callback
        self.photo = None
        self.paused = paused

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(self.camera_frame, width=self.width, height=self.height)
        self.canvas.pack()

        self.vid = self.video_capture
        self.delay = 40

        # self.camera_frame.after(1000, self.update_barcode_frame)

    def update_barcode_frame(self):
        if self.paused:
            return
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if frame is not None:
            frame = self.qr_code_scanner.read_barcodes(frame, callback=self.on_qr_scanned_callback)

        if frame is not None:
            frame = imutils.resize(frame, width=self.width, height=self.height)

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            self.camera_frame.after(self.delay, self.update_barcode_frame)
        else:
            self.camera_frame.after(self.delay * 100, self.update_barcode_frame)

    def pause(self):
        self.video_capture.release_camera()
        self.paused = True

    def resume(self):
        if self.paused:
            self.video_capture.init()
            self.paused = False
            if self.camera_frame is not None:
                self.camera_frame.after(100, self.update_barcode_frame)
