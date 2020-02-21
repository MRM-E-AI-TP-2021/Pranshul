import serial
import pynmea2
import numpy as np
ser = serial.Serial('/dev/ttyUSB0',baudrate=4800)
ser.flushInput()
while True:
    a= ser.readline()
    a = a.decode("utf-8")
    nmeaobj = np.array(a.split(","))
    if nmeaobj[0] == "$GPRMC":
        print("Latitude = ",str(nmeaobj[3]),str(nmeaobj[4]))
        print("Longitude = ",str(nmeaobj[5]),str(nmeaobj[6]))