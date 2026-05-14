import cv2
from ultralytics import YOLO  # importing yolo model 
import os # to create folder for saving screenshot

# load the YOLO model
model = YOLO("yolo11s.pt")

os.makedirs("screenshot", exist_ok=True) # use to create folder named screenshot in your project

# open the webcam
cap = cv2.VideoCapture(0)

count = 0 

while True: # to check if the webcam is off
    ret, frame = cap.read() # ret = to check whether the camera is on or not
                             # frame = the actual img that is going to capture 
                             # cap.read() = use to click the img per seconds

    result = model(frame) 
    annotated_frame = result[0].plot() # to draw boxes and name the detected boxes
    cv2.imshow("Object Detection", annotated_frame) 

    key = cv2.waitKey(1) & 0xFF  # added key variable here

    if key == ord('s'):
        count += 1
        cv2.imwrite(f"screenshot/detection_{count}.jpg", annotated_frame)
        print(f"Screenshot {count} saved!") # to save the present state of human

    if key == ord('q'): # to close the webcam using q button 
        break

cap.release()
cv2.destroyAllWindows()