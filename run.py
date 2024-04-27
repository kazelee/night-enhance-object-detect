from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import main_logic
import shutil

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# 记录程序是否正在运行
last_running_state = False
is_running = False


# 这里默认的是get请求方式
@app.route('/')
def hello_world():
    # 这里面就是你想要返回给前端的值， 切记，这里只能返回字符串，如果是个json数据，你的通过json.dumps(你的json数据)
    return 'Hello World!'


@app.route('/save-picture/', methods=['POST'])
def save_picture():
    file_obj = request.files.get('file')  # 图片对象
    file_name = request.form.get('fileName')  # 图片名字
    save_path = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\' + str(file_name)  # 保存路径
    file_obj.save(save_path)
    return '图片保存成功'


@app.route('/del-picture/', methods=['POST'])
def del_picture():
    try:
        # 获取前端发送的图像信息
        image_info = request.get_json()

        # 假设图像信息中包含文件名
        filename = image_info.get('filename')

        # 在这里执行删除图像的操作，例如从文件系统中删除文件
        # 请根据您的实际需求进行相应的处理

        if filename:
            # image_path = os.path.join('http://127.0.0.1:5000/static/img/', filename)
            image_path = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\' + str(filename)
            if os.path.exists(image_path):
                os.remove(image_path)
                return jsonify({'message': f'图像 {filename} 已成功删除'})
            else:
                return jsonify({'error': f'图像 {filename} 不存在'})

        return jsonify({'error': '未提供有效的图像文件名'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # # file_obj = request.files.get('file')  # 图片对象
    # file_name = request.form.get('fileName')  # 图片名字
    # save_path = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\' + str(file_name)  # 保存路径
    #
    # try:
    #     os.remove(save_path)  # Delete the image file
    #     return '图片删除成功'  # Return a success message
    # except FileNotFoundError:
    #     return '文件不存在'  # Return an error message if the file doesn't exist


@app.route('/do-sth/', methods=['POST'])
def do_something():

    tmp_data = request.get_json()
    if tmp_data["todo"] == "open-last":
        dirs = os.listdir('./output/')
        dir_name = dirs[-1]
        abs_path = os.path.abspath(os.path.join('./output/', dir_name))
        os.system(f'start explorer {abs_path}')
        return jsonify({'message': f'成功打开 {abs_path}'})

    return jsonify({'error': '未提供有效的指令'})

@app.route('/get-picture/', methods=['GET'])
def get_picture():
    picture_data_list = []
    img_path = './static/img'

    files = os.listdir(img_path)
    file_list = [file for file in files if os.path.isfile(os.path.join(img_path, file))]

    for file in file_list:
        picture_data_list.append({"file_name": file, "url": f"http://127.0.0.1:5000/static/img/{file}"})

    res = jsonify(picture_data_list)
    print(res)
    return res


def create_dir(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def remove_dir(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)


def mycopyfile(srcfile, dstpath):                      # 复制函数
    if not os.path.isfile(srcfile):
        print("%s not exist!" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)          # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


@app.route('/get-last-result/', methods=['GET'])
def get_last_result():
    remove_dir('./static/res/')
    create_dir('./static/res/')
    pic_src_list = []

    dirs = os.listdir('./output/')
    dir_name = dirs[-1]
    abs_path = os.path.abspath(os.path.join('./output/', dir_name))

    files = os.listdir(abs_path)
    # 保存图像的后缀名与原图后缀名一致，这里不考虑类型判断，只需要避免txt文件即可 # file.endswith('.jpg')
    file_list = [file for file in files if os.path.isfile(os.path.join(abs_path, file)) and not file.endswith('.txt')]

    for file in file_list:
        mycopyfile(os.path.join(abs_path, file), os.path.join('./static/res/'))
        pic_src_list.append(f'http://127.0.0.1:5000/static/res/{file}')

    res = jsonify(pic_src_list)
    print(f'res: {res}')
    return res


@app.route('/get-signal/', methods=['GET'])
def get_signal():
    global last_running_state
    global is_running
    signals = []
    if not last_running_state and not is_running:
        signals.append('none')
    elif not last_running_state and is_running:
        signals.append('start')
        last_running_state = True
    elif last_running_state and is_running:
        signals.append('running')
    else:
        # last = True and is_running = false
        signals.append('end')
        last_running_state = False

    return jsonify(signals)


@app.route('/set-args/', methods=['POST'])
def set_args():
    tmp_args = request.get_json()
    main_logic.is_light_effects_clear_chosen = tmp_args["delivery"]
    main_logic.is_night_enhancement_chosen = tmp_args["delivery2"]
    main_logic.is_object_detection_chosen = tmp_args["delivery3"]
    main_logic.has_night_enhancement_compare = tmp_args["delivery4"]
    if main_logic.has_night_enhancement_compare:
        main_logic.has_object_detection_compare = tmp_args["delivery5"]
        main_logic.has_detect_origin_img = tmp_args["delivery6"]
    else:
        main_logic.has_object_detection_compare = False
        main_logic.has_detect_origin_img = False

    main_logic.light_imgsz = int(tmp_args["region"])
    new_light_imgsz = int(tmp_args["desc"]) // 32 * 32 + 32 if int(tmp_args["desc"]) % 32 != 0 else int(tmp_args["desc"])
    main_logic.detect_imgsz = new_light_imgsz

    main_logic.enhance_model = tmp_args["region2"]
    main_logic.detect_model_name = tmp_args["region3"]

    main_logic.detect_conf = float(tmp_args["desc2"])
    main_logic.night_enhancement_result_path = './results/Test/RetinexFormer_Test/' + main_logic.enhance_model + '/'

    global is_running
    is_running = True

    main_logic.start()

    is_running = False

    return jsonify({"message": "图像处理已完成"})


if __name__ == '__main__':
    # 确保开始运行时有input和output文件夹
    if not os.path.exists('./input/'):
        os.mkdir('./input/')
    if not os.path.exists('./output/'):
        os.mkdir('./output')

    app.run()
    # app.run(host='0.0.0.0', port=5678, debug=True)
