import cv2  # loading open cv library
from deepface import DeepFace  # to load face recognition library

Capture = cv2.VideoCapture(0)  # to open Webcam

while True:  # to run the webcam continuously

    ret, frame = Capture.read()  # to capture the frame from webcam

    if not ret:  # to check whether frame is captured or not
        print("Failed to capture the frame")
        break

    # analyze the emotion from the frame
    result = DeepFace.analyze(
        frame,
        actions=['emotion'],  # to detect only emotion
        enforce_detection=False  # to continue even if face is not detected properly
    )

    # to get the detected emotion
    emotion = result[0]['dominant_emotion']

    # to display emotion on the screen
    cv2.putText(
        frame,
        f"Emotion: {emotion}",
        (20, 40),
        cv2.FONT_HERSHEY_DUPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Capture.release()
cv2.destroyAllWindows()