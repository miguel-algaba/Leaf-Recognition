from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

model= YOLO("yolov8n.pt")

model.train(data="configuracion.yaml", epochs=30,imgsz=256,iou=0.6)