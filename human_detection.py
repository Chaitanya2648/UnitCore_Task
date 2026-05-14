import cv2
from ultralytics import YOLO   
import datetime # to load data and time when human is detected

# load the YOLO model
model = YOLO("yolo11s.pt")

# open the webcam
cap = cv2.VideoCapture(0)

detection_log = [] # to store the timestamp and count the detected human

while True: # to check if the webcam is off
    ret, frame = cap.read() # ret = to check whether the camera is on or not
                             # frame = the actual img that is going to capture 
                             # cap.read() = use to click the img per seconds

    result = model(frame) 
    annotated_frame = result[0].plot() # to draw boxes and name the detected boxes

    human_count = 0 # use to count human in each frame
    for box in result[0].boxes:
        if int(box.cls[0]) == 0:
            human_count += 1

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # to get the time according to the clock

    detection_log.append({"time": timestamp, "count": human_count}) # to save the time and count

    cv2.putText(annotated_frame, f"Humans: {human_count}", (10, 30), # to write text on webcam
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Object Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # to close the webcam using q button
        break

cap.release()
cv2.destroyAllWindows()