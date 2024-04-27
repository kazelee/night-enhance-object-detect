from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/save-picture/', methods=['POST'])
def save_picture():
    import os
    # 图片对象
    file_obj = request.files.get('file')
    # 图片名字
    file_name = request.form.get('fileName')
    # 图片保存的路径
    save_path = os.path.abspath(os.path.dirname(__file__) + '\\static') + '\\img' + '\\' + str(
        file_name)
    # 保存
    file_obj.save(save_path)
    return '图片保存成功'

# @app.route('/img/<filename>')
# def get_filename(filename):
#     with open(f'./img/{filename}', 'rb') as f:
#         file_content = f.read()
#     return file_content


@app.route('/get-picture/', methods=['GET'])
def get_picture():
    picture_data = {
        "file_name": "15.jpg",
        "url": "http://127.0.0.1:5678/static/img/15.jpg"
    }
    return jsonify(picture_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678, debug=True)
