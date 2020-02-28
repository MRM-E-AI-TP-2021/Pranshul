#!/usr/bin/env python
import numpy as np
import rospy
import serial
from std_msgs.msg import Float64
ser = serial.Serial('/dev/ttyUSB0',baudrate=4800)
ser.flushInput()
def talker():
    Latitude = 0
    Longitude = 0
    pub = rospy.Publisher('gps_pub',Float64, queue_size=20)
    rospy.init_node('gps_pub', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    while True:
    	a= ser.readline()
    	a = a.decode("utf-8")
    	nmeaobj = np.array(a.split(","))
    	if nmeaobj[0] == "$GPRMC":
        	Latitude = float(nmeaobj[3])
        	Longitude = float(nmeaobj[5])
        pub.publish(Latitude)
	pub.publish(Longitude)
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
