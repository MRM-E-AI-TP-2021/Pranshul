import socket
import cv2
import numpy as np
import pickle
cap = cv2.VideoCapture(0)
cap.set(3,200)
cap.set(4,150)
s=socket.socket()
s.bind(('', 2000))
s.listen(3)
a,c = s.accept()
while(True):
    z , frame = cap.read()
    if(z==True):
        frame = pickle.dumps(frame)
        a.sendall(frame)
        lol = pickle.dumps("a")
        a.sendall(lol)
a.close()
cap.release()
cv2.destroyAllWindows()