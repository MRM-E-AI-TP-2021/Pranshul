import socket
import cv2
import numpy as np
frame = np.zeros((640,480))
cap = cv2.VideoCapture(0)
po = 0
s=socket.socket()
s.bind(('', 2000))
s.listen(3)
while(True):
    z , frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        HSV = np.array2string(HSV)
        HSV = HSV.encode()
        a,c=s.accept()
        a.send(HSV)
a.close()