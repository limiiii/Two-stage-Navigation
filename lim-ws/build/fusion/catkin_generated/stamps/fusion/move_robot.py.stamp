#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import rospy
from geometry_msgs.msg import Twist

class MoveRobot:
    def __init__(self):
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
        self.rate = rospy.Rate(10)


    def rotate(self, radian_speed, duration, flag):
        velocity_msg = Twist()
        velocity_msg.linear.x = 0.0
        if flag == True:
            velocity_msg.angular.z = radian_speed
        else:
            velocity_msg.angular.z = -radian_speed
        print("start rotateing...")
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < duration:
            self.velocity_publisher.publish(velocity_msg)
            #self.rate.sleep()
            
        #stop
        velocity_msg.linear.x = 0.0
        velocity_msg.angular.z = 0.0
        self.velocity_publisher.publish(velocity_msg)

    def move(self, linear_speed, duration):
        velocity_msg = Twist()
        velocity_msg.linear.x = linear_speed
        velocity_msg.angular.z = 0
        print("start moving...")
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < duration:
            self.velocity_publisher.publish(velocity_msg)
            #self.rate.sleep()
            
        #stop
        velocity_msg.linear.x = 0.0
        velocity_msg.angular.z = 0.0
        self.velocity_publisher.publish(velocity_msg)
