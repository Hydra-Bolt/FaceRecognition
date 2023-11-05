import threading
import os
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cascPath = "haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
faces_dict = {face: os.listdir(f"./faces/{face}") for face in os.listdir("./faces")}
face_match = False
confidence = 0
matched_name: str = ""


def check_face(frame):
    global face_match, matched_name, confidence
    for name, face_angles in faces_dict.items():
        for face_angle in face_angles:
            # print(f"./faces/{name}/{face_angle}")
            reference_img = cv2.imread(f"./faces/{name}/{face_angle}")
            result  = DeepFace.verify(frame, reference_img.copy(), )
            try:
                if result["verified"] and result["distance"]<.3:
                    face_match = True
                    matched_name = name
                    confidence = result["distance"]
                    return
                else:
                    face_match = False
                    matched_name = ""
            except ValueError:
                face_match = False
                matched_name = ""

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                check_face(frame.copy())
            except ValueError:
                pass
        counter += 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags= cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            # print(matched_name)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, matched_name + ":" + str(1-confidence) if matched_name else "Not Recognized" , (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
