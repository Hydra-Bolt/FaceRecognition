import threading

import cv2
from deepface import DeepFace

def checkFace(frame):
    global face_match
    try:
        if DeepFace.verify(frame, rfrnce.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

count = 0

match = False

rfrnce = cv2.imread("reference.jpg")

while True:
    ret, frame = cap.read()
    
    if ret:
        if count%30 == 0:
            try:
                threading.Thread(target = checkFace, args = (frame.copy(),)).start()
            except ValueError:
                pass
        count+=1
        
        if match:
            
            cv2.putText(frame, "Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "No Match!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    key= cv2.waitKey(1)
    if key == ord("q"):
        break
cv2.destroyAllWindows()