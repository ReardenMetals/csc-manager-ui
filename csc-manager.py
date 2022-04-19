import sys
import tkinter
import pygame
from app import App
from app_tools.logger import stdout_redirector
from di.containers import MyContainer
import ui
import controller


def main():
    tk = tkinter.Tk()
    pygame.mixer.init()
    App("CSC Manager UI v0.3.4", tk)
    tk.mainloop()


if __name__ == '__main__':
    sys.stdout = stdout_redirector
    container = MyContainer()
    container.init_resources()
    container.config.from_ini('config.ini')
    container.wire(modules=[sys.modules[__name__]], packages=[ui, controller])
    main()
