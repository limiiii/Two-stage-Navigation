#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-
import torch
import clip
from PIL import Image
import numpy as np
import rospy
import openai
from chatgpt_server import Chatgptserver
from geometry_msgs.msg import PoseStamped
from fusion.srv import nav_result, nav_resultResponse
from fusion.srv import get_photo, get_photoResponse

#记录前端选取的节点的位姿及其对应图片
def get_image_pose_dict(path):
    image_pose_dict = {}
    with open(path, 'r') as f:
        count = 0
        for line in f:
            room_list = []
            data = line.split()
            room_list.append(float(data[0]))
            room_list.append(float(data[1]))
            room_list.append(float(data[2]))
            room_list.append(float(data[3]))
            print("get line success!")
            image_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/target_image'+str(count)+'.jpg'
            image_pose_dict[image_path] = room_list
            count += 1
    print("create dict success!")
    return image_pose_dict

def get_probs_array(item_list, image_pose_dict):
    probs_arrays = []
    device = "cpu"

    for index, image_dir in enumerate(image_pose_dict):
        print(f"第{index}次循环")
        model, preprocess = clip.load("ViT-B/32", device=device)
        image = preprocess(Image.open(image_dir)).unsqueeze(0).to(device)
        text = clip.tokenize([item for item in item_list]).to(device)
        with torch.no_grad():
            image_features = model.encode_image(image)
            text_features = model.encode_text(text)
            logits_per_image, logits_per_text = model(image, text)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()
            print("Label probs:", probs)
            probs_arrays.append(probs)
    
    probs_array = np.vstack(probs_arrays)
    return probs_array

def pub_pose(target_pose_list):
    #接受列表，依次执行导航，可以参考pre_load.py中的pub_pose
    r = rospy.Rate(1)
    R = rospy.Rate(0.15)
    for index, target_pose in enumerate(target_pose_list):
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x = target_pose[0]
        pose.pose.position.y = target_pose[1]
        pose.pose.position.z = 0.0
        pose.pose.orientation.z = target_pose[2]
        pose.pose.orientation.w = target_pose[3]
        pose.pose.orientation.x = 0.0
        pose.pose.orientation.y = 0.0
        pub.publish(pose)
        res_result = nav_resultResponse()
        #res_photo = get_photoResponse()
        is_first = True
        while True:
        #到达终点时候推出循环，否则一直等待
            if is_first == True:
            #为避免接受上次导航结束时未及时更新的信息，首次导航时添加个间歇时间5s
                print("正在前往第{}个目标.".format(index))
                R.sleep()
                is_first = False
            r.sleep()
            res_result = target_client.call()
            if res_result.isget == True:
            #到达目标点，保存关联模型训练数据、保存图片
                print("get destination :", index)
                R.sleep()
                #res_photo = photo_client.call()
                #if res_photo.is_done == True:
                    #print("save photo success!")
                #else:
                    #print("save photo unsuccess")
                break
    print("Navigation completed")

    

if __name__ == '__main__':
    rospy.init_node('test_main')
    rospy.sleep(1)
    gpt = Chatgptserver()
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5)
    target_client = rospy.ServiceProxy("/gettarget", nav_result)
    target_client.wait_for_service()
    #photo_client = rospy.ServiceProxy("/getphoto", get_photo)
    #photo_client.wait_for_service()

    #初始化所有节点
    image_pose_dict = get_image_pose_dict('/home/yang/lim-ws/src/fusion/scripts/pose/small_house/goals.txt')

    #将自然语言指令转换成'目标列表'
    #发送消息Go straight ahead to the chair, then turn back and go straight ahead, When you reach the cabinet, turn right and stop near the television.给ChatGPT并获取回复
    language_instruction = input("input your instruction:")
    target_list = gpt.chat_with_gpt(language_instruction)
    print("ChatGPT:", target_list)
    target_pose_list = []

    probs_array = get_probs_array(target_list, image_pose_dict)
    #获取目标物一列中概率最大的行索引，行索引的值对应着“图像/导航点”
    for index, target in enumerate(target_list):
        col_index = target_list.index(target)
        col = probs_array[:, col_index]
        max_value_index = np.argmax(col)
        print(f"第{index}个目标物{target}对应节点为{max_value_index}，其概率为{probs_array[max_value_index][col_index]}")
        #通过保存的‘图像’-‘pose’字典来获取目标点的pose
        image_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/target_image'+str(max_value_index)+'.jpg'
        target_pose_list.append(image_pose_dict[image_path])
    
    #发布导航人物，执行导航
    pub_pose(target_pose_list)