## Additional Feature - Emotion Detection

This project also uses DeepFace and OpenCV to perform real-time emotion detection through a webcam.

The system:
- Detects faces from the webcam feed
- Analyzes facial emotions in real time
- Displays the dominant emotion on the screen
- Supports emotions such as Happy, Sad, Angry, Fear, Surprise, Neutral, and Disgust

This feature can be used for:
- Human behavior analysis
- AI-based monitoring systems
- Student projects and research
- Computer vision learning

- ## Libraries Used

- OpenCV - for webcam and image processing
- Ultralytics YOLO - for object detection
- DeepFace - for emotion detection
- Pandas - for data handling
- Numpy - for numerical operations
- Datetime - for timestamp
- CSV - for saving detection log

- ## Project Files

- Yolo_Example.py - main object detection file
- human_detection.py - human detection file
- emotion_detection.py - real-time emotion detection using DeepFace
- csv_format_example.py - saves detection log to csv
- save_ss.py - saves screenshots
- pandas_Example.py - pandas example
- np_Example.py - numpy example
- opencv_Example.py - opencv example
- detection_log.csv - saved detection data
- screenshot/ - saved screenshots folder

- ## Emotion Detection Usage

1. Connect your webcam.
2. Run the emotion detection file:

python emotion_detection.py

3. The webcam window will open.
4. The detected emotion will be displayed above the face.
5. Press Q to quit the application.
