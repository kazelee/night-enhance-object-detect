import os
import os.path
import shutil
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
# from main_ui import WinGUI

import main_logic
from main_logic import start

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    # ui: object
    # ui: WinGUI
    try:
        from main_ui import WinGUI
        ui: WinGUI
    except:
        ui: object

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    # def tmp_start_test(self, evt):
    #     flag = messagebox.askokcancel('提示', '确定测试运行吗？')
    #     if flag:
    #         self.start_test(evt)

    def start_test(self, evt):
        # flag = messagebox.askokcancel('提示', '确定测试运行吗？')
        # if not flag:
        #     return
        if not messagebox.askokcancel('提示', '要执行此操作吗？'):
        #     self.ui.tk_button_start_test.config(state=NORMAL)
            return

        if not self.ui.is_light_check.get() and not self.ui.is_night_check.get() and not self.ui.is_object_check.get():
            self.ui.hint_content.set("请至少选择参数设置中的一项！")
            # self.ui.tk_button_start_test.config(state=NORMAL)
            return

        if main_logic.is_input_dir_empty():
            self.ui.hint_content.set("input 文件夹中没有文件！")
            # self.ui.tk_button_start_test.config(state=NORMAL)
            return

        self.ui.hint_content.set("正在测试中……")
        self.ui.tk_label_text_hint.update()

        main_logic.is_light_effects_clear_chosen = self.ui.is_light_check.get()
        main_logic.is_night_enhancement_chosen = self.ui.is_night_check.get()
        main_logic.is_object_detection_chosen = self.ui.is_object_check.get()

        main_logic.has_night_enhancement_compare = self.ui.has_compare.get()
        '''main_logic中默认为False，仅当compare为True时考虑子选项'''
        if self.ui.has_compare.get():
            main_logic.has_object_detection_compare = self.ui.has_com_obj.get()
            main_logic.has_detect_origin_img = self.ui.has_com_ori.get()

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
        for node in self.ui.tree.selection():
            abspath = self.ui.nodes.get(node)
            if not abspath or os.path.isdir(abspath):
                continue
            print(f'try to open {abspath}')
            os.system(f'start explorer {abspath}')

    def delete_selected_files(self, evt):
        if not messagebox.askokcancel('提示', '确定要删除选择的文件吗？'):
        #     self.ui.tk_button_delete.config(state=NORMAL)
            return

        for node in self.ui.tree.selection():
            abspath = self.ui.nodes.get(node)
            if not abspath or os.path.isdir(abspath):
                continue
            os.remove(abspath)
        self.ui.tk_dir_tree(self.ui, self.ui.base_dir)

    def refresh_files(self, evt):
        self.ui.tk_dir_tree(self.ui, self.ui.base_dir)

    '''other buttons'''

    def open_cur_dir(self, evt):
        base = './' + self.ui.base_dir + '/'
        abspath = os.path.abspath(base)
        os.system(f'start explorer {abspath}')

    def switch_dir(self, evt):
        if self.ui.base_dir == 'input':
            self.ui.base_dir = 'output'
            self.ui.tk_dir_tree(self.ui, 'output')
        else:
            self.ui.base_dir = 'input'
            self.ui.tk_dir_tree(self.ui, 'input')

    def add_files(self, evt):
        file_paths = filedialog.askopenfilenames()
        for file_path in file_paths:
            main_logic.mycopyfile(file_path, './input/')

    def clear_files(self, evt):
        # tmp_flag = False
        if not messagebox.askokcancel('提示', f'确定清空{self.ui.base_dir}文件夹下的所有文件吗？'):
            # self.ui.tk_button_clear_file.configure(takefocus=False)
            # self.ui.tk_button_clear_file.state(['!selected'])
            # self.ui.tk_button_clear_file.configure(relief=RAISED)
            # self.ui.tk_button_clear_file.setvar('state', '!selected')
            # self.ui.tk_button_clear_file.update()
            # self.ui.tk_button_clear_file.configure(state='disabled')
            # self.ui.tk_button_clear_file.configure(state='normal')
            # tmp_flag = True
            return
        # if tmp_flag:
        base = './' + self.ui.base_dir + '/'
        shutil.rmtree(base)
        os.mkdir(base)

    def check_last_test(self, evt):
        dirs = os.listdir('./output/')
        dir_name = dirs[-1]
        abs_path = os.path.abspath(os.path.join('./output/', dir_name))
        os.system(f'start explorer {abs_path}')

    def check_last_argu(self, evt):
        dirs = os.listdir('./output/')
        dir_name = dirs[-1]
        argu_name = dir_name + '.log.txt'
        abs_path = os.path.abspath(os.path.join('./output/', dir_name, argu_name))
        print(f'try to open {abs_path}')
        os.system(f'start explorer {abs_path}')

    def open_cur_img(self, evt):
        if self.ui.cur_img_path == '':
            return
        os.system(f'start explorer {self.ui.cur_img_path}')

    def open_output_dir(self, evt):
        self.ui.base_dir = 'output'
        self.ui.tk_dir_tree(self.ui, 'output')
