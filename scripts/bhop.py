from scripts.player_process import Player
from scripts.netvars import NETVARS

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
        while True:
            time.sleep(0.0015)
            if keyboard.is_pressed('space'):
                self.active_bhop()

            if keyboard.is_pressed(Bhop.bhop_key):
                time.sleep(0.1)
                print('<zt_cs> EXIT BHOP')
                Bhop.bhop_running = False
                break

    def active_bhop(self):
        force_jump = self.client + self.force_jump
        on_ground = self.pm.read_uint(
            self.player + NETVARS["DT_BasePlayer"]["m_fFlags"])
        if self.player and on_ground == 257 or on_ground == 263:
            self.pm.write_int(force_jump, 6)
