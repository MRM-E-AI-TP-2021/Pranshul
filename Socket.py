import socket
import cv2
import numpy as np
import pickle
import time
cap = cv2.VideoCapture(0)
cap.set(3,200)
cap.set(4,150)
s=socket.socket()
s.bind(('',2000))
s.listen(3)
a,c = s.accept()
time.sleep(5)
while(True):
    z , frame = cap.read()
    if(z==True):
        frame = cv2.imencode('.jpg',frame)
        
        frame = pickle.dumps(frame)
        a.sendall(frame)
        time.sleep(0.01)
        lol = pickle.dumps("bk")
        a.sendall(lol)
a.close()
cap.release()
cv2.destroyAllWindows()