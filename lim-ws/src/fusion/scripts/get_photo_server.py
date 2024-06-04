#!/usr/bin/python3
# -*- coding:utf-8 -*-

#sys.path.append('../../../../devel/lib/python2.7/dist-packages/')

import rospy
from fusion.srv import get_photo, get_photoResponse
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os

class GetPhotoServer:
    def __init__(self):
        self.sub1 = rospy.Subscriber("/camera/image_raw", Image, self.get_image)
        self.sub2 = rospy.Subscriber("/camera/depth/image_raw", Image, self.get_depth_image)
        self.server = rospy.Service("/getphoto", get_photo, self.save_image)
        self.count = 0
        self.save_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/'
        self.save_name = 'target_image'
        rospy.loginfo("GetPhotoServer start!")
    
    def get_depth_image(self, depth_image):
        cv_bridge = CvBridge()
        self.depth_image = cv_bridge.imgmsg_to_cv2(depth_image, desired_encoding='passthrough')

    def get_image(self, image):
        #将ros格式的图像转为cv格式
        cv_bridge = CvBridge()
        self.image = cv_bridge.imgmsg_to_cv2(image, desired_encoding='passthrough')

    def save_image(self, req):
        res = get_photoResponse()
        image_name = self.save_name + str(self.count) + '.jpg'
        depth_image_name = self.save_name +'_depth' + str(self.count) +'.jpg'
        image_file = os.path.join(self.save_path, image_name)
        depth_image_file = os.path.join(self.save_path, depth_image_name)

        cv2.imwrite(image_file, self.image)
        cv2.imwrite(depth_image_file, self.depth_image)

        self.count += 1

        res.is_done = True
        return res