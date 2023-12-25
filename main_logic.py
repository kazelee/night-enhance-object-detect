import os
import shutil
import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["figure.autolayout"] = True

import light_effects_clear
import night_enhancement
import object_detection
# import image_gather

'''settings'''

is_light_effects_clear_chosen = True
is_night_enhancement_chosen = True
is_object_detection_chosen = True

light_imgsz = 1024

enhance_model = 'SID'

detect_model_name = 'car_day_40k.pt'
detect_imgsz = 640
detect_conf = 0.5

'''const path'''

input_path = './input/'
light_effect_path = './ClearLightEffects/light-effects/'
light_effect_result_path = './ClearLightEffects/output/'

night_enhancement_path = './data/Test/input/'
night_enhancement_result_root = './results/Test/RetinexFormer_Test/'
night_enhancement_result_path = './results/Test/RetinexFormer_Test/' + enhance_model + '/'

object_detection_path = './object_test/'
object_detection_result_path = './runs/detect/predict/'
output_path = './output/'


def is_input_dir_empty() -> bool:
    in_files = os.listdir(input_path)
    return len(in_files) == 0


def mycopyfile(srcfile, dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


# def mymovefile(srcfile, dstpath):
#     mycopyfile(srcfile, dstpath)
#     os.remove(srcfile)

def move_file(src_path, dst_path, file):
    # print('from : ',src_path)
    # print('to : ',dst_path)
    try:
        # cmd = 'chmod -R +x ' + src_path
        # os.popen(cmd)
        f_src = os.path.join(src_path, file)
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        f_dst = os.path.join(dst_path, file)
        shutil.move(f_src, f_dst)
    except Exception as e:
        print(f'move_file ERROR: {e}')
        # traceback.print_exc()


def clear(clear_input=False, clear_detect=False):
    if clear_input:
        shutil.rmtree(input_path)
        os.mkdir(input_path)
    shutil.rmtree(light_effect_path)
    os.mkdir(light_effect_path)
    shutil.rmtree(light_effect_result_path)
    os.mkdir(light_effect_result_path)
    shutil.rmtree(night_enhancement_path)
    os.mkdir(night_enhancement_path)
    # shutil.rmtree(night_enhancement_result_path)
    # os.mkdir(night_enhancement_result_path)
    shutil.rmtree(night_enhancement_result_root)
    os.mkdir(night_enhancement_result_root)
    shutil.rmtree(object_detection_path)
    os.mkdir(object_detection_path)
    if clear_detect:
        if os.path.exists(object_detection_result_path):
            shutil.rmtree(object_detection_result_path)
        # os.mkdir(object_detection_result_path)


def start(input_included=True):
    clear(clear_detect=True)
    if not is_night_enhancement_chosen and not is_object_detection_chosen and not is_light_effects_clear_chosen:
        print("At least choose one!")
        return

    nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    output_time = output_path + nowTime + '/'
    input_files = os.listdir(input_path)

    if input_included:
        output_input = output_time + 'input/'
        os.makedirs(output_input)
        for file in input_files:
            mycopyfile(os.path.join(input_path, file), os.path.join(output_input))

    if is_light_effects_clear_chosen:
        img_types = set()
        for file in input_files:
            '''获取文件后缀名：名称按点split，取最后一段'''
            img_types.add(file.split('.')[-1])
            mycopyfile(os.path.join(input_path, file), os.path.join(light_effect_path))
        for t in img_types:
            light_effects_clear.main(imgsz=light_imgsz, img_type='.'+t)
        '''将处理过的文件复制到output中'''
        new_dir = output_time + 'light_effects_clear/'
        os.makedirs(new_dir)
        result_files = os.listdir(light_effect_result_path)
        for file in result_files:
            mycopyfile(os.path.join(light_effect_result_path, file), os.path.join(new_dir))
    else:
        for file in input_files:
            mycopyfile(os.path.join(input_path, file), os.path.join(light_effect_result_path))

    light_effects_result_files = os.listdir(light_effect_result_path)

    if is_night_enhancement_chosen:
        for file in light_effects_result_files:
            mycopyfile(os.path.join(light_effect_result_path, file), os.path.join(night_enhancement_path))
            # move_file(light_effect_result_path, night_enhancement_path, file)
        night_enhancement.main(model=enhance_model)
        '''将处理过的文件复制到output中'''
        new_dir = output_time + 'night_enhanced/'
        os.makedirs(new_dir)
        result_files = os.listdir(night_enhancement_result_path)
        for file in result_files:
            mycopyfile(os.path.join(night_enhancement_result_path, file), os.path.join(new_dir))
    else:
        for file in light_effects_result_files:
            mycopyfile(os.path.join(light_effect_result_path, file), os.path.join(night_enhancement_result_path))

    night_enhancement_result_files = os.listdir(night_enhancement_result_path)

    if is_object_detection_chosen:
        for file in night_enhancement_result_files:
            mycopyfile(os.path.join(night_enhancement_result_path, file), os.path.join(object_detection_path))
        object_detection.main(model_name=detect_model_name, imgsz=detect_imgsz, conf=detect_conf)
        '''将处理过的文件复制到output中'''
        new_dir = output_time + 'object_detected/'
        os.makedirs(new_dir)
        result_files = os.listdir(object_detection_result_path)
        for file in result_files:
            mycopyfile(os.path.join(object_detection_result_path, file), os.path.join(new_dir))
    # else:
    #     for file in night_enhancement_result_files:
    #         mycopyfile(os.path.join(night_enhancement_result_path, file), os.path.join(object_detection_result_path))

    # for file in input_files:
    #     i = 1
    #     # titles = ['原图像']
    #     # plt.figure(figsize=(10,10))
    #     plt.figure(figsize=(12.8, 9.6))  # (6.4, 4.8 by default)
    #     plt.tight_layout()
    #     plt.subplot(2,2,1)
    #     plt.imshow(mpimg.imread(os.path.join(input_path, file)))
    #     plt.title('原图像')
    #     plt.xticks([]), plt.yticks([])
    #     if is_light_effects_clear_chosen:
    #         i += 1
    #         # titles.append('强光分离后')
    #         plt.subplot(2,2,i)
    #         plt.imshow(mpimg.imread(os.path.join(light_effect_result_path, file[:-3] + 'png')))
    #         plt.title('强光分离后')
    #         plt.xticks([]), plt.yticks([])
    #     if is_night_enhancement_chosen:
    #         i += 1
    #         # titles.append('暗光增强后')
    #         plt.subplot(2,2,i)
    #         plt.imshow(mpimg.imread(os.path.join(night_enhancement_result_path, file[:-3] + 'png')))
    #         plt.title('弱光分离后')
    #         plt.xticks([]), plt.yticks([])
    #     if is_object_detection_chosen:
    #         i += 1
    #         # titles.append('目标检测结果')
    #         plt.subplot(2,2,i)
    #         plt.imshow(mpimg.imread(os.path.join(object_detection_result_path, file[:-3] + 'png')))
    #         plt.title('目标检测结果')
    #         plt.xticks([]), plt.yticks([])
    #     # plt.title(titles)
    #     # plt.imsave(os.path.join(output_time, file))
    #     plt.savefig(os.path.join(output_time, file[:-3] + 'png'))

    object_detection_result_files = os.listdir(object_detection_result_path)

    rows = 0
    if is_light_effects_clear_chosen:
        rows += 1
    if is_night_enhancement_chosen:
        rows += 1
    if is_object_detection_chosen:
        rows += 1

    for i in range(len(input_files)):
        pos = 1
        '''when rows = 1, only 2 sub, one line'''
        sub_rows = 2 if rows >= 2 else 1
        # plt.figure(figsize=(12.8, 9.6))  # (6.4, 4.8 by default)
        if sub_rows == 2:
            plt.figure(figsize=(12.8, 9.6))
        else:
            plt.figure(figsize=(12.8, 4.8))
        # plt.tight_layout(pad=0.4)
        plt.subplot(sub_rows,2,1)
        plt.imshow(mpimg.imread(os.path.join(input_path, input_files[i])))
        plt.title('原图像')
        plt.xticks([]), plt.yticks([])
        if is_light_effects_clear_chosen:
            pos += 1
            plt.subplot(sub_rows,2,pos)
            plt.imshow(mpimg.imread(os.path.join(light_effect_result_path, light_effects_result_files[i])))
            plt.title('强光分离后')
            plt.xticks([]), plt.yticks([])
        if is_night_enhancement_chosen:
            pos += 1
            plt.subplot(sub_rows,2,pos)
            plt.imshow(mpimg.imread(os.path.join(night_enhancement_result_path, night_enhancement_result_files[i])))
            plt.title('弱光分离后')
            plt.xticks([]), plt.yticks([])
        if is_object_detection_chosen:
            pos += 1
            plt.subplot(sub_rows,2,pos)
            plt.imshow(mpimg.imread(os.path.join(object_detection_result_path, object_detection_result_files[i])))
            plt.title('目标检测结果')
            plt.xticks([]), plt.yticks([])
        # plt.title(titles)
        # plt.imsave(os.path.join(output_time, file))
        plt.savefig(os.path.join(output_time, input_files[i]))

    with open(os.path.join(output_time, nowTime + '.log.txt'), 'w', encoding='utf-8') as f:
        f.write('[images]\n')
        # f.writelines(input_files)
        for file in input_files:
            f.write(f'{file}\n')
        f.write('\n[settings]\n')
        f.write(f'light effects clear: {is_light_effects_clear_chosen}\n')
        if is_light_effects_clear_chosen:
            f.write(f'\timgsz: {light_imgsz}\n')
        f.write(f'night enhancement: {is_night_enhancement_chosen}\n')
        if is_night_enhancement_chosen:
            f.write(f'\tmodel: {enhance_model}\n')
        f.write(f'object detection: {is_object_detection_chosen}\n')
        if is_object_detection_chosen:
            f.write(f'\tmodel: {detect_model_name}\n')
            f.write(f'\timgsz: {detect_imgsz}\n')
            f.write(f'\tconf: {detect_conf}\n')

    clear(clear_detect=True)


if __name__ == '__main__':
    # clear()
    start()
