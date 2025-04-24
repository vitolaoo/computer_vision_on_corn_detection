from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
  model = YOLO("yolov8l.yaml")
  #model = YOLO("D:/computer_vision_on_corn_detection/train/runs/detect/train4/weights/best.pt")

  results = model.train(
    data="config.yaml",
    epochs=10,
    batch=50,
    workers=0,
    #name="yolov8_corn_detector_v1",
    project="D:/cvcd_trained_models"
)
#focal loss
#dropout