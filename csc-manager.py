import tkinter

import sys

from app import App
import pygame

from app_tools.logger import stdout_redirector
from di.containers import MyContainer


def main():
    tk = tkinter.Tk()
    pygame.mixer.init()
    App("CSC Manager 1.3.0", tk)
    tk.mainloop()


if __name__ == '__main__':
    sys.stdout = stdout_redirector
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]])
    main()
