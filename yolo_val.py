from ultralytics import YOLO

# Load a model
# model = YOLO('yolov8m.pt')  # load an official model
# model = YOLO('runs/detect/yolov8_640_ep200/weights/best.pt')  # load a custom model
model = YOLO('object_weights/bdd_day40k20c.pt')

'''change dataset_dir in "C:\\Users\\LENOVO\\AppData\\Roaming\\Ultralytics\\settings.yaml"'''

# Validate the model
# metrics = model.test(split='test')  # no arguments needed, dataset and settings remembered
# metrics.box.map  # map50-95
# metrics.box.map50  # map50
# metrics.box.map75  # map75
# metrics.box.maps  # a list contains map50-95 of each category
metrics = model.val(data='car_val.yaml', split='test')
'''Broken Pipe Error in my PC'''

print(metrics.box.maps)
