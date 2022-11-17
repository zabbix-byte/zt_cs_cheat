import tkinter
import customtkinter
from tkinter import *
from tkinter.ttk import *

from scripts.states import AppStates
from scripts.utl import *

"""
made by zabbix https://github.com/zabbix-byte
"""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("450x700")
app.title("ZT CHEAT CS GO BETA")
app.resizable(0, 0)
app.attributes('-topmost', True)

app.iconbitmap("ico.ico")


def button_exit():
    AppStates.APP_RUNNING = False
    app.quit()



app.protocol("WM_DELETE_WINDOW", button_exit)
app.update()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=5, padx=10, fill="both", expand=True)

title = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.LEFT, text='ZT CHEAT CS GO BETA')
title.pack(side='left', padx=145)




### WALL ####
wall_frame = customtkinter.CTkFrame(master=app)
wall_frame.pack(pady=10, padx=40, fill="both", expand=True)


title_wall = customtkinter.CTkLabel(
    master=wall_frame, justify=tkinter.LEFT, text='RUN WALL')
title_wall.pack(pady=5)

color_wall_user = customtkinter.CTkComboBox(master=wall_frame, values=['red', 'green', 'white', 'blue', 'black'])
color_wall_user.pack(side='right', padx=20)

wall_switch = customtkinter.CTkSwitch(
    master=wall_frame, text='Run Wall  | KEY 7', state=tkinter.NORMAL, onvalue=True, offvalue=False)
wall_switch.pack(side='left', padx=20)

# CHANMS
wall_frame_chams = customtkinter.CTkFrame(master=app)
wall_frame_chams.pack(pady=5, padx=70, fill="both", expand=True)

title_wall = customtkinter.CTkLabel(
    master=wall_frame_chams, justify=tkinter.LEFT, text='CHAMS CONFIG')
title_wall.pack(pady=12)

color_chams_user = customtkinter.CTkComboBox(master=wall_frame_chams, values=['red', 'green', 'white', 'blue', 'black'])
color_chams_user.pack(side='right', padx=20)

chams_switch = customtkinter.CTkSwitch(
    master=wall_frame_chams, text='Active', state=tkinter.NORMAL, onvalue=True, offvalue=False)
chams_switch.pack(side='left', padx=20, pady=10)

#radar
wall_frame_radar = customtkinter.CTkFrame(master=app)
wall_frame_radar.pack(pady=5, padx=70, fill="both", expand=True)
radat_switch = customtkinter.CTkSwitch(
    master=wall_frame_radar, text='Active Radar', state=tkinter.NORMAL, onvalue=True, offvalue=False)
radat_switch.pack(side='left', padx=20)


#############

#### AIM
aim_frame_radar = customtkinter.CTkFrame(master=app)
aim_frame_radar.pack(pady=10, padx=40, fill="both", expand=True)

title_aim = customtkinter.CTkLabel(
    master=aim_frame_radar, justify=tkinter.LEFT, text='RUN AIM')
title_aim.pack(pady=5, padx=10)


aim_switch = customtkinter.CTkSwitch(
    master=aim_frame_radar, text='Run Aim | KEY 9', state=tkinter.NORMAL, onvalue=True, offvalue=False)
aim_switch.pack(side='left', padx=20)

auto_shoot = customtkinter.CTkSwitch(
    master=aim_frame_radar, text='Auto shoot', state=tkinter.NORMAL, onvalue=True, offvalue=False)
auto_shoot.pack(side='right', padx=20)

aim_frame_radar_config = customtkinter.CTkFrame(master=app)
aim_frame_radar_config.pack(pady=5, padx=70, fill="both", expand=True)

title_aim = customtkinter.CTkLabel(
    master=aim_frame_radar_config, justify=tkinter.LEFT, text='AIM CONFIG')
title_aim.pack(pady=12, padx=5)

conf_aim_fov = customtkinter.CTkSwitch(
    master=aim_frame_radar_config, text='Fov', state=tkinter.NORMAL, onvalue=True, offvalue=False)
conf_aim_fov.pack(side='left', padx=5)
conf_aim_fov.select()

conf_spotted = customtkinter.CTkSwitch(
    master=aim_frame_radar_config, text='No fov walls', state=tkinter.NORMAL, onvalue=True, offvalue=False)
conf_spotted.pack(side='left', padx=5)
conf_spotted.select()

conf_smooth = customtkinter.CTkSwitch(
    master=aim_frame_radar_config, text='Smooth', state=tkinter.NORMAL, onvalue=True, offvalue=False)
conf_smooth.pack(side='left', padx=5)

aim_frame_radar_config_2 = customtkinter.CTkFrame(master=app)
aim_frame_radar_config_2.pack(pady=5, padx=70, fill="both", expand=True)

conf_baim = customtkinter.CTkSwitch(
    master=aim_frame_radar_config_2, text='Only body', state=tkinter.NORMAL, onvalue=True, offvalue=False)
conf_baim.pack(side='left', padx=5)

conf_aimtrcs = customtkinter.CTkSwitch(
    master=aim_frame_radar_config_2, text='Recoil Control System', state=tkinter.NORMAL, onvalue=True, offvalue=False)
conf_aimtrcs.pack(side='left', padx=5)

aim_frame_radar_config_3 = customtkinter.CTkFrame(master=app)
aim_frame_radar_config_3.pack(pady=5, padx=70, fill="both", expand=True)

aim_frame_radar_config_4 = customtkinter.CTkFrame(master=app)
aim_frame_radar_config_4.pack(pady=5, padx=70, fill="both", expand=True)


def change_random(value):
    from scripts.aim import Aim
    Aim.conf_random = value


def change_sens(value):
    from scripts.aim import Aim
    Aim.conf_sens = value

title_aim = customtkinter.CTkLabel(
    master=aim_frame_radar_config_3, justify=tkinter.LEFT, text='Random')
title_aim.pack(padx=10)

random_config = customtkinter.CTkSlider(master=aim_frame_radar_config_3, command=change_random ,from_=0, to=25)
random_config.pack(padx=10)
random_config.set(0)


title_aim = customtkinter.CTkLabel(
    master=aim_frame_radar_config_4, justify=tkinter.LEFT, text='Sensibility')
title_aim.pack(padx=10)

sens_config = customtkinter.CTkSlider(master=aim_frame_radar_config_4, command=change_sens ,from_=0, to=1.5)
sens_config.pack(padx=10)
sens_config.set(0)

#############


#### BHOP
bhop_frame_radar = customtkinter.CTkFrame(master=app)
bhop_frame_radar.pack(pady=10, padx=40, fill="both", expand=True)

title_bhop = customtkinter.CTkLabel(
    master=bhop_frame_radar, justify=tkinter.LEFT, text='RUN BHOP')
title_bhop.pack(pady=5, padx=10)

bhop_switch = customtkinter.CTkSwitch(
    master=bhop_frame_radar, text='Run Bhop | KEY 8', state=tkinter.NORMAL, onvalue=True, offvalue=False)
bhop_switch.pack(side='left', padx=20)
#############

### DLL LOADER

#### exit
exit_fram = customtkinter.CTkFrame(master=app)
exit_fram.pack(pady=5, padx=10, fill="both", expand=True)

button_1 = customtkinter.CTkButton(
    master=exit_fram, command=button_exit, text='EXIT')
button_1.pack(side='left', padx=145)


def load_dll_interface():
    import os
    os.system(os.path.abspath(r'injector.exe'))


dll_loader_frame = customtkinter.CTkFrame(master=app)
dll_loader_frame.pack(pady=5, fill="both", expand=True)

loader_button = customtkinter.CTkButton(
    master=dll_loader_frame, command=load_dll_interface, text='LOAD CUSTOM DLL')
loader_button.pack(pady=7)