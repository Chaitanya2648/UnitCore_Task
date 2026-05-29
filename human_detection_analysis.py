import cv2 # importing open cv library
import csv # importing csv library
from ultralytics import YOLO # importing YOLO model
from datetime import datetime # importing date and time

file = open("human_count.csv", "a") # creating a csv file

writer = csv.writer(file) # use to convert file into csv writer

capture = cv2.VideoCapture(0) # to start the web cam

model = YOLO("yolov8n.pt") # to load the YOLO model

while True: 
    ret, frame = capture.read() # to read the web cam frame

    result = model(frame, classes=[0]) # use to detect human

    human_count = len(result[0].boxes) # to count human figure

    timestamp = datetime.now().strftime("%H:%M:%S") # to store the current time

    writer.writerow([timestamp, human_count]) # use to write a row in csv file

    annotated_frame = result[0].plot() # to create a box over detected figure

    cv2.putText(  # to display human count on the screen
        annotated_frame,
        f"Human: {human_count}",
        (20, 40),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Human detected", annotated_frame) # to display the output

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows() 

file.close()