import ctypes
import time


# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
MOUSE_LEFTDOWN = 0x0002     # left button down
MOUSE_LEFTUP = 0x0004       # left button up
MOUSE_RIGHTDOWN = 0x0008    # right button down
MOUSE_RIGHTUP = 0x0010      # right button up
MOUSE_MIDDLEDOWN = 0x0020   # middle button down
MOUSE_MIDDLEUP = 0x0040     # middle button up


def pos(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)  # set mouse position


def left_click():
    ctypes.windll.user32.mouse_event(MOUSE_LEFTDOWN)  # left down
    ctypes.windll.user32.mouse_event(MOUSE_LEFTUP)  # left up


def right_click():
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTDOWN)  # right down
    ctypes.windll.user32.mouse_event(MOUSE_RIGHTUP)  # right up