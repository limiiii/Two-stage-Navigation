#!/usr/bin/python3
# coding=utf-8
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    try:
        cv_image = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    except Exception as e:
        rospy.logerr(e)
        return

    cv2.imwrite("image2.jpg", cv_image)
    rospy.loginfo("Image saved as image2.jpg")

def main():
    rospy.init_node("image_subscriber")

    # 创建一个订阅者，订阅/camera_image/image_raw话题，回调函数为image_callback
    rospy.Subscriber("/camera/image_raw", Image, image_callback)

    rospy.spin()

if __name__ == '__main__':
    main()