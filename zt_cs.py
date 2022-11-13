

import psutil
import time

"""
made by zabbix https://github.com/zabbix-byte
"""


def check_if_process_is_running(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''

    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


if __name__ == '__main__':
    cs_go_is_find = False

    while True:
        time.sleep(0.01)
        if check_if_process_is_running('csgo.exe'):
            cs_go_is_find = True
            break
    
    if cs_go_is_find:
        from scripts.ui import app
        from scripts.interface import *

        back_process = threading.Thread(target=back_process)
        back_process.start()

        print('<zt_cs> cheat by zabbix')
        app.mainloop()
    
    
            
