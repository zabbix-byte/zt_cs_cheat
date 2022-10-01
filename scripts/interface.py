from scripts.wall import Wall
from scripts.bhop import Bhop
from scripts.aim import Aim
from scripts.states import AppStates
from scripts.ui import *

import time
import keyboard
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


def commads():
    while True:
        time.sleep(0.0025)
        if AppStates.APP_RUNNING == False:
            exit()

        if keyboard.is_pressed('0'):
            exit()

        if wall_switch.get() == True and Wall.wall_running == False:
            print('<zt_cs> WALL switch')
            time.sleep(0.1)
            Wall.wall_running = True
            wall = threading.Thread(target=Interface.wall)
            wall.start()

        if keyboard.is_pressed(Wall.wall_key) and Wall.wall_running == False:
            print('<zt_cs> WALL button')
            time.sleep(0.1)
            Wall.wall_running = True

            if wall_switch.get() == False:
                wall_switch.select()
                app.update()

            wall = threading.Thread(target=Interface.wall)
            wall.start()

        if aim_switch.get() == True and Aim.aim_running == False:
            print('<zt_cs> AIM switch')
            time.sleep(0.1)
            Aim.aim_running = True
            aim = threading.Thread(target=Interface.aim)
            aim.start()

        if keyboard.is_pressed(Aim.aim_key) and Aim.aim_running == False:
            print('<zt_cs> AIM button')
            time.sleep(0.1)
            Aim.aim_running = True
            if aim_switch.get() == False:
                aim_switch.select()
                app.update()
            aim = threading.Thread(target=Interface.aim)
            aim.start()

        if bhop_switch.get() == True and Bhop.bhop_running == False:
            print('<zt_cs> BHOP switch')
            time.sleep(0.1)
            Bhop.bhop_running = True
            bhop = threading.Thread(target=Interface.bhop)
            bhop.start()

        if keyboard.is_pressed(Bhop.bhop_key) and Bhop.bhop_running == False:
            print('<zt_cs> BHOP button')
            time.sleep(0.1)
            Bhop.bhop_running = True
            if bhop_switch.get() == False:
                bhop_switch.select()
                app.update()
            bhop = threading.Thread(target=Interface.bhop)
            bhop.start()
        