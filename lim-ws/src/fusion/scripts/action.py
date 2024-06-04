#!/usr/bin/python3
# coding=utf-8
import rospy
from geometry_msgs.msg import PoseStamped
from fusion.srv import yolo_model, yolo_modelResponse
import math
from fusion.srv import get_photo, get_photoResponse
#根据receive_pose_sub中订阅并保存得到的goals.txt目标点进行导航；通过gettaeget服务节点判断是否完成单次导航，

def my_main():
    #获取检测结果
    res_yolo = yolo_modelResponse()
    res_yolo = model_client.call()
    find_nearest_point(res_yolo.Class, res_yolo.xmid, res_yolo.ymid)
    #保存图片
    res_photo = get_photoResponse()
    res_photo = photo_client.call()

    if res_photo.is_done == True:
        print("save photo success!")
    else:
        print("save photo unsuccess")

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
    with open('/home/yang/lim-ws/src/fusion/scripts/train_model.txt', 'a+') as file:
        for k in range(n):
            print(Class[k], result[k])
            file.write(Class[k])
            file.write(" ")
            file.write(result[k])
            file.write('\n')
    print("write done!")

if __name__ == '__main__':
    rospy.init_node('test_pub_goal')
    rospy.sleep(1)

    #创建服务，用于获取关联模型“训练集”、保存“检测结果图”
    model_client = rospy.ServiceProxy("/YoloModel", yolo_model)
    model_client.wait_for_service()
    photo_client = rospy.ServiceProxy("/getphoto", get_photo)
    photo_client.wait_for_service()

    my_main()
    rospy.spin()
