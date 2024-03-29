import tkinter


class LogWidget:
    def __init__(self, frame, frame_width=None):
        self.text_area = tkinter.Text(frame)
        self.text_area.bind("<Key>", lambda e: "break")
        self.text_area.pack(fill='x')

    def add_log(self, text):
        self.text_area.insert(tkinter.END, text)
        self.text_area.see(tkinter.END)
