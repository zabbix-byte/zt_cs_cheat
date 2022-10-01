from scripts.player_process import Player
from scripts.states import AppStates
from math import *
from scripts.ui import *
import keyboard
import time

"""
made by zabbix https://github.com/zabbix-byte
"""


class Chams(Player):
    chams_color = (255, 0, 0)
    def __init__(self) -> None:
        super().__init__()

    def get_class_id(self, entity):
        buf = self.pm.read_int(entity + 8)
        buf = self.pm.read_int(buf + 2 * 4)
        buf = self.pm.read_int(buf + 1)
        buf = self.pm.read_int(buf + 20)
        return buf

    def chams(self, entity, entity_team_id, entity_dormant, first):
        if color_chams_user.get() == 'red':
            Chams.chams_color = (255, 0, 0)
        elif color_chams_user.get() == 'green':
            Chams.chams_color = (0, 255, 0)
        elif color_chams_user.get() == 'blue':
            Chams.chams_color = (0, 0, 255)
        elif color_chams_user.get() == 'black':
            Chams.chams_color = (0, 0, 0)
        else:
            Chams.chams_color = (255, 255, 255)

        if entity and entity != 0:
            if self.get_class_id(entity) == 40:
                enemy = 2 if self.local_team == 3 else 3

                # after give color
                if entity_team_id == enemy and not entity_dormant:
                    self.pm.write_uchar(entity + 112, Chams.chams_color[0])
                    self.pm.write_uchar(entity + 113, Chams.chams_color[1])
                    self.pm.write_uchar(entity + 114, Chams.chams_color[2])

                # first add model ambients
                if first:
                    buf = 1084227584
                    point = self.pm.read_int(
                        self.engine + self.model_ambient - 44)
                    xored = buf ^ point
                    self.pm.write_int(self.engine + self.model_ambient, xored)

    def reset_chams(self, entity, entityTeam):
        if entity and entity != 0:
            if self.get_class_id(entity) == 40:
                if entityTeam != 0 and entity != self.local_player:
                    self.pm.write_uchar(entity + 112, 255)
                    self.pm.write_uchar(entity + 113, 255)
                    self.pm.write_uchar(entity + 114, 255)

                b = 0
                pointer = self.pm.read_int(
                    self.engine + self.model_ambient - 44)
                xo = b ^ pointer
                self.pm.write_int(self.engine + self.model_ambient, xo)


class Wall(Chams):
    color = (255, 0, 0)  # color of enemy
    wall_running = False
    wall_key = '7'

    def __init__(self) -> None:
        super().__init__()

        First = True
        cham = False

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

                    if radat_switch.get():
                        self.pm.write_int(entity + self.b_spotted, 1)

                    if chams_switch.get():
                        self.chams(entity, entity_team_id, entity_dormant, First)

                    if not chams_switch.get() and cham:
                        self.reset_chams(entity, entity_team_id)

                    if chams_switch.get():
                        cham = True
                    elif not chams_switch.get():
                        cham = False
                        First = True

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

        if color_wall_user.get() == 'red':
            Wall.color = (255, 0, 0)
        elif color_wall_user.get() == 'green':
            Wall.color = (0, 255, 0)
        elif color_wall_user.get() == 'blue':
            Wall.color = (0, 0, 255)
        elif color_wall_user.get() == 'black':
            Wall.color = (0, 0, 0)
        else:
            Wall.color = (255, 255, 255)

        # long wange wall
        if entity_team_id == enemy and not entity_dormant:
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0x8, float(Wall.color[0]))  # R
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0xC, float(Wall.color[1]))  # G
            self.pm.write_float(
                self.glow_manager + entity_glow * 0x38 + 0x10, float(Wall.color[2]))  # B
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
