import cv2 # to import the open cv library
from ultralytics import YOLO # to YOLO library from ultralytics
import os # to create a folder 
from datetime import datetime # to display the date and time 

# creating a folder to store the image of human detected
os.makedirs("detections", exist_ok=True)

# now starting the webcam 
capture = cv2.VideoCapture(0)

# loading the model using YOLO
model = YOLO("yolov8n.pt")

# starting a continuous loop
while True:

    # use to read the frame
    ret, frame = capture.read()

    # checking if frame is detected properly
    if not ret:
        print("Failed to detect the frame")
        break

    # use to detect human
    result = model(frame, classes=[0])

    # to count the human
    human_count = len(result[0].boxes)

    # checking if human is detected
    if human_count > 0:

        # creating timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # creating filename
        filename = f"detections/human_{timestamp}.jpg"

        # saving the detected image
        cv2.imwrite(filename, frame)

    # displaying the frame
    cv2.imshow('Human Detection', frame)

    # press q to exit the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the webcam
capture.release()

# closing all windows
cv2.destroyAllWindows()