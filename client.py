import cv2
import numpy as np
import socket
a = np.ones((640,480))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.42.0.1",2000))

for i in range(0,4):
    for j in range(0,2):
        a = s.recv(1024,int)
print(a)
s.close()