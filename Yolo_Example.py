import cv2
from ultralytics import YOLO    

model = YOLO("yolo11s.pt") # to load yolo model file
cap = cv2.VideoCapture(0) # to start the webcam

while True: # to check if the webcam is off
    ret, frame = cap.read() # ret = to check whether the camera is on or not
                             # frame =  to actual img that is going to capture 
                             # cap.read() = use to click the img per seconds

    result = model(frame) 
    annotated_frame = result[0].plot() # to draw boxes and name the detected boxes
    cv2.imshow("objecgt detection: ", annotated_frame ) 
    if cv2.waitKey(1) & 0xFF == ord('q'): # to close the webcam using q button 
        break

cap.release()
cv2.destroyAllWindows()

