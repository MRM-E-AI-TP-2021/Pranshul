import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
while(cap.isOpened()):
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if ret==True and ret1==True:
        frame = np.concatenate((frame,frame1))
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cap1.release()
cv2.destroyAllWindows()
