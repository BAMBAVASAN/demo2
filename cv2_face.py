import cv2

# Load the pre-trained cascade classifier for face detection
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create a VideoCapture object to read from the webcam
vs = cv2.VideoCapture(0)

while True:
    # Read the current frame from the video stream
    ret, frame = vs.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
vs.release()
cv2.destroyAllWindows()
