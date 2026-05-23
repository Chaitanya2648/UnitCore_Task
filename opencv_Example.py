# to load a open cv library to open webcam
import cv2 as cv

capture = cv.VideoCapture(0) # to open webcam 

while True:
    isTrue, frame = capture.read() # to load every frame of the video
    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xff ==  ord ("q"):
        break

capture.release() # it use to release the code so other can use it
cv.destroyAllWindows() # use to close all open cv windows