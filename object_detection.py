# 从平台库导入YOLO类
from ultralytics import YOLO
import os


def main(model_name='yolov8n.pt', imgsz=320, conf=0.5):
    # 从模型文件构建model
    model = YOLO("./object_weights/" + model_name)

    path = "./object_test/"
    files = os.listdir(path)
    for file in files:
        model.predict(path + "/" + file, save=True, imgsz=imgsz, conf=conf)
