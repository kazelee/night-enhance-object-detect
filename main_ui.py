"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import *
from tkinter.ttk import *
import os

import main_logic
from ui_controller import Controller

from tkinter.messagebox import showinfo
import windnd

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()

        self.hint_content = StringVar(value="请选择文件并设置参数后，点击测试按钮运行……")

        self.is_light_check = BooleanVar(value=True)
        self.is_night_check = BooleanVar(value=True)
        self.is_object_check = BooleanVar(value=True)

        self.light_imgsz = StringVar(value="1024")  # IntVar(value=1024)

        self.night_model = StringVar(value="LOL_v1")

        self.object_model = StringVar(value="yolov8n.pt")
        self.object_imgsz = StringVar(value="640")  # IntVar(value=640)
        self.object_conf = StringVar(value="0.5")  # DoubleVar(value=0.5)

        self.start_state = StringVar(value="开始测试")

        self.tk_select_box_choice_night_model = self.__tk_select_box_choice_night_model(self)
        self.tk_select_box_choice_model2 = self.__tk_select_box_choice_model2(self)
        self.tk_check_button_select_light = self.__tk_check_button_select_light(self)
        self.tk_list_box_box_listdir = self.__tk_list_box_box_listdir(self)
        self.tk_label_lb_listdir = self.__tk_label_lb_listdir(self)
        self.tk_label_lb_settings = self.__tk_label_lb_settings(self)
        self.tk_select_box_choice_size1 = self.__tk_select_box_choice_size1(self)
        self.tk_label_lb_size1 = self.__tk_label_lb_size1(self)
        self.tk_check_button_select_night = self.__tk_check_button_select_night(self)
        self.tk_label_lb_model1 = self.__tk_label_lb_model1(self)
        self.tk_check_button_select_object = self.__tk_check_button_select_object(self)
        self.tk_label_lb_model2 = self.__tk_label_lb_model2(self)
        self.tk_label_lb_size2 = self.__tk_label_lb_size2(self)
        self.tk_label_lb_conf = self.__tk_label_lb_conf(self)
        self.tk_button_start_test = self.__tk_button_start_test(self)
        self.tk_button_open_input = self.__tk_button_open_input(self)
        self.tk_button_add_file = self.__tk_button_add_file(self)
        self.tk_button_clear_file = self.__tk_button_clear_file(self)
        self.tk_button_open_last_test = self.__tk_button_open_last_test(self)
        self.tk_label_text_hint = self.__tk_label_text_hint(self)
        self.tk_button_open_output = self.__tk_button_open_output(self)
        self.tk_input_input_conf = self.__tk_input_input_conf(self)
        self.tk_input_input_size = self.__tk_input_input_size(self)

        # windnd.hook_dropfiles(self.tk_list_box_box_listdir, func=self.tk_listdir_update)

        self.tk_button_check = self.__tk_button_check(self)
        self.tk_button_delete = self.__tk_button_delete(self)
        self.tk_button_refresh = self.__tk_button_refresh(self)

    def __win(self):
        self.title("暗光增强车辆检测")
        # 设置窗口大小、居中
        width = 640
        height = 480
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_select_box_choice_night_model(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.night_model)
        cb['values'] = ("LOL_v1", "LOL_v2_real", "LOL_v2_synthetic", "SDSD_indoor", "SDSD_outdoor", "SID", "SMID", "FiveK")
        cb.place(x=500, y=200, width=120, height=30)
        return cb

    def __tk_select_box_choice_model2(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.object_model)
        cb['values'] = ("yolov8n.pt", "car_day_40k.pt")
        cb.place(x=500, y=280, width=120, height=30)
        return cb

    def __tk_check_button_select_light(self, parent):
        # is_light_check = self.is_light_check
        cb = Checkbutton(parent, text="强光分离", variable=parent.is_light_check)
        cb.place(x=420, y=80, width=80, height=30)
        return cb

    def __tk_list_box_box_listdir(self, parent):
        lb = Listbox(parent, selectmode="extended")

        lb.place(x=20, y=80, width=360, height=240)
        return lb

    def __tk_label_lb_listdir(self, parent):
        label = Label(parent, text="图片文件列表", anchor="center", )
        label.place(x=20, y=20, width=360, height=30)
        return label

    def __tk_label_lb_settings(self, parent):
        label = Label(parent, text="参数设置", anchor="center", )
        label.place(x=420, y=20, width=200, height=30)
        return label

    def __tk_select_box_choice_size1(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.light_imgsz)
        cb['values'] = ("1024", "512")
        cb.place(x=500, y=120, width=60, height=30)
        return cb

    def __tk_label_lb_size1(self, parent):
        label = Label(parent, text="尺寸:", anchor="center", )
        label.place(x=440, y=120, width=50, height=30)
        return label

    def __tk_check_button_select_night(self, parent):
        # is_night_check = self.is_night_check
        cb = Checkbutton(parent, text="弱光增强", variable=parent.is_night_check)
        cb.place(x=420, y=160, width=80, height=30)
        return cb

    def __tk_label_lb_model1(self, parent):
        label = Label(parent, text="模型:", anchor="center", )
        label.place(x=440, y=200, width=50, height=30)
        return label

    def __tk_check_button_select_object(self, parent):
        # is_object_check = self.is_object_check
        cb = Checkbutton(parent, text="目标检测", variable=parent.is_object_check)
        cb.place(x=420, y=240, width=80, height=30)
        return cb

    def __tk_label_lb_model2(self, parent):
        label = Label(parent, text="模型:", anchor="center", )
        label.place(x=440, y=280, width=50, height=30)
        return label

    def __tk_label_lb_size2(self, parent):
        label = Label(parent, text="尺寸:", anchor="center", )
        label.place(x=440, y=320, width=50, height=30)
        return label

    def __tk_label_lb_conf(self, parent):
        label = Label(parent, text="阈值:", anchor="center", )
        label.place(x=440, y=360, width=50, height=30)
        return label

    '''list dir buttons BEG'''
    def __tk_button_check(self, parent):
        btn = Button(parent, text="查看", takefocus=False, )
        btn.place(x=320, y=205, width=50, height=30)
        return btn

    def __tk_button_delete(self, parent):
        btn = Button(parent, text="删除", takefocus=False, )
        btn.place(x=320, y=245, width=50, height=30)
        return btn

    def __tk_button_refresh(self, parent):
        btn = Button(parent, text="刷新", takefocus=False, )
        btn.place(x=320, y=285, width=50, height=30)
        return btn

    '''list dir buttons END'''

    def __tk_button_start_test(self, parent):
        # btn = Button(parent, text="开始测试", takefocus=False, )
        btn = Button(parent, takefocus=False, textvariable=self.start_state)
        btn.place(x=420, y=420, width=200, height=40)
        return btn

    def __tk_button_open_input(self, parent):
        btn = Button(parent, text="打开输入文件夹", takefocus=False, )
        btn.place(x=280, y=340, width=100, height=30)
        return btn

    def __tk_button_add_file(self, parent):
        btn = Button(parent, text="新增文件", takefocus=False, )
        btn.place(x=20, y=340, width=100, height=30)
        return btn

    def __tk_button_clear_file(self, parent):
        btn = Button(parent, text="清空现有文件", takefocus=False, )
        btn.place(x=150, y=340, width=100, height=30)
        return btn

    def __tk_button_open_last_test(self, parent):
        btn = Button(parent, text="查看上一次运行结果", takefocus=False, )
        btn.place(x=20, y=430, width=160, height=30)
        return btn

    def __tk_label_text_hint(self, parent):
        label = Label(parent, text="标签", anchor="center", textvariable=self.hint_content)
        label.place(x=20, y=380, width=360, height=40)
        return label

    def __tk_button_open_output(self, parent):
        btn = Button(parent, text="打开输出文件夹", takefocus=False, )
        btn.place(x=220, y=430, width=160, height=30)
        return btn

    def __tk_input_input_conf(self, parent):
        ipt = Entry(parent, textvariable=self.object_conf)
        ipt.place(x=500, y=360, width=60, height=30)
        return ipt

    def __tk_input_input_size(self, parent):
        ipt = Entry(parent, textvariable=self.object_imgsz)
        ipt.place(x=500, y=320, width=120, height=30)
        return ipt

    def tk_listdir_update(self):
        self.tk_list_box_box_listdir.delete(0, END)
        input_path = './input/'
        files = os.listdir(input_path)
        for file in files:
            self.tk_list_box_box_listdir.insert(END, file)

    # def dragged_files(self, files):
    #     msg = '\n'.join((item.decode('gbk') for item in files))
    #     showinfo('您拖入的文件', msg)
    #     for file in files:
    #         main_logic.mycopyfile(file, main_logic.input_path)
    #     self.tk_listdir_update()


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
        self.tk_listdir_update()

    def __event_bind(self):
        self.tk_button_start_test.bind('<Button-1>', self.ctl.start_test)
        self.tk_button_open_input.bind('<Button-1>', self.ctl.open_input_dir)
        self.tk_button_add_file.bind('<Button-1>', self.ctl.add_files)
        self.tk_button_clear_file.bind('<Button-1>', self.ctl.clear_files)
        self.tk_button_open_last_test.bind('<Button-1>', self.ctl.check_last_test)
        self.tk_button_open_output.bind('<Button-1>', self.ctl.open_output_dir)

        self.tk_button_check.bind('<Button-1>', self.ctl.check_selected_files)
        self.tk_button_delete.bind('<Button-1>', self.ctl.delete_selected_files)
        self.tk_button_refresh.bind('<Button-1>', self.ctl.refresh_files)


def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    showinfo('您拖入的文件', msg)
    for file in files:
        main_logic.mycopyfile(file.decode('gbk'), main_logic.input_path)
    # tk_listdir_update()


if __name__ == "__main__":
    # win = WinGUI()
    ctl = Controller()
    win = Win(ctl)
    windnd.hook_dropfiles(win.tk_list_box_box_listdir, func=dragged_files)
    win.mainloop()
