from scripts.player_process import Player
from scripts.states import AppStates
from math import *
from scripts.ui import *
import keyboard
import time

"""
made by zabbix https://github.com/zabbix-byte
"""


class Wall(Player):
    radar = False  # radar
    chams = False  # for moment this funtion is disabled
    color = (255, 0, 0)  # color of enemy
    wall_running = False
    wall_key = '7'

    def __init__(self) -> None:
        super().__init__()
        while Wall.wall_running:
            time.sleep(0.0015)
            for i in range(0, 64):
                entity = self.pm.read_uint(
                    self.client + self.entity_list + i * 0x10)
                if entity:
                    entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant = self.get_entity_vars(
                        entity)
                    self.set_entity_glow(
                        entity_team_id, entity_dormant, entity_glow)

                    if self.radar:
                        self.pm.write_int(entity + self.b_spotted, 1)

                if wall_switch.get() == False:
                    time.sleep(0.1)
                    print('<zt_cs> Exit WALL')
                    Wall.wall_running = False
                    break

                elif keyboard.is_pressed(self.wall_key) or AppStates.APP_RUNNING == False:
                    time.sleep(0.1)
                    print('<zt_cs> Exit WALL')
                    Wall.wall_running = False

                    if wall_switch.get() == True:
                        wall_switch.deselect()
                        app.update()
                    break

    def set_entity_glow(self, entity_team_id, entity_dormant, entity_glow):
        enemy = 2 if self.local_team == 3 else 3

        # long wange wall
        if entity_team_id == enemy and not entity_dormant:
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0x8, float(self.color[0]))  # R
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0xC, float(self.color[1]))  # G
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0x10, float(self.color[2]))  # B
            self.pm.write_float(self.glow_manager +
                                entity_glow * 0x38 + 0x14, float(255))  # A
            self.pm.write_int(self.glow_manager +
                              entity_glow * 0x38 + 0x28, 1)  # Enable

    def get_entity_vars(self, entity):
        while True:
            try:
                entity_glow = self.pm.read_uint(entity + self.glow_index)
                entity_team_id = self.pm.read_uint(entity + self.team_num)
                entity_isdefusing = self.pm.read_uint(entity + self.defusing)
                entity_hp = self.pm.read_uint(entity + self.i_health)
                entity_dormant = self.pm.read_uint(entity + self.m_dormant)
            except Exception as e:
                time.sleep(0.2)
                continue
            return entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant
