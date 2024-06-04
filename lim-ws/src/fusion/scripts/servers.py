#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
sys.path.append('/home/yang/lim-ws/src/fusion/scripts/')
import rospy
from yolo_result_server import YoloResultServer
from point_image_server import MovementServer
from get_target_service import GettargetServer
from yolo_model_server import YoloModelServer
from get_photo_server import GetPhotoServer
from fusion.srv import BBox, BBoxResponse, BBoxRequest
from fusion.srv import movement, movementResponse, movementRequest
if __name__ == "__main__":
    rospy.init_node('servers_node')
    #server1返回检测结果，server2返回距离目标物的旋转、距离信息
    server1 = YoloResultServer()
    server2 = MovementServer()
    #server3返回是否到达目标点，server4返回关联模型训练所需训练集
    server3 = GettargetServer()
    server4 = YoloModelServer()
    #server5保存当前检测图像，用于可视化
    server5 = GetPhotoServer()
    print("open servers success！waiting...")
    rospy.spin()