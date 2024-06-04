#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
sys.path.append('/home/rob/lim_ws/src/')
import time
import cv2
import rospy
import math

from geometry_msgs.msg import PoseStamped, Twist
from cv_bridge import CvBridge
from std_msgs.msg import Bool
import base64
from std_srvs.srv import Trigger, TriggerResponse

from yolov5_ros_msgs.msg import BoundingBox, BoundingBoxes
from fusion.srv import BBox, BBoxResponse, BBoxRequest
from fusion.srv import movement, movementResponse, movementRequest
from move_robot import MoveRobot

if __name__ =="__main__":

        rospy.init_node('main_node')
        #请求语音识别结果：目标列表target_list和动作列表action_list
        target_list = ["bottle", "lim", "person"]
        #target_list = ["person", "lim", "bottle"]
        for item in target_list:
            print("target confirmed:", item)
            req_yolo = BBoxRequest()
            req_yolo.target = item
            
            # 请求推理结果

            yolo_client = rospy.ServiceProxy("/YoloResult", BBox)
            yolo_client.wait_for_service()
            while True:
                yolo_res = yolo_client.call(req_yolo)
                #处理过程中，当成功匹配当前目标物则会将.num置111
                if yolo_res.num == 111:
                    break
                #rospy.sleep(0.1)
            rospy.loginfo("detect successfully")

            # 请求并计算点云获取的旋转和距离结果
            req_movement = movementRequest()
            req_movement.xmin = yolo_res.xmin
            req_movement.ymin = yolo_res.ymin
            req_movement.xmax = yolo_res.xmax
            req_movement.ymax = yolo_res.ymax

            move_client = rospy.ServiceProxy("/Movement", movement)
            move_client.wait_for_service()
            move_res = move_client.call(req_movement)
            flag = False
            if move_res.radian < 0:
                flag = True

            radian_speed = 0.5
            duration_radian = abs(move_res.radian)/ radian_speed

            linear_speed = 0.3
            duration_linear = move_res.distance/ linear_speed
            print("rotate and move duration is:", duration_radian, duration_linear)
            
            #控制小车进行移动
            robot = MoveRobot()
            robot.rotate(radian_speed, duration_radian-0.1, flag)
            robot.move(linear_speed, duration_linear-1)
            print("--------get destination!--------")
            rospy.sleep(2)

        

