from tkinter import *
# from tkinter.ttk import *
# import tkinter as tk


'''主界面窗口'''

root = Tk()
root.title("暗光增强车辆检测")
width = 640
height = 480
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(geometry)
root.resizable(width=False, height=False)


'''参数设置'''
is_light_check = IntVar()


'''check button'''

check_button_light = Checkbutton(root, text="强光分离", variable=is_light_check, onvalue=1, offvalue=0)
check_button_light.place(x=420, y=160, width=80, height=30)
# check_button_light.grid(column=3, row=0)

root.mainloop()
