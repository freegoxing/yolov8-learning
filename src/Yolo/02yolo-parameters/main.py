from ultralytics import YOLO

yolo = YOLO(model="../../models/yolov8n.pt", task="detect")

# 设置最低置信度，即概率小于 conf 的模型不会在结果上标注(默认为0.25)
result_conf = yolo.predict(source="traffic.png", save=True, conf=0.66)

