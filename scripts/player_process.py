from scripts.get_process import GetProcess
from scripts.netvars import NETVARS

"""
made by zabbix https://github.com/zabbix-byte
"""


class Player(GetProcess):
    def __init__(self) -> None:
        super().__init__()
        
        self.local_player = self.get_sig("client.dll", bytes(
            self.pattern_dict["dwLocalPlayer"], encoding="raw_unicode_escape"), 4, 3)
        self.local_player = int(self.local_player, 0)
        self.player = self.pm.read_uint(self.client + self.local_player)

        self.force_jump = self.get_sig("client.dll", bytes(
            self.pattern_dict["dwForceJump"], encoding="raw_unicode_escape"), 0, 2)
        self.force_jump = int(self.force_jump, 0)

        self.m_aim_angle_puch = int(
            NETVARS['DT_Local']['m_aimPunchAngle']) + 12236
        self.send_packet = self.get_sig("engine.dll", bytes(
            self.pattern_dict["dwbSendPackets"], encoding="raw_unicode_escape"), 1)

        self.dw_input = self.get_sig("client.dll", bytes(
            self.pattern_dict["dwInput"], encoding="raw_unicode_escape"), 0, 1)
        self.dw_input = int(self.dw_input, 0)

        self.clientstate_last_outgoing_command = self.get_sig("engine.dll", bytes(
            self.pattern_dict["clientstate_last_outgoing_command"], encoding="raw_unicode_escape"), 0, 2, False)
        self.clientstate_last_outgoing_command = int(
            self.clientstate_last_outgoing_command, 0)

        self.client_state_net_channel = self.get_sig("engine.dll", bytes(
            self.pattern_dict["clientstate_net_channel"], encoding="raw_unicode_escape"), 0, 2, False)
        self.client_state_net_channel = int(self.client_state_net_channel, 0)

        self.shoots_fired = int(
            NETVARS["DT_CSLocalPlayerExclusive"]["m_iShotsFired"])

        self.client_state_angles = int(self.get_sig("engine.dll", bytes(
            self.pattern_dict["dwClientState_ViewAngles"], encoding="raw_unicode_escape"), 0, 4, False), 0)

        self.vec_view_off = int(NETVARS["DT_LocalPlayerExclusive"]["m_vecViewOffset[0]"])

        self.client_state_get_local_player = self.get_sig("engine.dll", bytes(self.pattern_dict["dwClientState_GetLocalPlayer"], encoding="raw_unicode_escape"), 0, 2, False)
        self.client_state_get_local_player = int(self.client_state_get_local_player, 0)

        self.team_num = int(NETVARS["DT_BaseEntity"]["m_iTeamNum"])

        self.entity_list = self.get_sig("client.dll",bytes(self.pattern_dict["dwEntityList"], encoding="raw_unicode_escape"), 0, 1 )
        self.entity_list = int(self.entity_list, 0)

        self.i_health = int(NETVARS["DT_BasePlayer"]["m_iHealth"])

        self.m_dormant = self.get_sig("client.dll", bytes(self.pattern_dict["m_bDormant"], encoding="raw_unicode_escape"), 8, 2, False)
        self.m_dormant = int(self.m_dormant, 0)

        self.m_spotted_map = int(NETVARS["DT_BaseEntity"]["m_bSpottedByMask"])

        self.vec_origin = int(NETVARS["DT_BaseEntity"]["m_vecOrigin"])
        self.bone_matrix = int(NETVARS["DT_BaseAnimating"]["m_nForceBone"]) + 28

        self.gun_game_immunity = int(NETVARS["DT_CSPlayer"]["m_bGunGameImmunity"])

        self.glow_manager = self.get_sig("client.dll", bytes(self.pattern_dict["dwGlowObjectManager"], encoding="raw_unicode_escape"), 4, 1)
        self.glow_manager = int(self.glow_manager, 0)

        self.crosshairid = int(NETVARS["DT_CSPlayer"]["m_bHasDefuser"]) + 92


        self.get_player_vars()

        self.glow_index = int(NETVARS["DT_CSPlayer"]["m_flFlashDuration"]) + 24

        self.defusing = int(NETVARS["DT_CSPlayer"]["m_bIsDefusing"])

        self.b_spotted = int(NETVARS["DT_BaseEntity"]["m_bSpotted"])



    def get_player_vars(self):
        self.player = self.pm.read_uint(self.client + self.local_player)
        self.engine_pointer = self.pm.read_uint(self.engine + self.client_state)
        self.glow_manager = self.pm.read_uint(self.client + self.glow_manager)
        self.crosshairid = self.pm.read_uint(self.player + self.crosshairid)
        self.getcrosshairtarget = self.pm.read_uint(self.client + self.entity_list + (self.crosshairid - 1) * 0x10)
        self.immunitygunganme = self.pm.read_uint(self.getcrosshairtarget + self.gun_game_immunity)
        self.local_team = self.pm.read_uint(self.player + self.team_num)
        self.crosshairteam = self.pm.read_uint(self.getcrosshairtarget + self.team_num)
        self.y_angle = self.pm.read_float(self.engine_pointer + self.client_state_angles + 0x4)


    
