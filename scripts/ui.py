import tkinter
import customtkinter

from scripts.states import AppStates

"""
made by zabbix https://github.com/zabbix-byte
"""

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x580")
app.title("zt cs go cheat")
app.resizable(0, 0)
app.attributes('-topmost', True)

app.iconbitmap("ico.ico")


def button_exit():
    AppStates.APP_RUNNING = False
    app.quit()



app.protocol("WM_DELETE_WINDOW", button_exit)
app.update()

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

title = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.LEFT, text='ZT - CHEAT')
title.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(
    master=frame_1, command=button_exit, text='EXIT')
button_1.pack(pady=12, padx=10)

title_wall = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.LEFT, text='WALL CONFIG')
title_wall.pack(pady=12, padx=10)

wall_switch = customtkinter.CTkSwitch(
    master=frame_1, text='Active Wall', state=tkinter.NORMAL, onvalue=True, offvalue=False)
wall_switch.pack(pady=12, padx=10)

title_aim = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.LEFT, text='AIM CONFIG')
title_aim.pack(pady=12, padx=10)

aim_switch = customtkinter.CTkSwitch(
    master=frame_1, text='Active AIM', state=tkinter.NORMAL, onvalue=True, offvalue=False)
aim_switch.pack(pady=12, padx=10)

title_bhop = customtkinter.CTkLabel(
    master=frame_1, justify=tkinter.LEFT, text='AIM CONFIG')
title_bhop.pack(pady=12, padx=10)

bhop_switch = customtkinter.CTkSwitch(
    master=frame_1, text='Active BHOP', state=tkinter.NORMAL, onvalue=True, offvalue=False)
bhop_switch.pack(pady=12, padx=10)
