#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
def callback(data):
    print(data)
     
def listener():
    rospy.init_node('gps_sub', anonymous=False) 
    rospy.Subscriber("nmea_serial_driver_node", Float64, callback) 
    rospy.spin() 
if __name__ == '__main__':
    listener()
