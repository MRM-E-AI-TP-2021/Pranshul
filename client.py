import socket
import pickle
import cv2
import numpy as np
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2001))
while 1:
    a = []
    while True:
        packet = s.recv(99999)
        if not packet:
            print("error")
            break
        if(pickle.loads(packet) == "pg"):
            break
        else:
            a.append(packet)
    m,data_arr = pickle.loads(b"".join(a))
    data_arr = cv2.imdecode(data_arr,cv2.IMREAD_ANYCOLOR)
    print(data_arr)
    cv2.imshow('frame',data_arr)
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()
s.close()