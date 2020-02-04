import pygame
import serial
import pickle
import time
ser = serial.Serial('/dev/ttyUSB0')
     # write a string
def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
pygame.init()
print("Joystics: ", pygame.joystick.get_count())
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()
a = 1
fl = 0
fr = 0
bl = 0
br = 0
m = 0
n = 0
q = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
while 1:
    for event in pygame.event.get():
        clock.tick(60)
        X = my_joystick.get_axis(0)
        Y = my_joystick.get_axis(1)
        X=-1*(map(X, -1, 1, -1023, 1023))
        Y=map(Y, -1, 1, -1023, 1023)
        X = X
        Y = Y
        x1 = 1023
        x2 = 1023
        y1 = 1023
        y2 = 1023
        if(X==0):
            if(Y==0):
                ####/*move nowhere*###/
                fl = 0
                fr = 0
                bl = 0
                br = 0    
            elif(Y<0 and Y>=-y1):
                ####/*move forward*###/
                n = map(Y,0,-y1,0,255)
                fl = n
                fr = n
                bl = 0
                br = 0
            elif(Y>0 and Y<=y2):
            ###/*move back*###/
                n = map(Y,0,y2,0,255)
                fl = 0
                fr = 0
                bl = n
                br = n
        elif(Y == 0):
            if(X<=x2 and X>0):
                ####/*hard right*###/
                n = map(X,0,x2,0,255)
                fl = n
                fr = 0
                bl = 0
                br = n
                        
            elif(X>=-x1 and X<0):
                ####/*hard left*###/
                n = map(X,0,-x1,0,255)
                fl = 0
                fr = n
                bl = n
                br = 0
        elif(Y == -y1):
            if(X == -x1 and Y == -y1):
                ####/*soft left*###/
                fl = 0
                fr = 255
                bl = 0
                br = 0
            elif(X == x2 and Y == -y1):
                ####/*soft right*###/
                fl = 255
                fr = 0
                bl = 0
                br = 0   
            elif(X<x2 and X>0 and Y == -y1):
            ###/*2*###/
                n = map(X,x2,0,0,255)
                fl = 255
                fr = n
                bl = 0
                br = 0
            
            elif(X<0 and X>-x1 and Y == -y1):
            ###/*3*###/
                n = map(X,-x1,0,0,255)
                fl = n
                fr = 255
                bl = 0
                br = 0
        
        elif(Y == 1022 or Y == 1023):
            print("back")
            if(X == -x1):
                ####/*soft back right*###/
                fl = 0
                fr = 0
                bl = 255
                br = 0
            elif(X<0 and X>-x1):
            ###/*6*###/
                print("66666")
                n = map(X,-x1,0,0,255)
                fl = 0
                fr = 0
                bl = 255
                br = n
            elif(X<x2 and X>0):
            ###/*7*###/
                n = map(X,x2,0,0,255)
                fl = 0
                fr = 0
                bl = n
                br = 255

        elif(X == y2 and Y == x2):
            ####/*soft back left*###/
            fl = 0
            fr = 0
            bl = 0
            br = 255 
       
        

        elif(X == x2 and Y<0 and Y>-y1):
        ###/*1*###/
            n = map(Y,-y1,0,0,255)
            fl = 255
            fr = 0
            bl = 0
            br = n

        elif(X == -x1 and Y<0 and Y>-y1):
        ###/*4*###/
            n = map(Y,-y1,0,0,255)
            fl = 0
            fr = 255
            bl = n
            br = 0


        elif(X == x2 and Y<y2 and Y>0):
        ###/*8*###/
            n = map(Y,y2,0,0,255)
            fl = n
            fr = 0
            bl = 0
            br = 255
        elif(X == -1022 and Y<y2 and Y>0):
        ####/*5*###/
            n = map(Y,y2,0,0,255)
            fl = 0
            fr = n
            bl = 255
            br = 0
        print("fl = ",fl)
        print("fr = ",fr)
        print("bl = ",bl)
        print("br = ",br)
        fl = "{0:0=4d}".format(fl)
        fl = fl*10+1
        fl = str(fl)
        fl = line.encode()
        ser.write(fl)
        fr = "{0:0=4d}".format(fr)
        fr = fr*10+2
        fr = str(fr)
        fr = line.encode()
        ser.write(fr)
        bl = "{0:0=4d}".format(bl)
        bl = bl*10+3
        bl = str(bl)
        bl = line.encode()
        ser.write(bl)
        br = "{0:0=4d}".format(br)
        br = br*10+4
        br = str(br)
        br = line.encode()
        ser.write(br)
pygame.quit ()