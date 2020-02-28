#!/usr/bin/env python
import sys
import rospy
from pranshul.srv import *
 
def Gps():
    rospy.wait_for_service('gps')
    try:
        gps = rospy.ServiceProxy('gps', gps_srv)
	a = gps()
	print(a.Latitude)
	print(a.Longitude)
    except rospy.ServiceException:
        print( "Service call failed" )
  
if __name__ == "__main__":
    Gps()
