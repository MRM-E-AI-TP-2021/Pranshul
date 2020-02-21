import pygame
ser = serial.Serial('/dev/ttyUSB0')
def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

pygame.init()
print ("Joystics: ", pygame.joystick.get_count())
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        x=my_joystick.get_axis(0)
        y=my_joystick.get_axis(1)
        x=-1*(map(x, -1, 1, -1023, 1023))
        y=map(y, -1, 1, -1023, 1023)
        clock.tick(100)
        ledR=0
        ledL=0
        if (y > 10):
            ledR = map(y, 10, 1023, 0, 255)
            ledL = map(y, 10, 1023, 0, 255)
        elif (y < -10):
            ledR = map(y, -10, -1023, 0, -255)
            ledL = map(y, -10, -1023, 0, -255)
        else:
            ledR = 0
            ledL = 0
        if (x > 10):
            X = map(x, 10, 1023, 0, 255)
            ledR = ledR - X
            ledL = ledL + X
            if (ledL > 255):
                ledL = 255
            if (ledR < -255):
                ledR = -255
        elif (x < -10):
            X = map(x, -10, -1023, 0, 255)
            ledR = ledR + X
            ledL = ledL - X
            if (ledR > 255):
                ledR = 255
            if (ledL < -255):
                ledL = -255
        if(ledL>=0):
            fl = ledL
        else:
            bl = ledL
        if(ledR>=0):
            bl = ledR
        else:
            br = ledR
        fl = int(fl)*10+1
        fr = int(fr)*10+2
        bl = int(bl)*10+3
        br = int(br)*10+4
        fl = "{0:0=4d}".format(fl)
        fl = str(fl)
        fl = fl.encode()
        time.sleep(0.05)
        ser.write(fl)
        fr = "{0:0=4d}".format(fr)
        fr = str(fr)
        fr = fr.encode()
        ser.write(fr)
        bl = "{0:0=4d}".format(bl)
        bl = str(bl)
        bl = bl.encode()
        ser.write(bl)
        br = "{0:0=4d}".format(br)
        br = str(br)
        br = br.encode()
        time.sleep(0.05)
        ser.write(br)

pygame.quit ()