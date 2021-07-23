import logging
import tkinter


class DispatcherTab(tkinter.Frame):

    def __init__(self, parent, in_callback=None, out_callback=None):
        self.logger = logging.getLogger(f'{self.__class__.__name__}', )
        self.parent = parent
        self.in_callback = in_callback
        self.out_callback = out_callback
        tkinter.Frame.__init__(self, parent)

    def on_visible_in(self, parent, id, str):
        self.logger.debug("on_visible_in: parent=%s, ID=%s, str=%s", parent, id, str)
        if self.in_callback is not None:
            self.in_callback()

    def on_visible_out(self, parent, id, str):
        self.logger.debug("on_visible_in: parent=%s, ID=%s, str=%s", parent, id, str)
        if self.out_callback is not None:
            self.out_callback()
