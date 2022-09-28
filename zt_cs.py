from scripts.wall import CsGoWall
from scripts.bhop import Bhop

import keyboard
import time

"""
made by zabbix https://github.com/zabbix-byte
"""

class Interface:
    @staticmethod
    def wall() -> None:
        CsGoWall()

    @staticmethod
    def bhop() -> None:
        Bhop()


if __name__ == '__main__':
    print('<zt_cs> cheat by zabbix')
    while True:
        time.sleep(0.0025)
        if keyboard.is_pressed('0'):
            break
        if keyboard.is_pressed('f1'):
            print('<zt_cs> wall')
            time.sleep(0.1)
            Interface.wall()
        if keyboard.is_pressed('f2'):
            print('<zt_cs> bhop')
            time.sleep(0.1)
            Interface.bhop()
