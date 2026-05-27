# importing opencv library and YOLO library from ultralytics
import cv2
from ultralytics import YOLO

capture = cv2.VideoCapture(0) # to start webcam

model = YOLO("yolov8n.pt") # to load YOLO model

while True:
    ret, frame = capture.read() # read each and every frame from webcam

    if not ret: # checking if the webcam capture the frame properly or not
        print("Failed to detect the frame")
        break

    result = model(frame, classes=[0]) # to detect only humans from the frame
    human_count = len(result[0].boxes) # to count only humans from the frame
    annotated_frame = result[0].plot() # to create a box over the detected figure
    
    cv2.putText(  # to display human count on the screen
        annotated_frame,
        f"Human: {human_count}",
        (20, 40),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Human detected", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
