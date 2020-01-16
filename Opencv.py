
import cv2
import  numpy as np
def nothing(x):
    print(x)
def save(x):
    if(x==1):
        Thresh1 = np.array([lh,ls,lv])
        Thresh2 = np.array([uh,hs,hv])
        print(Thresh1)
        print(Thresh2)
cv2.namedWindow("HSV")
cv2.createTrackbar("lh", "HSV", 0, 179, nothing);
cv2.createTrackbar("ls", "HSV", 0, 255, nothing);
cv2.createTrackbar("lv", "HSV", 0, 255, nothing);
cv2.createTrackbar("uh", "HSV", 179, 179, nothing);
cv2.createTrackbar("hs", "HSV", 255, 255, nothing);
cv2.createTrackbar("hv", "HSV", 255, 255, nothing);
cv2.createTrackbar("save","HSV",0,1,save);


cap = cv2.VideoCapture(0)
while(True):
    z,frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        lh = cv2.getTrackbarPos('lh', "HSV")
        ls = cv2.getTrackbarPos('ls', "HSV")
        lv = cv2.getTrackbarPos('lv', "HSV")
        uh = cv2.getTrackbarPos('uh', "HSV")
        hs = cv2.getTrackbarPos('hs', "HSV")
        hv = cv2.getTrackbarPos('hv', "HSV")

        thresh1 = np.array([lh,ls,lv])
        thresh2 = np.array([uh,hs,hv])

        mask = cv2.inRange(HSV,thresh1,thresh2)
        HSV1 = cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("HSV",HSV1)
        if(cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
