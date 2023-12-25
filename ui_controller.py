"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
import os
import os.path
import shutil
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# from main_ui import WinGUI
#
import main_logic
from main_logic import start

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    # ui: WinGUI

    def __init__(self):
        # self.last_time = ""
        # self.in_progress = False
        # self.end_time = ""
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def start_test(self, evt):
        # if self.ui.start_state.get() != "开始测试":
        #     # exit(1)
        #     raise SystemExit(1)

        if not self.ui.is_light_check.get() and not self.ui.is_night_check.get() and not self.ui.is_object_check.get():
            self.ui.hint_content.set("请至少选择参数设置中的一项！")
            # print("<Button-1>事件未处理:", evt)
            return

        if main_logic.is_input_dir_empty():
            self.ui.hint_content.set("input 文件夹中没有文件！")
            return

        # self.ui.start_state.set("强制停止")
        # self.ui.tk_button_start_test.update()

        # self.ui.tk_label_text_hint.setvar("正在测试中……")
        self.ui.hint_content.set("正在测试中……")
        self.ui.tk_label_text_hint.update()
        # self.ui.tk_label_text_hint.setvar(self.ui.hint_content.get())
        # self.ui.tk_label_text_hint.waitvar()
        # self.ui.tk_label_text_hint.wait_variable(self.ui.hint_content)
        # time.sleep(0.1)
        # if int(self.ui.object_imgsz) % 32 != 0:
        #     self.ui.object_imgsz = int(self.ui.object_imgsz) // 32 * 32 + 32

        main_logic.is_light_effects_clear_chosen = self.ui.is_light_check.get()
        main_logic.is_night_enhancement_chosen = self.ui.is_night_check.get()
        main_logic.is_object_detection_chosen = self.ui.is_object_check.get()

        main_logic.light_imgsz = int(self.ui.light_imgsz.get())
        # main_logic.detect_imgsz = int(self.ui.object_imgsz.get())
        new_light_imgsz = int(self.ui.object_imgsz.get()) // 32 * 32 + 32 if int(self.ui.object_imgsz.get()) % 32 != 0 \
            else int(self.ui.object_imgsz.get())
        main_logic.detect_imgsz = new_light_imgsz

        main_logic.enhance_model = self.ui.night_model.get()
        main_logic.detect_model_name = self.ui.object_model.get()

        main_logic.detect_conf = float(self.ui.object_conf.get())

        main_logic.night_enhancement_result_path = './results/Test/RetinexFormer_Test/' + main_logic.enhance_model + '/'

        start()

        self.ui.hint_content.set("测试完成！")
        # self.ui.start_state.set("开始测试")

    def check_selected_files(self, evt):
        for index in self.ui.tk_list_box_box_listdir.curselection():
            # file_name = self.ui.tk_list_box_box_listdir.itemcget(index, 'background')
            file_name = self.ui.tk_list_box_box_listdir.get(index)
            file_path = os.path.join('./input/', file_name)
            abs_path = os.path.abspath(file_path)
            print(f'try to open {file_path}')
            os.system(f'start explorer {abs_path}')

    def delete_selected_files(self, evt):
        for index in self.ui.tk_list_box_box_listdir.curselection():
            # file_name = self.ui.tk_list_box_box_listdir.itemcget(index)
            file_name = self.ui.tk_list_box_box_listdir.get(index)
            file_path = os.path.join('./input/', file_name)
            # shutil.rmtree(file_path)
            os.remove(file_path)
        self.ui.tk_listdir_update()

    def refresh_files(self, evt):
        self.ui.tk_listdir_update()

    '''other buttons'''

    def open_input_dir(self, evt):
        abs_path = os.path.abspath('./input/')
        os.system(f'start explorer {abs_path}')
        # print("<Button-1>事件未处理:", evt)

    def add_files(self, evt):
        file_paths = filedialog.askopenfilenames()
        for file_path in file_paths:
            main_logic.mycopyfile(file_path, './input/')
        # print("<Button-1>事件未处理:", evt)

    def clear_files(self, evt):
        shutil.rmtree('./input/')
        os.mkdir('./input/')
        # print("<Button-1>事件未处理:", evt)

    def check_last_test(self, evt):
        # output_dirs = [path for path in os.listdir('./output/') if os.path.isdir(path)]
        # print(os.listdir('./output/'))
        # print(output_dirs)
        # abs_path = os.path.abspath(os.path.join('./output/', output_dirs[-1]))
        dirs = os.listdir('./output/')
        dir_name = dirs[-1]
        abs_path = os.path.abspath(os.path.join('./output/', dir_name))
        os.system(f'start explorer {abs_path}')
        # print("<Button-1>事件未处理:", evt)

    def open_output_dir(self, evt):
        abs_path = os.path.abspath('./output/')
        os.system(f'start explorer {abs_path}')
        # print("<Button-1>事件未处理:", evt)
