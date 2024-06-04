#!/usr/bin/python3
# coding=utf-8
import rospy
import cv2
from sensor_msgs.msg import Image
from autoware_msgs.msg import PointsImage
from cv_bridge import CvBridge,CvBridgeError

###-------------------------ͼ��͵����ںϿ��ӻ�------------------------------

cv_image = None

def image_callback(image):
    global cv_image
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(image, "bgr8")

def point_cloud_callback(msg):
    global cv_image
    bridge = CvBridge()
    # ��ͼ���ϱ�ǵ�������
    cv_image1 = cv_image

    for i in range(len(msg.distance)):
        # ��Ϊ0��ʱ���ʾ������Ƴɹ�ӳ�䵽����ƽ��
        if msg.distance[i] != 0:
            width = i % 640
            height = i // 640
            # ͨ��ӳ����ͼ����б�㣬���ղ�ͬ�ľ��루��λcm����ǲ�ͬ����ɫ���̡��ơ��졢��
            if msg.distance[i] <= 200:
                cv_image1[height, width] = (90, 255, 25)
                if height>=1 and height<=478 and width >=1 and width <=638:
                    cv_image1[height-1, width] = (90, 255, 25)
                    cv_image1[height, width-1] = (90, 255, 25)
                    cv_image1[height+1, width] = (90, 255, 25)
                    cv_image1[height, width+1] = (90, 255, 25)
            elif msg.distance[i] <= 400:
                cv_image1[height, width] = (235, 242, 38)
                if height>=1 and height<=478 and width >=1 and width <=638:
                    cv_image1[height-1, width] = (235, 242, 38)
                    cv_image1[height, width-1] = (235, 242, 38)
                    cv_image1[height+1, width] = (235, 242, 38)
                    cv_image1[height, width+1] = (235, 242, 38)
            elif msg.distance[i] <= 600:
                cv_image1[height, width] = (255, 35, 25)
                if height>=1 and height<=478 and width >=1 and width <=638:
                    cv_image1[height-1, width] = (255, 35, 25)
                    cv_image1[height, width+1] = (255, 35, 25)
                    cv_image1[height, width-1] = (255, 35, 25)
                    cv_image1[height+1, width] = (255, 35, 25)
            else:
                cv_image1[height, width] = (134, 33, 247)
                if height>=1 and height<=478 and width >=1 and width <=638:
                    cv_image1[height-1, width] = (134, 33, 247)
                    cv_image1[height, width-1] = (134, 33, 247)
                    cv_image1[height, width+1] = (134, 33, 247)
                    cv_image1[height+1, width] = (134, 33, 247)
    # ������Ǻ��ͼ��
    print("fusion_success!")
    fusion_image = bridge.cv2_to_imgmsg(cv_image1, "bgr8")
    pub.publish(fusion_image)


if __name__ == '__main__':
    rospy.init_node("fusion")

    # ����ͼ����
    #rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    rospy.Subscriber("/yolov5/detection_image", Image, image_callback)

    # ���ĵ����������껰��
    rospy.Subscriber("/points_image", PointsImage, point_cloud_callback)

    # ����������
    pub = rospy.Publisher("/fusion_image", Image, queue_size=10)

    rospy.spin()
