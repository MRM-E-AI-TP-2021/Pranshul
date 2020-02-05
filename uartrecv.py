import serial
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
p1 = GPIO.PWM(18,500)
p2 = GPIO.PWM(19,500)
p1 = GPIO.PWM(13,500)
p2 = GPIO.PWM(12,500)
p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
ser = serial.Serial('/dev/ttyS0')
ser.flushInput()
fl = 0
fr = 0
bl = 0
br = 0
while True:
    try:
        time.sleep(0.01)
        Data = ser.read(4)
        data = str(Data.decode("utf-8"))
        try:
            data = int(data)
            bit = data%10
            a = data - bit
            a = a/10
            if(bit == 1):
                fl = a
            if(bit == 2):
                fr = a
            if(bit == 3):
                bl = a
            if(bit == 4):
                br = a
            print("fl = ",fl)
            print("fr = ",fr)
            print("bl = ",bl)
            print("br = ",br)
            fl = int(fl)*100/255
            fr = int(fr)*100/255
            bl = int(bl)*100/255
            br = int(br)*100/255
            p1.ChangeDutyCycle(fl)
            p2.ChangeDutyCycle(fr)
            p3.ChangeDutyCycle(bl)
            p4.ChangeDutyCycle(br)
        except:
            pass