from flask import Flask, request, jsonify
import os
from flask_cors import CORS  # 导入CORS模块

# 文件存储的目录
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 启用CORS
# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # 允许所有来源

# 设置文件上传大小限制为 16 MB
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': '上传的非图片'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': '没选择图片'})

    if file and allowed_file(file.filename):
        print(file)
        print(file.filename)
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': '上传图片成功'})
    else:
        return jsonify({'error': '无效'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
