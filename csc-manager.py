import tkinter

from app import App
import pygame


def main():
    tk = tkinter.Tk()
    pygame.mixer.init()
    App("CSC Manager 1.3.0", tk)
    tk.mainloop()


if __name__ == '__main__':
    main()
