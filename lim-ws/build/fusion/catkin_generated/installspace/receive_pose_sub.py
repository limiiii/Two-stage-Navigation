#!/usr/bin/python
# coding=utf-8
import rospy
from geometry_msgs.msg import PoseStamped
#获取前端发布在话题/target_pose上的目标信息,并将位姿信息按行写入文件goals.txt
def pose_callback(message):

    with open('/home/rob/lim_ws/src/fusion/scripts/goals.txt', 'a+') as file:
        px = str(message.pose.position.x) + ' '
        py = str(message.pose.position.y) + ' '
        oz = str(message.pose.orientation.z) + ' '
        ow = str(message.pose.orientation.w) + '\n'

        file.write(px)
        file.write(py)
        file.write(oz)
        file.write(ow)
        print('write done!')

if __name__ == '__main__':

    rospy.init_node('pose_listener')
    rospy.Subscriber('/target_pose', PoseStamped, pose_callback, queue_size=5)
    print('start subscribing...')

    rospy.spin() 