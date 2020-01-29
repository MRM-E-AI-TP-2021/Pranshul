import socket
import pickle
import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2000))

while 1:
    data = []
    data_arr = 0
    while True:
        packet = s.recv(99999)
        if not packet:
            break
        try:
            if(pickle.loads(packet) == "a"):
                break
        except:
            data.append(packet)
            continue
    try:
        data_arr = pickle.loads(b"".join(data))
        data_arr = np.array(data_arr,dtype=np.uint8)
        cv2.imshow('frame', data_arr)
    except:
        pass
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()
s.close()