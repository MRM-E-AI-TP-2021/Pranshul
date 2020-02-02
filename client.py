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
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
        thresh1 = np.array([lh,ls,lv])
        thresh2 = np.array([uh,hs,hv])
        mask = cv2.inRange(HSV,thresh1,thresh2)
        mask = cv2.GaussianBlur(mask,(7,7),0)
        image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
        HSV1 = cv2.bitwise_and(frame,frame,mask=mask)

        for i in range(0,len(contours)):
            if len(contours)>1:
                (x,y),radius = cv2.minEnclosingCircle(contours[i])
                center = (int(x),int(y))
                radius = int(radius)
                x1, y1, w, h = cv2.boundingRect(contours[i])
                aspect_ratio = float(w) / h
                area1 = np.pi * radius * radius
                area2 = cv2.contourArea(contours[i])
                if(area1 != 0 and area2 != 0 ):
                    e = area1/area2
                else:
                    e = 0
                area = cv2.contourArea(contours[i])
                hull = cv2.convexHull(contours[i])
                hull_area = cv2.contourArea(hull)
                if(hull_area != 0):
                    solidity = float(area) / hull_area
                else:
                    solidity = 0
            if(aspect_ratio > a1 and aspect_ratio < a2 and e>e1 and e < e2 and minrad<radius and solidity < 1 and solidity > a1 ):
                frame = cv2.drawContours(frame,contours,i,color=(255,0,0),thickness=3)
                frame = cv2.circle(frame,center,radius,(0,0,255),2)
                frame = cv2.putText(frame,"Ball",(int(x-radius),int(y-radius)),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
                frame = cv2.putText(frame, "Ball detected", (380,30),
                                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 0, 255),thickness=3)

        else:
            pass
        fps = cap.get(cv2.CAP_PROP_FPS)
        cv2.imshow("HSV",frame)
        cv2.imshow("mask",mask)
        if(cv2.waitKey(1) & 0xFF == 27):
            break
    except:
        pass
    if(cv2.waitKey(1) & 0xFF == 27):
        break
cv2.destroyAllWindows()
s.close()