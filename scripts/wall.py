import re

from get_process import GetProcess

"""
made by zabbix https://github.com/zabbix-byte
"""


class CsGoWall(GetProcess):
    def __init__(self) -> None:
        super().__init__()
        self.active_wall()

    def active_wall(self):
        address = self.client_leg.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                                          self.client_module).start() + 2
        self.pm.write_uchar(
            address, 2 if self.pm.read_uchar(address) == 1 else 1)
        self.pm.close_process()
