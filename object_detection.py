# using YOLO libraries from ultralytics
from ultralytics import YOLO
# using open cv to start the web cam
import cv2

model = YOLO("yolov8n.pt")
capture = cv2.VideoCapture(0) # to start and load the web cam

while True:
    ret, frame = capture.read()
    if not ret: # if the frame is not capture it break the loop
        break
    result = model(frame) # to send the frame to model
    annotated_frame = result[0].plot() # it is use to store the result taken by the frame

    cv2.imshow("YOLO detection", annotated_frame) # to displat the frame that captured

    if cv2.waitKey(1) & 0xFF == ord('q'): # free the output till user does not press 'q
        break

capture.release()
cv2.destroyAllWindows()