#!/usr/bin/python
# coding=utf-8
import rospy
from geometry_msgs.msg import PoseStamped

#测试用，充当前端发布导航点信息
def load_points():
    room_list = []
    with open('/home/rob/lim_ws/src/fusion/scripts/goal_rooms.txt', 'r') as f:
        for line in f:
            room_point = PoseStamped()
            data = line.split()
            room_point.pose.position.x = float(data[0])
            room_point.pose.position.y = float(data[1])
            room_point.pose.orientation.z = float(data[2])
            room_point.pose.orientation.w = float(data[3])
            room_list.append(room_point)
            print("get line success!")
    return room_list

#根据导航点 依次执行导航任务
def pub_pose(point_list):
    r = rospy.Rate(2)
    for pose in point_list:
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = rospy.Time.now()
        goal_pose.pose = pose.pose
        r.sleep()
        pub.publish(goal_pose)
    print("pub done!")

if __name__ == '__main__':
    # 初始化ROS节点
    rospy.init_node('pose_publisher')
    # 创建一个发布器，当做前端发送的位姿消息
    pub = rospy.Publisher("/target_pose", PoseStamped, queue_size=5)
    point_list = load_points()
    print("publishing the goal")
    pub_pose(point_list)
    # 开始循环执行程序
    rospy.spin()