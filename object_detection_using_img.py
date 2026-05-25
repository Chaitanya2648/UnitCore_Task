from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.predict(
    source="https://ultralytics.com/images/bus.jpg",
    save=True
)

results[0].show()