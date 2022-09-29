from scripts.wall import CsGoWall
from scripts.bhop import Bhop
from scripts.aim import Aim
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

    @staticmethod
    def aim() -> None:
        Aim()

if __name__ == '__main__':
    print('<zt_cs> cheat by zabbix')
    while True:
        time.sleep(0.0025)
        if keyboard.is_pressed('0'):
            break
        if keyboard.is_pressed('7'):
            print('<zt_cs> wall')
            time.sleep(0.1)
            Interface.wall()
        if keyboard.is_pressed('8'):
            print('<zt_cs> bhop')
            time.sleep(0.1)
            Interface.bhop()
        if keyboard.is_pressed('9'):
            time.sleep(0.1)
            Interface.aim()
            
