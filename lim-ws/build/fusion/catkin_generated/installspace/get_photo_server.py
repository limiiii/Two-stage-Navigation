#!/usr/bin/python
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
        self.sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.get_image)
        self.server = rospy.Service("/getphoto", get_photo, self.save_image)
        self.count = 0
        self.save_path = '/home/rob/lim_ws/src/fusion/scripts/images/'
        self.save_name = 'target_image'
        rospy.loginfo("GetPhotoServer start!")
        
    def get_image(self, image):
        #将ros格式的图像转为cv格式
        cv_bridge = CvBridge()
        self.image = cv_bridge.imgmsg_to_cv2(image, desired_encoding='passthrough')

    def save_image(self, req):
        res = get_photoResponse()
        image_name = self.save_name + str(self.count) + '.jpg'
        image_file = os.path.join(self.save_path, image_name)
        cv2.imwrite(image_file, self.image)
        self.count += 1

        res.is_done = True
        return res