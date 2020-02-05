import serial
import time
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
