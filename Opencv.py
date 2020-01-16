import cv2
import  numpy as np
def nothing(x):
    print(x);

cv2.namedWindow("HSV")
cv2.createTrackbar("R", "HSV", 0, 255, nothing);
cv2.createTrackbar("B", "HSV", 0, 255, nothing);
cv2.createTrackbar("G", "HSV", 0, 255, nothing);
r_val =0
b_val =0
g_val =0
l=0
p=0
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    z,frame = cap.read()
    if(z==True):
        HSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        ball = HSV[300:200, 320:240]
        r_val = cv2.getTrackbarPos('R', 'HSV')
        b_val = cv2.getTrackbarPos('B', 'HSV')
        g_val = cv2.getTrackbarPos('G', 'HSV')

        if(cv2.waitKey(1) & 0xFF == ord("c")):
            l=1
        if(l==1):
            cv2.rectangle(HSV, (540, 380), (640, 480),(b_val,g_val,r_val), -1)
        if (cv2.waitKey(1) & 0xFF == ord("q")):
            l=0
        colour = np.uint8([[[b_val,g_val,r_val]]])
        thresh = cv2.cvtColor(colour, cv2.COLOR_HSV2BGR)
        mask = cv2.inRange(HSV,thresh-30,thresh+30)
        HSV1 = cv2.bitwise_and(HSV,HSV,mask=mask)


        if(cv2.waitKey(1) & 0xFF == ord("m")):
            p=1
        if(p==1):
            cv2.imshow("HSV",mask)
        else:
            cv2.imshow("HSV", HSV)
        if (cv2.waitKey(1) & 0xFF == ord("q")):
            p=0
        if(cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()