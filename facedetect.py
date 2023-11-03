from cv2 import CascadeClassifier, VideoCapture, cvtColor, COLOR_BGR2GRAY, imshow, waitKey, destroyAllWindows, CASCADE_SCALE_IMAGE, rectangle
import sys

cascPath = "haarcascade_frontalcatface.xml"
faceCascade = CascadeClassifier(cascPath)

video_capture = VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cvtColor(frame, COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags= CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    imshow('Video', frame)

    if waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
destroyAllWindows()