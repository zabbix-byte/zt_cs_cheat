from scripts.player_process import Player
from scripts.netvars import NETVARS
from scripts.states import AppStates
from scripts.ui import *

import keyboard
import time

"""
made by zabbix https://github.com/zabbix-byte
"""


class Bhop(Player):
    bhop_running = False
    bhop_key = '8'
    def __init__(self) -> None:
        super().__init__()
        try:
            while Bhop.bhop_running:
                time.sleep(0.0015)

                if keyboard.is_pressed('space'):
                    self.active_bhop()

                if bhop_switch.get() == False:
                    time.sleep(0.1)
                    print('<zt_cs> Exit BHOP')
                    Bhop.bhop_running = False
                    
                elif keyboard.is_pressed(self.bhop_key) or AppStates.APP_RUNNING == False:
                    time.sleep(0.1)
                    print('<zt_cs> EXIT BHOP')
                    
                    if bhop_switch.get() == True:
                        bhop_switch.deselect()
                        app.update()

                    Bhop.bhop_running = False
        except:
            if aim_switch.get() == True:
                aim_switch.deselect()

            if wall_switch.get() == True:
                wall_switch.deselect()

            if bhop_switch.get() == True:
                bhop_switch.deselect()
    def active_bhop(self):
        force_jump = self.client + self.force_jump
        on_ground = self.pm.read_uint(
            self.player + NETVARS["DT_BasePlayer"]["m_fFlags"])
        if self.player and on_ground == 257 or on_ground == 263:
            self.pm.write_int(force_jump, 6)
