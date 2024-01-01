from tkinter import *
from tkinter.ttk import *
import os

import PIL

import main_logic
from ui_controller import Controller

from tkinter.messagebox import showinfo
import windnd

import tkinter.font as tkFont
# import ctypes
from PIL import Image, ImageTk

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()

        self.hint_content = StringVar(value="请选择文件并设置参数后，点击测试按钮运行……")

        self.is_light_check = BooleanVar(value=True)
        self.is_night_check = BooleanVar(value=True)
        self.is_object_check = BooleanVar(value=True)

        self.base_dir = 'input'
        self.cur_img_path = ''

        self.light_imgsz = StringVar(value="1024")  # IntVar(value=1024)
        self.night_model = StringVar(value="LOL_v1")
        self.object_model = StringVar(value="yolov8n.pt")
        self.object_imgsz = StringVar(value="640")  # IntVar(value=640)
        self.object_conf = StringVar(value="0.5")  # DoubleVar(value=0.5)
        self.start_state = StringVar(value="开始测试")

        self.myFont = tkFont.Font(family='SimHei', size=20)
        self.labelFont = tkFont.Font(family='SimHei', size=12)
        # self.s_label = Style()
        # self.s_label.configure('my.TLabel', font=('SimHei', 15))
        self.s_checkbutton = Style()
        self.s_checkbutton.configure('my.TCheckbutton', font=('SimHei', 12))
        self.s_button = Style()
        self.s_button.configure('small.TButton', font=('SimHei', 12))
        self.s_treeview = Style()
        self.s_treeview.configure('my.Treeview', font=('微软雅黑', 10))

        # self.TB = Style()
        # self.TB.configure('my.TButton', font=('SimHei', 15))
        # self.STB = Style()
        # self.STB.configure('my.LButton', font=('SimHei', 10))

        # self.tk_notebook_widget = self.__tk_notebook_widget(self)
        # self.style = Style()
        # self.style.theme_create("MyStyle", parent="alt", settings={
        #     "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
        #     "TNotebook.Tab": {"configure": {"padding": [100, 100]}, }})
        # self.style.theme_use("MyStyle")
        # self.nodes = dict()
        # self.tk_dir_tree = self.__tk_dir_tree(self)
        self.tk_dir_tree(self)

        self.tk_select_box_choice_night_model = self.__tk_select_box_choice_night_model(self)
        self.tk_select_box_choice_model2 = self.__tk_select_box_choice_model2(self)
        self.tk_check_button_select_light = self.__tk_check_button_select_light(self)
        # self.tk_list_box_box_listdir = self.__tk_list_box_box_listdir(self)
        self.tk_label_canvas = self.__tk_label_canvas(self)
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
        self.tk_button_switch_dir = self.__tk_button_switch_dir(self)
        self.tk_button_add_file = self.__tk_button_add_file(self)
        self.tk_button_clear_file = self.__tk_button_clear_file(self)
        self.tk_button_open_last_test = self.__tk_button_open_last_test(self)
        self.tk_label_text_hint = self.__tk_label_text_hint(self)
        self.tk_button_open_cur_dir = self.__tk_button_open_cur_dir(self)
        self.tk_input_input_conf = self.__tk_input_input_conf(self)
        self.tk_input_input_size = self.__tk_input_input_size(self)
        self.tk_button_open_last_argu = self.__tk_button_open_last_argu(self)
        self.tk_button_open_cur_img = self.__tk_button_open_cur_img(self)

        self.tk_button_check = self.__tk_button_check(self)
        self.tk_button_delete = self.__tk_button_delete(self)
        self.tk_button_refresh = self.__tk_button_refresh(self)

        # self.label_img = Label()
        self.tk_canvas = self.__tk_canvas(self)
        # self.tk_label_img = self.__tk_label_img(self)

    def __win(self):
        self.title("暗光增强车辆检测")
        # 设置窗口大小、居中
        width = 1280
        height = 720
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

    # def __tk_notebook_widget(self, parent):
    #     nb = Notebook(parent)
    #     # nb.place(x=0, y=0, width=1280, height=720)
    #     nb.pack(expand=True, fill='both')
    #     nb.Frame1 = Frame(nb)
    #     nb.Frame1.configure(height='200', width='200')
    #     nb.Frame1.pack(side='left')
    #     nb.add(nb.Frame1, text='Tab1')
    #     return nb

    '''ui_tree BEG'''
    def tk_dir_tree(self, parent, root='input'):
        base_dir = f'./{root}/'
        self.nodes = dict()
        # frame = Frame(parent, width=240, height=400)
        # frame.pack()
        # frame.place(x=20, y=80)
        # frame.place(x=20, y=80, width=240, height=400)
        self.tree = Treeview(parent, style='my.Treeview')
        self.tree.place(x=20, y=80, width=240, height=400)
        self.create_bar(parent, self.tree, True, False, 20, 80, 240, 400, 1280, 720)
        # self.tree.place(x=20, y=80, width=240, height=400)  # new added
        # self.tree.place(x=20, y=80)
        # ysb = Scrollbar(frame, orient='vertical', command=self.tree.yview)
        # xsb = Scrollbar(frame, orient='horizontal', command=self.tree.xview)
        # self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)

        #
        # self.tree.grid()
        # ysb.grid(row=0, column=1, sticky='ns')
        # xsb.grid(row=1, column=0, sticky='ew')
        # frame.grid()

        abspath = os.path.abspath(base_dir)
        self.tree.heading('#0', text=abspath, anchor='w')
        # self.insert_node('', abspath, abspath)
        self.insert_node('', root, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        self.tree.bind('<Double-Button-1>', self.open_file)
        # self.tree.place(x=20, y=80)

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        self.nodes[node] = abspath
        if os.path.isdir(abspath):
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.get(node)
        if abspath and os.path.isfile(abspath):
            return
        abspath = self.nodes.pop(node, None)
        # abspath = self.nodes.get(node)
        if abspath:
            if os.path.isdir(abspath):
                self.tree.delete(self.tree.get_children(node))
                for p in os.listdir(abspath):
                    self.insert_node(node, p, os.path.join(abspath, p))
        # else:
        #     print('bad')  # print when close

    def open_file(self, event):
        node = self.tree.focus()
        abspath = self.nodes.get(node)
        if abspath and os.path.isdir(abspath):
            return

        # abspath = self.nodes.pop(node, None)
        if abspath and os.path.isfile(abspath):  # 对图片专门处理
            global img_png
            try:
                self.cur_img_path = abspath
                img_open = Image.open(abspath)
                img_open = img_open.resize((720, 400))
                img_png = ImageTk.PhotoImage(img_open)
                self.label_img = Label(self, image=img_png)
                self.label_img.place(x=280, y=80, width=720, height=400)
            except PIL.UnidentifiedImageError:
                print('文件必须是图片')

        # self.tree.delete(self.tree.get_children(node))
        # for p in os.listdir(abspath):
        #     self.insert_node(node, p, os.path.join(abspath, p))
        # else:
        #     print('bad!')

    '''ui_tree END'''

    def __tk_canvas(self, parent):
        canvas = Canvas(parent, bg='#FFF')
        canvas.place(x=280, y=80, width=720, height=400)
        return canvas

    # def __tk_label_img(self, parent):
    #     label = Label(parent)
    #     label.place(x=280, y=80, width=720, height=400)
    #     return label

    def __tk_label_canvas(self, parent):
        label = Label(parent, text="图片展示", anchor="center", font=self.myFont)
        label.place(x=520, y=20, width=240, height=40)
        return label

    def __tk_select_box_choice_night_model(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.night_model)
        cb['values'] = ("LOL_v1", "LOL_v2_real", "LOL_v2_synthetic", "SDSD_indoor", "SDSD_outdoor", "SID", "SMID",
                        "FiveK")
        cb.place(x=1120, y=200, width=120, height=30)
        return cb

    def __tk_select_box_choice_model2(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.object_model)
        cb['values'] = ("yolov8n.pt", "bdd_day40k.pt", "bdd_day40k20c.pt", "bdd_day20.pt",
                        "bdd_day512.pt", "bdd_night512.pt")
        cb.place(x=1120, y=280, width=120, height=30)
        return cb

    def __tk_check_button_select_light(self, parent):
        cb = Checkbutton(parent, text="强光分离", variable=parent.is_light_check, style='my.TCheckbutton')
        cb.place(x=1020, y=80, width=120, height=30)
        return cb

    def __tk_list_box_box_listdir(self, parent):
        lb = Listbox(parent, selectmode="extended", font=tkFont.Font(family='微软雅黑', size=10))

        lb.place(x=20, y=80, width=240, height=400)
        self.create_bar(parent, lb, True, False, 20, 80, 240, 400, 1280, 720)
        return lb

    def __tk_label_lb_listdir(self, parent):
        label = Label(parent, text="文件列表", anchor="center", font=self.myFont)
        label.place(x=20, y=20, width=240, height=40)
        return label

    def __tk_label_lb_settings(self, parent):
        label = Label(parent, text="参数设置", anchor="center", font=self.myFont)
        label.place(x=1020, y=20, width=240, height=40)
        return label

    def __tk_select_box_choice_size1(self, parent):
        cb = Combobox(parent, state="readonly", textvariable=self.light_imgsz)
        cb['values'] = ("1024", "512")
        cb.place(x=1120, y=120, width=60, height=30)
        return cb

    def __tk_label_lb_size1(self, parent):
        label = Label(parent, text="尺寸:", anchor="center", font=self.labelFont)
        label.place(x=1040, y=120, width=50, height=30)
        return label

    def __tk_check_button_select_night(self, parent):
        cb = Checkbutton(parent, text="弱光增强", variable=parent.is_night_check, style='my.TCheckbutton')
        cb.place(x=1020, y=160, width=120, height=30)
        return cb

    def __tk_label_lb_model1(self, parent):
        label = Label(parent, text="模型:", anchor="center", font=self.labelFont)
        label.place(x=1040, y=200, width=50, height=30)
        return label

    def __tk_check_button_select_object(self, parent):
        # is_object_check = self.is_object_check
        cb = Checkbutton(parent, text="目标检测", variable=parent.is_object_check, style='my.TCheckbutton')
        cb.place(x=1020, y=240, width=120, height=30)
        return cb

    def __tk_label_lb_model2(self, parent):
        label = Label(parent, text="模型:", anchor="center", font=self.labelFont)
        label.place(x=1040, y=280, width=50, height=30)
        return label

    def __tk_label_lb_size2(self, parent):
        label = Label(parent, text="尺寸:", anchor="center", font=self.labelFont)
        label.place(x=1040, y=320, width=50, height=30)
        return label

    def __tk_label_lb_conf(self, parent):
        label = Label(parent, text="阈值:", anchor="center", font=self.labelFont)
        label.place(x=1040, y=360, width=50, height=30)
        return label

    '''list dir buttons BEG'''
    def __tk_button_check(self, parent):
        # s = Style()
        # s.configure('small.TButton', font=('SimHei', 12))
        btn = Button(parent, text="使用默认应用打开", takefocus=False, style='small.TButton')
        btn.place(x=20, y=550, width=155, height=40)
        return btn

    def __tk_button_delete(self, parent):
        btn = Button(parent, text="删除", takefocus=False, style='small.TButton')
        btn.place(x=190, y=500, width=70, height=40)
        return btn

    def __tk_button_refresh(self, parent):
        btn = Button(parent, text="刷新", takefocus=False, style='small.TButton')
        btn.place(x=105, y=500, width=70, height=40)
        return btn

    '''list dir buttons END'''

    def __tk_button_start_test(self, parent):
        s = Style()
        s.configure('my.TButton', font=('SimHei', 15))
        btn = Button(parent, takefocus=False, textvariable=self.start_state, style='my.TButton')
        btn.place(x=1020, y=620, width=240, height=80)
        return btn

    def __tk_button_switch_dir(self, parent):
        btn = Button(parent, text="切换输入/输出文件夹", takefocus=False, style='small.TButton')
        btn.place(x=20, y=600, width=240, height=40)
        return btn

    def __tk_button_add_file(self, parent):
        btn = Button(parent, text="添加", takefocus=False, style='small.TButton')
        btn.place(x=20, y=500, width=70, height=40)
        return btn

    def __tk_button_clear_file(self, parent):
        btn = Button(parent, text="清空", takefocus=False, style='small.TButton')
        btn.place(x=190, y=550, width=70, height=40)
        return btn

    def __tk_button_open_last_test(self, parent):
        btn = Button(parent, text="查看上一次运行结果", takefocus=False, style='small.TButton')
        btn.place(x=280, y=500, width=230, height=40)
        return btn

    def __tk_button_open_last_argu(self, parent):
        btn = Button(parent, text="查看上一次运行参数", takefocus=False, style='small.TButton')
        btn.place(x=525, y=500, width=230, height=40)
        return btn

    def __tk_button_open_cur_img(self, parent):
        btn = Button(parent, text="查看当前图片大图", takefocus=False, style='small.TButton')
        btn.place(x=770, y=500, width=230, height=40)
        return btn


    def __tk_label_text_hint(self, parent):
        label = Label(parent, text="标签", anchor="center", textvariable=self.hint_content, font=self.labelFont)
        label.place(x=280, y=550, width=720, height=150)
        return label

    def __tk_button_open_cur_dir(self, parent):
        btn = Button(parent, text="在文件管理器中显示", takefocus=False, style='small.TButton')
        btn.place(x=20, y=650, width=240, height=40)
        return btn

    def __tk_input_input_conf(self, parent):
        ipt = Entry(parent, textvariable=self.object_conf)
        ipt.place(x=1120, y=360, width=60, height=30)
        return ipt

    def __tk_input_input_size(self, parent):
        ipt = Entry(parent, textvariable=self.object_imgsz)
        ipt.place(x=1120, y=320, width=120, height=30)
        return ipt

    def tk_listdir_update(self):
        self.tk_list_box_box_listdir.delete(0, END)
        input_path = './input/'
        files = os.listdir(input_path)
        for file in files:
            self.tk_list_box_box_listdir.insert(END, file)

    # def open_or_show(self, evt):
    #     global img_png  # 函数运行结束就被回收了，会显示的是空白
    #     # filename = self.tree.selection_get()
    #     filename = self.tree.item(self.tree.focus())['text']
    #     # filename = self.tk_list_box_box_listdir.selection_get()
    #     # filename = self.tk_list_box_box_listdir.get(index)
    #     filepath = os.path.join('./input/' + filename)
    #     abs_path = os.path.abspath(filepath)
    #     img_open = Image.open(abs_path)
    #     img_open = img_open.resize((720, 400))  # 规定图片大小
    #     img_png = ImageTk.PhotoImage(img_open)
    #     # self.label_img = Label(self.tk_label_canvas, image=img_png)
    #     # self.label_img.pack()
    #     self.label_img = Label(self, image=img_png)
    #     self.label_img.place(x=280, y=80, width=720, height=400)
    #     # self.label_img.configure(width=400, height=400)
    #     # self.label_img.config(width=400, height=400)


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
        # self.tk_listdir_update()

    def __event_bind(self):
        self.tk_button_start_test.bind('<Button-1>', self.ctl.start_test)
        self.tk_button_switch_dir.bind('<Button-1>', self.ctl.switch_dir)
        self.tk_button_add_file.bind('<Button-1>', self.ctl.add_files)
        self.tk_button_clear_file.bind('<Button-1>', self.ctl.clear_files)
        self.tk_button_open_last_test.bind('<Button-1>', self.ctl.check_last_test)
        self.tk_button_open_cur_dir.bind('<Button-1>', self.ctl.open_cur_dir)
        self.tk_button_open_last_argu.bind('<Button-1>', self.ctl.check_last_argu)
        self.tk_button_open_cur_img.bind('<Button-1>', self.ctl.open_cur_img)

        self.tk_button_check.bind('<Button-1>', self.ctl.check_selected_files)
        self.tk_button_delete.bind('<Button-1>', self.ctl.delete_selected_files)
        self.tk_button_refresh.bind('<Button-1>', self.ctl.refresh_files)
        # self.tree.bind('<Double-Button-1>', self.open_or_show)
        # self.tk_list_box_box_listdir.bind('<Double-Button-1>', self.ctl.open_or_show)
        # self.tk_list_box_box_listdir.bind('<Double-Button-1>', self.open_or_show)


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
    # # 告诉操作系统使用程序自身的dpi适配
    # ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # # 获取屏幕的缩放因子
    # ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # # 设置程序缩放
    # win.tk.call('tk', 'scaling', ScaleFactor / 75)
    # windnd.hook_dropfiles(win.tk_list_box_box_listdir, func=dragged_files)
    windnd.hook_dropfiles(win.tree, func=dragged_files)
    win.mainloop()
