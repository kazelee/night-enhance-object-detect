import os
import os.path
import shutil
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

# from main_ui import WinGUI

import main_logic
from main_logic import start

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    # ui: WinGUI

    def __init__(self):
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
        for node in self.ui.tree.selection():
            abspath = self.ui.nodes.get(node)
            if not abspath or os.path.isdir(abspath):
                continue
            print(f'try to open {abspath}')
            os.system(f'start explorer {abspath}')

    def delete_selected_files(self, evt):
        for node in self.ui.tree.selection():
            abspath = self.ui.nodes.get(node)
            if not abspath or os.path.isdir(abspath):
                continue
            os.remove(abspath)
        self.ui.tk_dir_tree(self.ui, self.ui.base_dir)

    def refresh_files(self, evt):
        self.ui.tk_dir_tree(self.ui, self.ui.base_dir)
        # self.ui.tk_listdir_update()

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
        # self.ui.base_dir = 'input'
        # self.ui.tk_dir_tree(self.ui, 'input')
        # abs_path = os.path.abspath('./input/')
        # os.system(f'start explorer {abs_path}')

    def add_files(self, evt):
        file_paths = filedialog.askopenfilenames()
        for file_path in file_paths:
            main_logic.mycopyfile(file_path, './input/')

    def clear_files(self, evt):
        shutil.rmtree('./input/')
        os.mkdir('./input/')

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
        # abs_path = os.path.abspath('./output/')
        # os.system(f'start explorer {abs_path}')

    # def open_or_show(self, evt):
    #     lb = self.ui.tk_list_box_box_listdir
    #     file_name = lb.get(lb.curselection())
    #     file_path = os.path.join('./input/', file_name)
    #     abs_path = os.path.abspath(file_path)
    #     if os.path.isfile(abs_path):
    #         try:
    #             img_open = Image.open(abs_path)
    #             img_png = ImageTk.PhotoImage(img_open)
                # self.ui.tk_canvas.create_image(img_png)
                # label_img = Label(self.ui.tk_canvas, image=img_png)
                # label_img.pack(fill='both', expand=True)
                # self.ui.label_img = Label(self.ui, image=img_png)
                # self.ui.label_img.place(x=280, y=80, width=720, height=400)
        #     except:
        #         print('img!!!')
        # print(f'try to open {file_path}')
        # os.system(f'start explorer {abs_path}')
