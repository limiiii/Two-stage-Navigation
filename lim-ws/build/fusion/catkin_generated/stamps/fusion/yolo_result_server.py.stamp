#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
#sys.path.append('../../../../devel/lib/python2.7/dist-packages/')

import rospy
from yolov5_ros_msgs.msg import BoundingBox, BoundingBoxes
from fusion.srv import BBox, BBoxResponse, BBoxRequest

class YoloResultServer:
    def __init__(self):
        self.sub = rospy.Subscriber("/yolov5/BoundingBoxes", BoundingBoxes, self.get_result)
        self.server = rospy.Service("/YoloResult", BBox, self.istarget)
        self.yolo_result = BoundingBoxes()
        rospy.loginfo("YoloResultServer start!")
        

    def get_result(self, Boxes):
        self.yolo_result = Boxes

    def istarget(self, req):
        res = BBoxResponse()
        res.probability = 0
        res.ymin = 0
        res.xmin = 0
        res.xmax = 0
        res.ymax = 0
        res.num = 0
        for box in self.yolo_result.bounding_boxes:
            if box.Class == req.target and box.probability > 0.5 and box.probability > res.probability:
                res.probability = box.probability
                res.ymin = box.ymin
                res.xmin = box.xmin
                res.xmax = box.xmax
                res.ymax = box.ymax
                res.num = 111
        print("find target!")
        return res