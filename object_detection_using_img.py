# load library name YoLO from ultralytics
from ultralytics import  YOLO

model = YOLO("yolov8n.pt") # variable that store YOLO model

result = model.predict(
   source=r"C:\Users\Chaitanya\OneDrive\Desktop\unitecore project file\schinchan.jpg",
   save = True
)  # creating a container name result and making the YOLO to predict the source

print("Detection completed") # if the img is detected the print statement is printed
result[0].show() # is use to display the image with YOLO dectection result