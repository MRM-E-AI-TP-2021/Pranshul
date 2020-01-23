import cv2
import  numpy as np
m =0
aspect_ratio = 0
def nothing(x):
    pass
def save(x):
    if(x==1):
        Thresh1 = np.array([lh,ls,lv])
        Thresh2 = np.array([uh,hs,hv])
        print(Thresh1)
        print(Thresh2)
cv2.namedWindow("HSV")
cv2.createTrackbar("lh", "HSV",0, 179, nothing);
cv2.createTrackbar("ls", "HSV",0, 255, nothing);
cv2.createTrackbar("lv", "HSV",0, 255, nothing);
cv2.createTrackbar("uh", "HSV",179, 179, nothing);
cv2.createTrackbar("hs", "HSV",255, 255, nothing);
cv2.createTrackbar("hv", "HSV",255, 255, nothing);
cv2.createTrackbar("save","HSV",0,1,save);

minrad = 20
a1 = 0.9
a2 = 1.1
e1 = 1
e2 = 1.1
cv2.setTrackbarPos('lh',"HSV",25)
cv2.setTrackbarPos('ls',"HSV",55)
cv2.setTrackbarPos('lv',"HSV",35)
cv2.setTrackbarPos('uh',"HSV",125)
cv2.setTrackbarPos('hs',"HSV",255)
cv2.setTrackbarPos('hv',"HSV",255)
cap = cv2.VideoCapture(0)
po = 0
while(True):
    z,frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL)
        g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lh = cv2.getTrackbarPos('lh', "HSV")
        ls = cv2.getTrackbarPos('ls', "HSV")
        lv = cv2.getTrackbarPos('lv', "HSV")
        uh = cv2.getTrackbarPos('uh', "HSV")
        hs = cv2.getTrackbarPos('hs', "HSV")
        hv = cv2.getTrackbarPos('hv', "HSV")
        thresh1 = np.array([lh,ls,lv])
        thresh2 = np.array([uh,hs,hv])


        mask = cv2.inRange(HSV,thresh1,thresh2)
        mask = cv2.GaussianBlur(mask,(7,7),0)
        #mask = cv2.medianBlur(mask,5)
        k =1
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
            if(aspect_ratio > a1 and aspect_ratio < a2 and e>e1 and e < e2 and minrad<radius and solidity > a1 and solidity < a2):
                frame = cv2.drawContours(frame,contours,i,color=(255,0,0),thickness=3)
                frame = cv2.circle(frame,center,radius,(0,0,255),2)
                frame = cv2.putText(frame,"Ball",(int(x-radius),int(y-radius)),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,255))
                frame = cv2.putText(frame, "Ball detected", (380,30),
                                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 0, 255),thickness=3)
                print("BALL!!!!",po)
                po = po + 1

        else:
            pass

        cv2.imshow("HSV",mask)
        if(cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
