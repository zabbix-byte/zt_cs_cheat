from scripts.wall import Wall
from scripts.bhop import Bhop
from scripts.aim import Aim
import keyboard
import time
import threading

"""
made by zabbix https://github.com/zabbix-byte
"""

class Interface:
    @staticmethod
    def wall() -> None:
        Wall()

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

        if keyboard.is_pressed(Wall.wall_key) and Wall.wall_running == False:
            print('<zt_cs> WALL')
            time.sleep(0.1)
            Wall.wall_running = True
            wall = threading.Thread(target=Interface.wall)
            wall.start()

        if keyboard.is_pressed(Bhop.bhop_key) and Bhop.bhop_running == False:
            print('<zt_cs> BHOP')
            time.sleep(0.1)
            Bhop.bhop_running = True
            bhop = threading.Thread(target=Interface.bhop)
            bhop.start()
            
        if keyboard.is_pressed(Aim.aim_key) and Aim.aim_running == False:
            print('<zt_cs> AIM')
            time.sleep(0.1)
            Aim.aim_running = True
            aim = threading.Thread(target=Interface.aim)
            aim.start()
            
