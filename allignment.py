import serial
import pynmea2
import numpy as np
import math
import smbus		#import SMBus module of I2C
from time import sleep
Register_A     = 0              #Address of Configuration register A
Register_B     = 0x01           #Address of configuration register B
Register_mode  = 0x02           #Address of mode register

X_axis_H    = 0x03              #Address of X-axis MSB data register
Z_axis_H    = 0x05              #Address of Z-axis MSB data register
Y_axis_H    = 0x07              #Address of Y-axis MSB data register
declination = -0.00669          #define declination angle of location where measurement going to be done
pi          = 3.14159265359     #define pi value
def Distance(lat1,lon1,lat2,lon2):  
     R = 6372800  # Earth radius in meters    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 0)
def read_raw_data(addr):
    
        #Read raw 16-bit value
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lowvimer value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x1e   # HMC5883L magnetometer device address

Magnetometer_Init()
ser = serial.Serial('/dev/ttyUSB0',baudrate=4800)
ser.flushInput()
latitude_given = 13.34786166
longitude_given = 74.79216999
angle1  = 0
latitude = 0 
longitude = 0 
def angle(X1,Y1,Z1):
    x = read_raw_data(X1)
    z = read_raw_data(Z1)
    y = read_raw_data(Y1)

    heading = math.atan2(y, x) + declination
    if(heading > 2*pi):
            heading = heading - 2*pi
    if(heading < 0):
            heading = heading + 2*pi

    heading_angle = int(heading * 180/pi) - 88
    return heading_angle
while True:
    a= ser.readline()
    a = a.decode("utf-8")
    nmeaobj = np.array(a.split(","))
    if nmeaobj[0] == "$GPRMC":
        if(str(nmeaobj[4])=="S"):
            latitude = -float(nmeaobj[3])/100
        else:
            latitude = float(nmeaobj[3])/100
        if(str(nmeaobj[6])=="E"):
            longitude = -float(nmeaobj[5])/100
        else:
            longitude = float(nmeaobj[5])/100
        X = math.cos(latitude_given)*math.sin(longitude_given-longitude)
        Y = math.cos(latitude)*math.sin(latitude_given) - math.sin(latitude)*math.cos(latitude_given)*math.cos(longitude_given-longitude)
        angle1 = math.atan2(X,Y)
        
    angle2 = angle(X_axis_H,Y_axis_H,Z_axis_H)
    print(angle1 - angle2)
    print("Distance = %f" %Distance(latitude,longitude,latitude_given,longitude_given))
    sleep(0.01)