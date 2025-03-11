import cv2
import numpy as np
from ultralytics import YOLO

# Load mô hình YOLOv8
model = YOLO("./backend/ckpt/yolo11n.pt")

def detect_people(image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]

    people_count = 0
    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box
        if int(cls) == 0:  # Lớp 0 là "person" trong YOLO
            people_count += 1
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    processed_path = image_path.replace("uploads", "processed")
    cv2.imwrite(processed_path, image)
    
    return people_count, processed_path