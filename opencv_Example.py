# load open cv library
import cv2

capture = cv2.VideoCapture(0) # to start webcam

while True:
    ret, frame = capture.read() # to read frame from the webcam

    if not ret: # if the frame is not capture it break the loop
        break

    cv2.imshow("Webcam", frame) # o display the frame captured

    if cv2.waitKey(1) & 0xFF == ord('q'): # free the output till user does not press 'q
        break

capture.release() # to release file
cv2.destroyAllWindows() # to close the files open by webcam