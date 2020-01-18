import cv2
import  numpy as np

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
cv2.setTrackbarPos('lh',"HSV",30)
cv2.setTrackbarPos('ls',"HSV",42)
cv2.setTrackbarPos('lv',"HSV",67)
cv2.setTrackbarPos('uh',"HSV",63)
cv2.setTrackbarPos('hs',"HSV",255)
cv2.setTrackbarPos('hv',"HSV",255)
cap = cv2.VideoCapture(0)
while(True):
    z,frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        g = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        lh = cv2.getTrackbarPos('lh', "HSV")
        ls = cv2.getTrackbarPos('ls', "HSV")
        lv = cv2.getTrackbarPos('lv', "HSV")
        uh = cv2.getTrackbarPos('uh', "HSV")
        hs = cv2.getTrackbarPos('hs', "HSV")
        hv = cv2.getTrackbarPos('hv', "HSV")

        ret, thresh = cv2.threshold(g,127, 255, 0)

        thresh1 = np.array([lh,ls,lv])
        thresh2 = np.array([uh,hs,hv])
        mask = cv2.inRange(HSV,thresh1,thresh2)

        kernel = np.ones((2,2),np.uint8)/4
        mask = cv2.dilate(mask, kernel, iterations=1)
        mask = cv2.filter2D(mask, -1, kernel)
        #mask = cv2.medianBlur(mask,5)

        image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        HSV1 = cv2.bitwise_and(frame, frame, mask=mask)
        if(len(contours)>1):
            (x,y),radius = cv2.minEnclosingCircle(contours[0])
            center = (int(x),int(y))
            radius = int(radius)
            x, y, w, h = cv2.boundingRect(contours[0])
            aspect_ratio = float(w) / h
            area1 = np.pi * radius * radius
            area2 = cv2.contourArea(contours[0])
            
            if(area1 != 0 and area2 != 0 ):
                e = area1/area2
            else:
                e = 0
            
            if(aspect_ratio > a1 and aspect_ratio < a2 and e < e1 and minrad<radius):
                HSV1 = cv2.circle(HSV1,center,radius,(0,255,0),2)
                print("BALL!!!!")
        else:
            pass
        cv2.imshow("HSV",HSV1)

        if(cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
