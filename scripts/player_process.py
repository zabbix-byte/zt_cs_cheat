from get_process import GetProcess
import re
import pymem
import requests

"""
made by zabbix https://github.com/zabbix-byte
"""


class Player(GetProcess):
    def __init__(self) -> None:
        super().__init__()
        self.pattern_dict = {}
        self.transform_patterns()

        self.local_player = self.get_sig("client.dll", bytes(
            self.pattern_dict["dwLocalPlayer"], encoding="raw_unicode_escape"), 4, 3)
        self.local_player = int(self.local_player, 0)
        self.player = self.pm.read_uint(self.client + self.local_player)

        self.force_jump = self.get_sig("client.dll", bytes(
            self.pattern_dict["dwForceJump"], encoding="raw_unicode_escape"), 0, 2)
        self.force_jump = int(self.force_jump, 0)

    def get_sig(self, modulename, pattern, extra=0, offset=0, relative=True):
        if offset == 0:
            module = pymem.process.module_from_name(
                self.pm.process_handle, modulename)
            bytes = self.pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
            match = re.search(pattern, bytes).start()
            res = match + extra
            return res
        module = pymem.process.module_from_name(
            self.pm.process_handle, modulename)
        bytes = self.pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
        match = re.search(pattern, bytes).start()
        non_relative = self.pm.read_int(
            module.lpBaseOfDll + match + offset) + extra
        yes_relative = self.pm.read_int(
            module.lpBaseOfDll + match + offset) + extra - module.lpBaseOfDll
        return "0x{:X}".format(yes_relative) if relative else "0x{:X}".format(non_relative)

    def transform_patterns(self):
        response = requests.get(
            "https://raw.githubusercontent.com/frk1/hazedumper/master/config.json").json()
        for struct in response["signatures"]:
            old = str(struct["pattern"])
            new = old.replace("?", ".")
            new = new.split(" ")
            newone = ""
            for element in new:
                if element != ".":
                    element = r'\x' + element
                newone = newone + element
            self.pattern_dict[struct["name"]] = newone
