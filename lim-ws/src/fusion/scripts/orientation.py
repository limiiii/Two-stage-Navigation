#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-
import tf.transformations as tf
import numpy as np
#orientation == 1表示正前方，覆盖一四象限；2表示后方，覆盖二三象限；3表示左方，覆盖三四象限；4表示右方一二象限
def orientation_set(path, targetpose, orientation):
    poselist = []
    with open(path, 'r') as f:
        for line in f:
            room_list = []
            data = line.split()
            room_list.append(float(data[0]))
            room_list.append(float(data[1]))
            poselist.append(room_list)
    print("get pose success!")
    zwpose_target = [0, 0, targetpose[2], targetpose[3]]
    xypose_target = [targetpose[0], targetpose[1]]
    rpy = tf.euler_from_quaternion(zwpose_target)
    theta = rpy[2] #获得偏航角y
    print("偏航角为：{}".format(theta))
    result = []
    for index, item in enumerate(poselist):
        if orientation == 0:
            result.append(index)
            continue
        if item == xypose_target:
            continue
        xypose = np.array([item[0], item[1]])
        print("第{}个元素入队, (x, y) = :{}".format(index, xypose))
        TransformM = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        xypose_targetnp = np.array(xypose_target)
        #通过公式计算获得B在A下的坐标pose
        pose = np.dot(TransformM, (xypose - xypose_targetnp))
        print("转换后的pose为:{}".format(pose))
        if orientation == 1:
            if pose[0] >= 0: #正前方
                result.append(index)
        elif orientation == 2:#正后方
            if pose[0] <= 0:
                result.append(index)
        elif orientation == 3:#正左方
            if pose[1] >= 0:
                result.append(index)
        elif orientation == 4:#正右方
            if pose[1] <=0:
                result.append(index)
    print("pose result = {}".format(result))
    return result



path = '/home/yang/lim-ws/src/fusion/scripts/pose/small_house/goals.txt'
targetpose = [3.53744, -3.09835, 0.32740, 0.94489]
resultset = orientation_set(path, targetpose, 2)
print(resultset)
