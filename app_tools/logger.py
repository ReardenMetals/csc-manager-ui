import sys


class StdoutRedirector(object):

    def __init__(self, listener=None):
        self.listener = listener

    def write(self, log):
        if sys.__stdout__ is not None:
            sys.__stdout__.write(log)
        if self.listener is not None:
            self.listener.log(log)

    def flush(self) -> None:
        sys.__stdout__.flush()

    def set_listener(self, listener=None):
        self.listener = listener


stdout_redirector = StdoutRedirector()

