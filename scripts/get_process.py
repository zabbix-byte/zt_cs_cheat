import pymem
import requests
import re

"""
made by zabbix https://github.com/zabbix-byte
"""


class GetProcess:
    def __init__(self) -> None:
        self.pattern_dict = {}
        self.transform_patterns()

        self.pm = pymem.Pymem('csgo.exe')
        self.client = pymem.process.module_from_name(
            self.pm.process_handle, "client.dll").lpBaseOfDll
        self.client_leg = pymem.process.module_from_name(
            self.pm.process_handle, "client.dll")
        self.client_module = self.pm.read_bytes(
            self.client_leg.lpBaseOfDll, self.client_leg.SizeOfImage)

        self.client_state = self.get_sig("engine.dll", bytes(
            self.pattern_dict["dwClientState"], encoding="raw_unicode_escape"), 0, 1)
        self.client_state = int(self.client_state, 0)

        self.engine = pymem.process.module_from_name(
            self.pm.process_handle, "engine.dll").lpBaseOfDll
        self.engine_pointer = self.pm.read_uint(
            self.engine + self.client_state)

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
