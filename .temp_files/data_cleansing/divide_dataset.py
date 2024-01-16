import json

# srcfile 需要复制、移动的文件   
# dstpath 目的地址

import os
import shutil
from glob import glob


def mycopyfile(srcfile, dstpath):  # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        # print ("copy %s -> %s"%(srcfile, dstpath + fname))


with open("all_img_night.json", 'r', encoding='utf-8') as f:
    all_data = json.load(f)

target_dir = './dataset/'
# num = len(all_data)
# num = 10000

# for i in range(num):
#     print(f'{i + 1} / {num}')
#     img_dir = './all/' + all_data[i]["name"]
#     if i < num * 0.8:
#         dis_dir = target_dir + 'images/train/'
#         label_dir = target_dir + 'labels/train/' + all_data[i]["name"][:-3] + 'txt'
#     elif i < num * 0.9:
#         dis_dir = target_dir + 'images/val/'
#         label_dir = target_dir + 'labels/val/' + all_data[i]["name"][:-3] + 'txt'
#     else:
#         dis_dir = target_dir + 'images/test/'
#         label_dir = target_dir + 'labels/test/' + all_data[i]["name"][:-3] + 'txt'

# PART BEG: for val
for i in range(10000, 11000):
    print(f'{i + 1 - 10000} / 1000')
    img_dir = './all/' + all_data[i]["name"]

    dis_dir = target_dir + 'images/val/'
    label_dir = target_dir + 'labels/val/' + all_data[i]["name"][:-3] + 'txt'
    # PART END: for val

    mycopyfile(img_dir, dis_dir)

    dirname = os.path.dirname(label_dir)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(label_dir, 'w', encoding='utf-8') as f:
        for label in all_data[i]["labels"]:
            if label["category"] == "car":
                class_id = 0
            elif label["category"] == "bus":
                class_id = 1
            elif label["category"] == "truck":
                class_id = 2
            else:
                continue

            box_width = (label["box2d"]["x2"] - label["box2d"]["x1"]) / 1280.
            box_height = (label["box2d"]["y2"] - label["box2d"]["y1"]) / 720.
            center_x = (label["box2d"]["x1"] / 1280. + label["box2d"]["x2"] / 1280.) / 2.
            center_y = (label["box2d"]["y1"] / 720. + label["box2d"]["y2"] / 720.) / 2.

            f.write("{0} {1} {2} {3} {4}\n".format(class_id, center_x, center_y, box_width, box_height))
