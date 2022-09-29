from scripts.player_process import Player
from math import *
from random import randint
import keyboard
import time

"""
made by zabbix https://github.com/zabbix-byte
"""

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def angle(local: Vec3, enemy: Vec3):
    delta = Vec3(0, 0, 0)
    delta.x = local.x - enemy.x
    delta.y = local.y - enemy.y
    delta.z = local.z - enemy.z

    hyp = sqrt(delta.x * delta.x + delta.y * delta.y + delta.z * delta.z)
    new = Vec3(0, 0, 0)
    new.x = asin(delta.z / hyp) * 57.295779513082
    new.y = atan(delta.y / delta.x) * 57.295779513082

    if delta.x >= 0.0:
        new.y += 180.0

    return new

def normalize_angles(angle: Vec3):
    if angle.x > 89:
        angle.x -= 360
    elif angle.x < -89:
        angle.x += 360
    if angle.y > 180:
        angle.y -= 360
    elif angle.y < -180:
        angle.y += 360
    return angle

def cal_dist(current: Vec3, new: Vec3):
    distance = Vec3(0, 0, 0)

    distance.x = new.x - current.x

    if distance.x < -89:
        distance.x += 360
    elif distance.x > 89:
        distance.x -= 360
    if distance.x < 0.0:
        distance.x = -distance.x

    distance.y = new.y - current.y
    if distance.y < - 180:
        distance.y += 360
    elif distance.y > 180:
        distance.y -= 360
    if distance.y < 0.0:
        distance.y = -distance.y

    mag = sqrt(distance.x * distance.x + distance.y * distance.y)
    return mag
    
class Aim(Player): 
    conf_random = 10 # 5 to 25
    conf_spotted = False # Spotted
    conf_baim = False  # body-aim
    conf_aim_fov = True # Fov
    conf_smooth = True #smooth 
    conf_aimtrcs = True # rcs
    conf_sens = 0.5 # 0.5 to 1.5

    def __init__(self) -> None:
        super().__init__()
        s = 0
        n = 0
        first = True
        print('Aim running')
        random = Vec3(0, 0, 0)


        while True:
            time.sleep(0.0015)
            if self.conf_random != 0 and random.x == 0 and random.y == 0 and random.z == 0 and first:
                    random = Vec3(randint(-self.conf_random, self.conf_random), randint(-self.conf_random, self.conf_random), 0)

            target, localpos, targetpos = self.get_best_target(self.conf_spotted, self.conf_baim, self.conf_aim_fov, random)

            
            if target is not None and localpos is not None and targetpos is not None:
                if self.conf_smooth and not (self.pm.read_int(self.player + self.shoots_fired) > 1 and self.conf_aimtrcs):

                    localAngle = Vec3(0, 0, 0)
                    localAngle.x = self.pm.read_float(self.engine_pointer + self.client_state_angles)
                    localAngle.y = self.pm.read_float(self.engine_pointer + self.client_state_angles + 0x4)
                    localAngle.z = self.pm.read_float(self.player + self.vec_view_off + 0x8)

                    if s <= int(n) and cal_dist(angle(localpos, targetpos), localAngle) > 0.7:
                        n = self.step(self.conf_sens, localpos, targetpos, localAngle, s, n)
                        s += 1
                    elif s >= int(n) or cal_dist(angle(localpos, targetpos), localAngle):
                        s = 0
                        n = 0
                        random = Vec3(0, 0, 0)
                        first = False
                        self.shoot(localpos, targetpos, self.conf_aimtrcs)
                else:
                    self.shoot(localpos, targetpos, self.conf_aimtrcs)

            if keyboard.is_pressed('f3'):
                print('exit AIM')
                s = 0
                n = 0
                first = True
                random = Vec3(0, 0, 0)
                break

    def check_index(self):
        clientstate = self.pm.read_uint(self.engine + self.client_state)
        id = self.pm.read_uint(clientstate + self.client_state_get_local_player)
        return id

    def get_best_target(self, spotted, baim, aimfov, random):
        while True:
            olddist = 111111111
            newdist = 0
            target = None
            PlayerID = self.check_index()
            player_team = self.pm.read_int(self.player + self.team_num)
            engine_pointer = self.pm.read_uint(self.engine + self.client_state)
            for i in range(1, 32):
                entity = self.pm.read_uint(self.client + self.entity_list + i * 0x10)

                if entity and entity != self.player:
                    entity_hp = self.pm.read_uint(entity + self.i_health)
                    entity_dormant = self.pm.read_uint(entity + self.m_dormant)
                    entity_team = self.pm.read_uint(entity + self.team_num)
                    if spotted:
                        Entspotted = self.pm.read_uint(entity + self.m_spotted_map)
                    else:
                        Entspotted = True

                    if entity_hp > 0 and not entity_dormant and Entspotted and entity_team != player_team:
                        localAngle = Vec3(0, 0, 0)
                        localAngle.x = self.pm.read_float(engine_pointer + self.client_state_angles)
                        localAngle.y = self.pm.read_float(engine_pointer + self.client_state_angles + 0x4)
                        localAngle.z = self.pm.read_float(self.player + self.vec_view_off + 0x8)

                        localpos = Vec3(0, 0, 0)
                        localpos.x = self.pm.read_float(self.player + self.vec_origin)

                        localpos.y = self.pm.read_float(self.player + self.vec_origin + 4)
                        localpos.z = self.pm.read_float(self.player + self.vec_origin + 8) + localAngle.z
                        entity_bone = self.pm.read_uint(entity + self.bone_matrix)
                        entitypos = Vec3(0, 0, 0)
                        if baim is True:
                            entitypos.x = self.pm.read_float(entity_bone + 0x30 * 5 + 0xC) + random.x
                            entitypos.y = self.pm.read_float(entity_bone + 0x30 * 5 + 0x1C) + random.y
                            entitypos.z = self.pm.read_float(entity_bone + 0x30 * 5 + 0x2C) + random.z
                        else:
                            entitypos.x = self.pm.read_float(entity_bone + 0x30 * 8 + 0xC) + random.x
                            entitypos.y = self.pm.read_float(entity_bone + 0x30 * 8 + 0x1C) + random.y
                            entitypos.z = self.pm.read_float(entity_bone + 0x30 * 8 + 0x2C) + random.z
                        new = angle(localpos, entitypos)

                        newdist = cal_dist(localAngle, new)

                        if newdist < olddist and newdist < aimfov:
                            olddist = newdist
                            target = entity
                            targetpos = entitypos
            if target is not None:
                return target, localpos, targetpos
            else:
                return None, None, None

    def shoot(self, localpos, targetpos, aimrcs):
        Unnormal = angle(localpos, targetpos)
        Normal = normalize_angles(Unnormal)
        punchx = self.pm.read_float(self.player + self.m_aim_angle_puch)
        punchy = self.pm.read_float(self.player + self.m_aim_angle_puch + 0x4)
        if aimrcs and self.pm.read_int(self.player + self.shoots_fired) > 1:
            self.pm.write_float(
                self.engine_pointer + self.client_state_angles, Normal.x - (punchx * 2))
            self.pm.write_float(self.engine_pointer + self.client_state_angles + 0x4,
                                Normal.y - (punchy * 2))

        else:
            self.pm.write_float(
                self.engine_pointer + self.client_state_angles, Normal.x)
            self.pm.write_float(self.engine_pointer + self.client_state_angles + 0x4,
                                Normal.y)

    def step(self, smooth, CurrLocal, CurrTarget, LocalAngle, i, n):
        AngDiff = normalize_angles(angle(CurrLocal, CurrTarget))
        AngDiff.x = AngDiff.x - LocalAngle.x
        AngDiff.y = AngDiff.y - LocalAngle.y
        AngDiff.z = AngDiff.z - LocalAngle.z
        normalize_angles(AngDiff)
        Dist = sqrt(AngDiff.x * AngDiff.x + AngDiff.y * AngDiff.y + AngDiff.z * AngDiff.z)
        if i == 0:
            n = Dist * smooth
        AddAngl = Vec3(AngDiff.x / (n - i), AngDiff.y / (n - i), AngDiff.z / (n - i))
        writeang = Vec3(LocalAngle.x + AddAngl.x, LocalAngle.y + AddAngl.y, 0)
        self.pm.write_float(self.engine_pointer + self.client_state_angles, writeang.x)
        self.pm.write_float(self.engine_pointer + self.client_state_angles + 0x4, writeang.y)
        return n