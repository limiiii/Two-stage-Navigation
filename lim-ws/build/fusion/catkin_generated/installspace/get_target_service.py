#!/usr/bin/python
# -*- coding:utf-8 -*-
#sys.path.append('../../../../devel/lib/python2.7/dist-packages/')

import rospy
from actionlib_msgs.msg import GoalStatusArray
from actionlib_msgs.msg import GoalStatus
from fusion.srv import nav_result, nav_resultResponse
# import tf
# import tf.transformations as tf_trans
# from geometry_msgs.msg import PoseStamped
# from std_msgs.msg import Bool

class GettargetServer:
    #监听/move_base/result话题，判断是否完成导航
    def __init__(self):
        self.sub = rospy.Subscriber('/move_base/status', GoalStatusArray, self.status_callback, queue_size=1)
        self.server = rospy.Service('gettarget', nav_result, self.if_get_target)
        self.latest_status = GoalStatus()
        rospy.loginfo("GettargetServer start!")

    def status_callback(self, msg):
        self.latest_status = msg.status_list
        #print(self.latest_status[0].status)

    def if_get_target(self,req):
        res = nav_resultResponse()
        res.isget = False
        if len(self.latest_status) != 0 and self.latest_status[0].status == 3:
        #if self.latest_status[0].status == 3:
            res.isget = True
        return res

# def pose_callback(self, msg):
#     # 获取机器人当前位姿
#     self.robot_pose = msg.pose
#         # 创建一个TransformListener对象，并等待坐标变换的可用性
#     listener = tf.TransformListener()
#     listener.waitForTransform("/map", "/base_link", rospy.Time(), rospy.Duration(1.0))

#     try:
#         # 进行坐标变换，将机器人位姿从base_link坐标系转换到map坐标系
#         map_pose = listener.transformPose("/map", PoseStamped(header=msg.header, pose=self.robot_pose))
#         # 输出在map坐标系下的位姿
#         print("Robot pose in map frame:")
#         print("Position (x, y, z):", map_pose.pose.position.x, map_pose.pose.position.y, map_pose.pose.position.z)
#         print("Orientation (qx, qy, qz, qw):", map_pose.pose.orientation.x, map_pose.pose.orientation.y,
#               map_pose.pose.orientation.z, map_pose.pose.orientation.w)

#     except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
#         rospy.logwarn("Failed to transform pose.")

# def euclidean_distance(pose1, pose2):
#     # 提取姿态信息
#     quat1 = [pose1.pose.orientation.x, pose1.pose.orientation.y, pose1.pose.orientation.z, pose1.pose.orientation.w]
#     quat2 = [pose2.pose.orientation.x, pose2.pose.orientation.y, pose2.pose.orientation.z, pose2.pose.orientation.w]
#     # 将四元数转换为旋转矩阵
#     matrix1 = tf_trans.quaternion_matrix(quat1)
#     matrix2 = tf_trans.quaternion_matrix(quat2)
#     # 计算旋转矩阵之间的欧氏距离
#     distance = tf_trans.vector_norm(matrix1[:3, 3] - matrix2[:3, 3])

#     return distance
# def if_get_target(self, req):
#     res = targetposeResponse()
#     # 获取目标位姿
#     target_pose = PoseStamped()
#     target_pose.header.frame_id = 'map'
#     target_pose.header.stamp = rospy.Time.now()
#     target_pose.pose.position.x = req.posex
#     target_pose.pose.position.y = req.posey
#     target_pose.pose.orientation.z = req.orientationz
#     target_pose.pose.orientation.w = req.orientationw

#     # 计算目标位姿与当前位姿的欧氏距离
#     distance = euclidean_distance(self.robot_pose, target_pose)
    
#     if(distance < 0.1):
#         res.isget = True
#     else:
#         res.isget = False
#     return res
