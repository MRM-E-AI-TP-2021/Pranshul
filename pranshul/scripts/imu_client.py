#!/usr/bin/env python
import sys
import rospy
from pranshul.srv import *
 
def Imu():
    rospy.wait_for_service('imu')
    try:
        imu = rospy.ServiceProxy('imu',imu)
	a = imu()
	print(a.angle())
    except rospy.ServiceException:
        print( "Service call failed" )
  
if __name__ == "__main__":
    Imu()
