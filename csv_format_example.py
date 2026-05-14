import cv2
from ultralytics import YOLO   
import datetime
import csv

# load YOLO model
model = YOLO("yolo11s.pt")

# open webcam
cap = cv2.VideoCapture(0)

# empty list to store data
detection_log = []

while True:
    # read frame from webcam
    ret, frame = cap.read()

    # detect objects
    result = model(frame) 

    # draw boxes on frame
    annotated_frame = result[0].plot()

    # count humans
    human_count = 0
    for box in result[0].boxes:
        if int(box.cls[0]) == 0:
            human_count += 1

    # get current time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # save time and count in list
    detection_log.append({"time": timestamp, "count": human_count})

    # show human count on screen
    cv2.putText(annotated_frame, f"Humans: {human_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # display frame
    cv2.imshow("Object Detection", annotated_frame)

    # press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# save data to csv file
with open("detection_log.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["time", "count"])
    writer.writeheader()
    writer.writerows(detection_log)
    print("CSV file saved!")

# release webcam
cap.release()

# close all windows
cv2.destroyAllWindows()