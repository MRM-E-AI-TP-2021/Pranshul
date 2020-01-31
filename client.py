import socket
import pickle
import cv2
import numpy as np
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2001))
while 1:
    while True:
        packet = s.recv(99999)
        if not packet:
            print("error")
            break
        if(pickle.loads(packet) == "pg"):
            print("break")
            break
        else:
            print(type(pickle.loads(packet)))
            a = np.asarray(pickle.loads(packet))
            a = np.append(a,a)
    print(m)
    data_arr = cv2.imdecode(a,cv2.IMREAD_COLOR)
    cv2.imshow('frame', data_arr)
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()
s.close()