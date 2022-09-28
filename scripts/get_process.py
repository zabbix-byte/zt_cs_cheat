import pymem

"""
made by zabbix https://github.com/zabbix-byte
"""


class GetProcess:
    def __init__(self) -> None:
        self.pm = pymem.Pymem('csgo.exe')
        self.client = pymem.process.module_from_name(
            self.pm.process_handle, "client.dll").lpBaseOfDll
        self.client_leg = pymem.process.module_from_name(
            self.pm.process_handle, "client.dll")
        self.client_module = self.pm.read_bytes(
            self.client_leg.lpBaseOfDll, self.client_leg.SizeOfImage)
