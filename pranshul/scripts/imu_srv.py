#!/usr/bin/env python
from pranshul.srv import imu,imuRequest,imuResponse
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
angle1  = 0
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
def imu1(req):
    angle1 = angle(X_axis_H,Y_axis_H,Z_axis_H)
    return imuResponse(angle1)
def imu_srv():
    rospy.init_node('imu_server')
    s = rospy.Service('imu',imu,imu1)
    rospy.spin()
if __name__ == "__main__":
    imu_srv()

