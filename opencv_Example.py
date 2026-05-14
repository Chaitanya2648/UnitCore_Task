import cv2  # to import openCv library

cap = cv2.VideoCapture(0) # to open the camera 

while True: # run the loop till the user does not press q button 
    ret, frame = cap.read()

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()