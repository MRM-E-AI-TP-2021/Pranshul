import socket
import cv2
import numpy as np
import pickle
cap = cv2.VideoCapture(0)
cap.set(3,400)
cap.set(4,300)
s=socket.socket()
s.bind(('192.168.43.203',2000))
s.listen(3)
a,c = s.accept()
while(True):
    z , frame = cap.read()
    print(frame)
    if(z==True):
        frame = cv2.imencode('.jpeg',frame)
        
        frame = pickle.dumps(frame)
        a.sendall(frame)
        lol = pickle.dumps("pg")
        a.sendall(lol)
a.close()
cap.release()
cv2.destroyAllWindows()