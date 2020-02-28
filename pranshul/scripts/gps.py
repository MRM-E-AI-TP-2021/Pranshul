#!/usr/bin/env python
from pranshul.srv import gps_srv,gps_srvRequest,gps_srvResponse
import serial
import numpy as np
import rospy
ser = serial.Serial('/dev/ttyUSB0',baudrate=4800)
ser.flushInput()
def gps(req):
    while True:
    	a= ser.readline()
    	a = a.decode("utf-8")
    	nmeaobj = np.array(a.split(","))
    	if nmeaobj[0] == "$GPRMC":
        	Latitude = float(nmeaobj[3])
        	Longitude = float(nmeaobj[5])
		return gps_srvResponse(Latitude,Longitude)
def gps_server():
    rospy.init_node('gps_server')
    s = rospy.Service('gps',gps_srv,gps)
    rospy.spin()
if __name__ == "__main__":
    gps_server()
