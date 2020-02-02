import socket
import pickle
import cv2
import numpy as np
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.43.58', 2000))
while 1:
    a = []
    print(1)
    while True:
        packet = s.recv(99999)
        if not packet:
            print("error")
            break
        a.append(packet)
        print(2)
        try:
            if(pickle.loads(packet) == "bk"):
                break
            print(3)
        except:
            pass
    try:    
        print(4)
        m,data_arr = pickle.loads(b"".join(a))

        data_arr = cv2.imdecode(data_arr,cv2.IMREAD_ANYCOLOR)
        data_arr = cv2.resize(data_arr,(640,480))
        cv2.imshow('frame',data_arr)
    except:
        pass
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()
s.close()