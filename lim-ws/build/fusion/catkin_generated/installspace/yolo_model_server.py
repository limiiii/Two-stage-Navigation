#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
#sys.path.append('../../../../devel/lib/python2.7/dist-packages/')

import rospy
from yolov5_ros_msgs.msg import BoundingBoxes
from fusion.srv import yolo_model, yolo_modelResponse
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge
# import os
from std_msgs.msg import Float32MultiArray

class YoloModelServer:
    def __init__(self):
        self.sub = rospy.Subscriber("/yolov5/BoundingBoxes", BoundingBoxes, self.get_result)

        self.server = rospy.Service("/YoloModel", yolo_model, self.detect_result)
        self.yolo_result = BoundingBoxes()
        rospy.loginfo("YoloResultServer start!")
        
    def get_result(self, Boxes):
        self.yolo_result = Boxes

    def detect_result(self, req):
        res = yolo_modelResponse()
        for box in self.yolo_result.bounding_boxes:
            # if box.Class != 'person':
            #     print("len is:", len(res.xmid))
            #     res.Class.append(box.Class)
            #     xmid = (box.xmin + box.xmax) / 2
            #     ymid = (box.ymin + box.ymax) / 2
            #     res.xmid.append(xmid)
            #     res.ymid.append(ymid)
            #     print("return class:", box.Class)
            print("len is:", len(res.xmid))
            res.Class.append(box.Class)
            xmid = (box.xmin + box.xmax) / 2
            ymid = (box.ymin + box.ymax) / 2
            res.xmid.append(xmid)
            res.ymid.append(ymid)
            print("return class:", box.Class)
        return res