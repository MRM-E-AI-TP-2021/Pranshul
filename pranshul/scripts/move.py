#!/usr/bin/env python
import sys
import rospy
from pranshul.srv import *
 
def Gps():
    rospy.wait_for_service('gps')
    try:
        gps = rospy.ServiceProxy('gps', gps_srv)
	a = gps()
	return a.Latitude,a.Longitude

    except rospy.ServiceException:
        print( "Service call failed" )
def Imu():
    rospy.wait_for_service('imu')
    try:
        imu = rospy.ServiceProxy('imu',imu)
	a = imu()
	print(a.angle())
    except rospy.ServiceException:
        print( "Service call failed" )

def Distance(lat1,lon1,lat2,lon2):  
     R = 6372800  # Earth radius in meters    
    phi1, phi2 = math.radians(lat1), math.radians(lat2) 
    dphi       = math.radians(lat2 - lat1)
    dlambda    = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1 - a))

latitude_given = 13.34786166
longitude_given = 74.79216999
angle1  = 0
latitude = 0 
longitude = 0 
while True:
        latitude,longitude = Gps()
        X = math.cos(latitude_given)*math.sin(longitude_given-longitude)
        Y = math.cos(latitude)*math.sin(latitude_given) - math.sin(latitude)*math.cos(latitude_given)*math.cos(longitude_given-longitude)
        angle1 = math.atan2(X,Y)
        
    angle2 = Imu()
    print(angle1 - angle2)
    print("Distance = %f" %Distance(latitude,longitude,latitude_given,longitude_given))
    sleep(0.01)
    while (abs(angle2-angle1)>5):
        if(abs(angle2-angle1)<180 and angle1>angle2):
            print("mr")
        elif(abs(angle2-angle1)<180 and angle1<angle2):
            print("ml")
        if(abs(angle2-angle1)>180 and angle1>angle2):
            print("ml")
        elif(abs(angle2-angle1)>180 and angle1<angle2):
            print("mr")
    while "Distance = %f" %Distance(latitude,longitude,latitude_given,longitude_given)>3 and abs(angle2-angle1)>5):
        print("move forward")
        angle2 = Imu()      
