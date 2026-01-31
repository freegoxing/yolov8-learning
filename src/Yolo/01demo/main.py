import torch
from ultralytics import YOLO

# 检查GPU是否可用
print(f"CUDA是否可用: {torch.cuda.is_available()}")
print(f"设备名称: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else '无GPU设备'}")

# YOLOv8 会自动（优先）使用 GPU 加速推理
yolo = YOLO(model="../../models/yolov8n.pt", task="detect")

img_result = yolo.predict(source="traffic.png", save=True)
video_result = yolo.predict(source="traffic.mp4", save=True)
