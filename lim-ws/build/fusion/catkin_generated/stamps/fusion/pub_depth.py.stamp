#!/usr/bin/python
# -*- coding:utf-8 -*-
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
from tf.transformations import quaternion_matrix

class LidarCameraFusionNode:
    def __init__(self):
        rospy.init_node('lidar_camera_fusion_node')
        self.bridge = CvBridge()
        # 创建点云图像发布者
        self.points_image_publisher = rospy.Publisher('/projected_image', Image, queue_size=5)
        #初始化深度图像信息
        self.image_size = (640, 480)
        self.height =self.image_size[1]
        self.width = self.image_size[0]
        self.image = Image()
        self.image.header.frame_id = 'usb_cam'
        self.image.height = self.height
        self.image.width = self.width
        self.image.encoding = '32FC1'
        self.image.step = self.width * 4
        self.image.data = [0] * (self.height * self.width)

        self.load_calibration_data()
        # 订阅激光雷达发布的点云话题
        rospy.Subscriber('/lslidar_point_cloud', PointCloud2, self.lidar_callback)


    def load_calibration_data(self):
        # 加载外参文件， CameraExtrinsicMat, CameraMat, DistCoeff 矩阵
        calibration_file = '/home/rob/lim_ws/src/fusion/scripts/camera_lidar_fusion.yml'
        calibration_data = cv2.FileStorage(calibration_file, cv2.FILE_STORAGE_READ)

        self.camera_extrinsic_mat = calibration_data.getNode('CameraExtrinsicMat').mat()
        self.camera_mat = calibration_data.getNode('CameraMat').mat()
        self.dist_coeff = calibration_data.getNode('DistCoeff').mat()
        print("camera_extrinsic_mat", self.camera_extrinsic_mat)
        print(type(self.camera_extrinsic_mat))
        print("camera_mat", self.camera_mat)
        print("dist_coeff", self.dist_coeff)
        print("load params success!")
        calibration_data.release()


    def lidar_callback(self, velodyne_data):
        result = np.zeros((self.image_size[1], self.image_size[0]), dtype=np.uint16)

        inv_R = np.transpose(self.camera_extrinsic_mat[0:3, 0:3])
        inv_T = -np.dot(inv_R, self.camera_extrinsic_mat[0:3, 3])

        n = velodyne_data.height
        m = velodyne_data.width
        data = np.frombuffer(velodyne_data.data, dtype=np.float32).reshape((n, m, -1))

        for i in range(n):
            for j in range(m):
                dataptr = data[i, j]

                point = np.array([dataptr[0], dataptr[1], dataptr[2]], dtype=np.float64)
                point = np.dot(point, inv_R.T) + inv_T.T

                if point[2] <= 0:
                    continue

                # 计算归一化平面上的坐标
                tmp_x = point[0] / point[2]
                tmp_y = point[1] / point[2]
                r2 = tmp_x * tmp_x + tmp_y * tmp_y
                tmp_dist = 1 + self.dist_coeff[0][0] * r2 + self.dist_coeff[0][1] * r2 * r2 + self.dist_coeff[0][4] * r2 * r2 * r2

                # 计算畸变后的像素坐标
                image_x = tmp_x * tmp_dist + 2 * self.dist_coeff[0][2] * tmp_x * tmp_y + self.dist_coeff[0][3] * (r2 + 2 * tmp_x * tmp_x)
                image_y = tmp_y * tmp_dist + self.dist_coeff[0][2] * (r2 + 2 * tmp_y * tmp_y) + 2 * self.dist_coeff[0][3] * tmp_x * tmp_y

                # 将像素坐标转换为图像坐标
                image_x = self.camera_mat[0, 0] * image_x + self.camera_mat[0, 2]
                image_y = self.camera_mat[1, 1] * image_y + self.camera_mat[1, 2]

                px = int(image_x + 0.5)
                py = int(image_y + 0.5)
                if 0 <= px < self.image_size[0] and 0 <= py < self.image_size[1] and (result[py, px] == 0 or (result[py, px] / 100.0 > point[2])):
                    result[py, px] = point[2] * 100 + 0.5


        depth_image = np.reshape(result, (self.height, self.width))
        #depth_image = np.rot90(depth_image, k=1)
        self.image.data = depth_image.astype(np.float32).tobytes()
        # 将结果发布到话题
        self.points_image_publisher.publish(self.image)
        print("pub image done!")


        # 将 self.image 转换为 PIL.Image 格式的图像
        cv_image = self.bridge.imgmsg_to_cv2(self.image, desired_encoding='passthrough')
        file_name = '/home/rob/lim_ws/src/fusion/scripts/saved_image.jpg'  # 设置保存的文件名
        cv2.imwrite(file_name, cv_image)

    def run(self):
        # 循环等待回调函数
        rospy.spin()

if __name__ == '__main__':
    fusion_node = LidarCameraFusionNode()
    fusion_node.run()