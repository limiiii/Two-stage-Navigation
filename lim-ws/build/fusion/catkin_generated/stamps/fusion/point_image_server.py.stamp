#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
#sys.path.append('../../../../devel/lib/python2.7/dist-packages/')

import rospy
from autoware_msgs.msg import PointsImage
from cv_bridge import CvBridge,CvBridgeError
from fusion.srv import movement, movementResponse, movementRequest

class MovementServer:
    def __init__(self):
        self.sub = rospy.Subscriber("/points_image", PointsImage, self.get_result, queue_size=1)
        self.server = rospy.Service("/Movement", movement, self.getdis)
        self.dis_result = PointsImage()
        rospy.loginfo("MovementServer start!")
        

    def get_result(self, msg):
        self.dis_result = msg

    def getdis(self, req):
        res = movementResponse()
        
        xmid = (req.xmax + req.xmin) // 2
        ymid = (req.ymax + req.ymin) // 2
        #设置遍历区域大小
        xlen = (req.xmax - req.xmin) // 4
        ylen = (req.ymax - req.ymin) // 4
        
        avg_dis = 0
        count = 0
        for x in range(xmid - xlen, xmid + xlen):
            for y in range(ymid - ylen, ymid + ylen):
                if self.dis_result.distance[x + y * 640]!=0:
                    avg_dis += self.dis_result.distance[x + y * 640]
                    count += 1
    
        distance = avg_dis / (count *100)
        radian = (xmid - 320) * 0.0036813
        
        res.distance = distance
        res.radian = radian
        return res

