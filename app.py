
from app_tools.logger import StdoutRedirector, stdout_redirector
from scan_states.context import Context
from ui.main_widget import MainWidget


class App(Context):

    def __init__(self, window_title, window):
        super().__init__()
        self.window = window
        self.window.title(window_title)
        self.main_widget = MainWidget(self.window)
        stdout_redirector.set_listener(self)

    def log(self, log):
        self.window.after(10, lambda: self.main_widget.add_log(log))
