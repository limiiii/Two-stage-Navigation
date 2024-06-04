#!/usr/bin/python
# coding=utf-8
import rospy
from geometry_msgs.msg import PoseStamped
from fusion.srv import nav_result, nav_resultResponse
from fusion.srv import yolo_model, yolo_modelResponse
from fusion.srv import get_photo, get_photoResponse
import math
#根据receive_pose_sub中订阅并保存得到的goals.txt目标点进行导航；通过gettaeget服务节点判断是否完成单次导航，


def load_points():
#获取保存在goal_rooms.txt中的 在map坐标系下的导航目标点
    room_list = []
    with open('/home/rob/lim_ws/src/fusion/scripts/goals.txt', 'r') as f:
        for line in f:
            point_pose = PoseStamped()
            data = line.split()
            point_pose.header.frame_id = 'map'
            point_pose.header.stamp = rospy.Time.now()
            point_pose.pose.position.x = float(data[0])
            point_pose.pose.position.y = float(data[1])
            point_pose.pose.orientation.w = float(data[2])
            point_pose.pose.orientation.z =float(data[3])
            room_list.append(point_pose)
            print("get line success!")
    return room_list


def pub_pose(point_list):
#根据导航点 依次执行导航任务
    r = rospy.Rate(1)
    R = rospy.Rate(0.15)
    for index, pose in enumerate(point_list):
        r.sleep()
        pub.publish(pose)
        res_result = nav_resultResponse()
        res_yolo = yolo_modelResponse()
        res_photo = get_photoResponse()
        is_first = True
        while True:
        #到达终点时候推出循环，否则一直等待
            if is_first == True:
            #为避免接受上次导航结束时未及时更新的信息，首次导航时添加个间歇时间5s
                print("move to target:", index)
                R.sleep()
                is_first = False
            r.sleep()
            res_result = target_client.call()
            if res_result.isget == True:
            #到达目标点，保存关联模型训练数据、保存图片
                print("get destination and take picture", index)

                R.sleep()
                res_yolo = model_client.call()
                find_nearest_point(res_yolo.Class, res_yolo.xmid, res_yolo.ymid)
                res_photo = photo_client.call()
                if res_photo.is_done == True:
                    print("save photo success!")
                else:
                    print("save photo unsuccess")
                break
        #for循环内添加旋转、目标检测指令
            
def find_nearest_point(Class, xmid, ymid):
#到达目标点后获取检测结果，提取距离信息创建关联模型的训练集
    n = len(xmid)
    result = []
    print("n = ", n)
    for i in range(n):
        min_dis = float('inf')
        nearest_obj = ""
        for j in range(n):
            if i == j:
                continue
            dis = math.sqrt((xmid[i] - xmid[j])**2 + (ymid[i] - ymid[j])**2)
            if dis < min_dis:
                min_dis = dis
                nearest_obj = Class[j]
        result.append(nearest_obj)
    #将关联结果保存 用于后续训练
    with open('/home/rob/lim_ws/src/fusion/scripts/train_model.txt', 'a+') as file:
        for k in range(n):
            print(Class[k], result[k])
            file.write(Class[k])
            file.write(" ")
            file.write(result[k])
            file.write('\n')
    print("write done!")

if __name__ == '__main__':
    rospy.init_node('pub_pose')
    rospy.sleep(1)
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5)
    point_list = load_points()
    print("publishing the goal")

    #创建服务:用于确认是否到达目标、获取关联模型“训练集”、保存“检测结果图”
    target_client = rospy.ServiceProxy("/gettarget", nav_result)
    target_client.wait_for_service()
    model_client = rospy.ServiceProxy("/YoloModel", yolo_model)
    model_client.wait_for_service()
    photo_client = rospy.ServiceProxy("/getphoto", get_photo)
    photo_client.wait_for_service()

    pub_pose(point_list)
    rospy.spin()