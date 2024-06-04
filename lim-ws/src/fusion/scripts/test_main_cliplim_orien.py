#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-
import torch
from PIL import Image
import numpy as np
import rospy
from chatgpt_server import Chatgptserver
from chatgpt_server2 import Chatgptserver2
from geometry_msgs.msg import PoseStamped
from fusion.srv import nav_result, nav_resultResponse

from torchvision import transforms
from pkg_resources import packaging
from cliplim.nets.clip import CLIP
from typing import Any, Union, List
from cliplim.utils.utils import get_configs
from cliplim.utils.utils_aug import resize, center_crop
from cliplim.nets.simple_tokenizer import SimpleTokenizer as _Tokenizer, tokenize
import tf.transformations as tf

def preprocess(image, size):
    w, h = size
    iw, ih = image.size
    if(iw >= w and ih >= h):
        letterbox_image = False
    else:
        letterbox_image = True
    if letterbox_image:
        '''resize image with unchanged aspect ratio using padding'''
        scale = min(w/iw, h/ih)
        nw = int(iw*scale)
        nh = int(ih*scale)

        image = image.resize((nw,nh), Image.BICUBIC)
        new_image = Image.new('RGB', size, (128,128,128))
        new_image.paste(image, ((w-nw)//2, (h-nh)//2))
    else:
        if h == w:
            new_image = resize(image, h)
        else:
            new_image = resize(image, [h ,w])
        new_image = center_crop(new_image, [h ,w])
    return new_image

def tokenize(texts: Union[str, List[str]], context_length: int = 77, truncate: bool = False) -> Union[torch.IntTensor, torch.LongTensor]:
    if isinstance(texts, str):
        texts = [texts]
    _tokenizer = _Tokenizer()
    sot_token = _tokenizer.encoder["<|startoftext|>"]
    eot_token = _tokenizer.encoder["<|endoftext|>"]
    all_tokens = [[sot_token] + _tokenizer.encode(text) + [eot_token] for text in texts]
    if packaging.version.parse(torch.__version__) < packaging.version.parse("1.8.0"):
        result = torch.zeros(len(all_tokens), context_length, dtype=torch.long)
    else:
        result = torch.zeros(len(all_tokens), context_length, dtype=torch.int)
    for i, tokens in enumerate(all_tokens):
        if len(tokens) > context_length:
            if truncate:
                tokens = tokens[:context_length]
                tokens[-1] = eot_token
            else:
                raise RuntimeError(f"Input {texts[i]} is too long for context length {context_length}")
        result[i, :len(tokens)] = torch.tensor(tokens)
    return result

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
            image_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/target_image'+str(count)+'.jpg'
            image_pose_dict[image_path] = room_list
            count += 1
    print("create dict success!")
    return image_pose_dict

def get_probs_array(item_list, image_pose_dict):
    config = get_configs("openai/VIT-B-32")
    model = CLIP(**config)
    model.load_state_dict(torch.load("/home/yang/lim-ws/src/fusion/scripts/cliplim/logs/cliplim_4.19_fined.pth"))
    model.eval()
    image_size = [224, 224]
    device = "cpu"
    transform = transforms.ToTensor()
    probs_arrays = []

    for index, image_dir in enumerate(image_pose_dict):

        image = preprocess(Image.open(image_dir), image_size)
        image_tensor = torch.unsqueeze(transform(image), 0).to(device)

        depth_picture = image_dir[:68] + '_depth' + image_dir[68:]
        depth_image = preprocess(Image.open(depth_picture), image_size)
        depth_image_tensor = torch.unsqueeze(transform(depth_image), 0).to(device)
        #将原本是单通道的深度图扩张到3通道
        depth_image_tensor = depth_image_tensor.expand(1,3,224,224)
        with torch.no_grad():
            logits_per_image, logits_per_text = model(image_tensor, item_list, depth_image_tensor)
            probs = logits_per_image.softmax(dim=-1).cpu().numpy()
            print(f"第{index}次循环, Label probs ={probs}")
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

def getorientation_set(path, target_pose_index, orientation):
    poselist = []
    with open(path, 'r') as f:
        for line in f:
            room_list = []
            data = line.split()
            room_list.append(float(data[0]))
            room_list.append(float(data[1]))
            room_list.append(float(data[2]))
            room_list.append(float(data[3]))
            poselist.append(room_list)
    targetpose = poselist[target_pose_index]
    zwpose_target = [0, 0, targetpose[2], targetpose[3]]
    xypose_target = [targetpose[0], targetpose[1]]
    rpy = tf.euler_from_quaternion(zwpose_target)
    theta = rpy[2] #获得偏航角y
    #print("偏航角为：{}".format(theta))
    result = []
    for index, item in enumerate(poselist):
        if target_pose_index == index:
            result.append(index)
        item = item[:2]
        if orientation == '0':
            result.append(index)
            continue
        if item == xypose_target:
            continue
        xypose = np.array([item[0], item[1]])
        TransformM = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        xypose_targetnp = np.array(xypose_target)
        #通过公式计算获得B在A下的坐标pose
        pose = np.dot(TransformM, (xypose - xypose_targetnp))
        #print("转换后的pose为:{}".format(pose))
        if orientation == '1':
            if pose[0] >= 0: #正前方
                result.append(index)
        elif orientation == '2':#正后方
            if pose[0] <= 0:
                result.append(index)
        elif orientation == '3':#正左方
            if pose[1] >= 0:
                result.append(index)
        elif orientation == '4':#正右方
            if pose[1] <=0:
                result.append(index)
    return result

if __name__ == '__main__':
    rospy.init_node('test_main_cliplim_o')
    rospy.sleep(1)
    gpt = Chatgptserver()
    gpt2 = Chatgptserver2()
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5)
    target_client = rospy.ServiceProxy("/gettarget", nav_result)
    target_client.wait_for_service()
    path = '/home/yang/lim-ws/src/fusion/scripts/pose/small_house/goals.txt'
    #photo_client = rospy.ServiceProxy("/getphoto", get_photo)
    #photo_client.wait_for_service()

    #初始化所有节点
    image_pose_dict = get_image_pose_dict(path)
    print("--------------------------------starting cliplim_orienttion process-----------------------------------")
    #将自然语言指令转换成'目标列表'
    #发送消息Go straight ahead to the chair, then turn back and go straight ahead, When you reach the cabinet, turn right and stop near the television.给ChatGPT并获取回复
    language_instruction = input("input your instruction:")
    target_list = gpt.chat_with_gpt(language_instruction)
    orientation_list = gpt2.chat_with_gpt(language_instruction)
    print("ChatGPT:", target_list)
    print("orientation_list:", orientation_list)
    target_pose_list = []
    #获取目标物一列中概率最大的行索引，行索引的值对应着“图像/导航点”
    probs_array = get_probs_array(target_list, image_pose_dict)
    target_pose_index = 4                                                             ##--------------设置用于方位判断的初始点，以便根据初始位姿筛选导航点!!!!!!!
    result_point = []
    #获取目标物一列中概率最大的行索引，行索引的值对应着“图像/导航点”
    for index, target in enumerate(target_list):
        orientation_set = getorientation_set(path, target_pose_index, orientation_list[index])

        col_index = target_list.index(target)
        col = probs_array[:, col_index]
        max_value_index = np.argmax(col)
        while max_value_index not in orientation_set:
            col[max_value_index] = 0
            max_value_index = np.argmax(col)
        #print(f"第{index + 1}个目标物{target}可能解集为{orientation_set}, 求得目标为{max_value_index}，其概率为{probs_array[max_value_index][col_index]}")
        result_point.append(max_value_index + 1)
        target_pose_index = max_value_index
        #通过保存的‘图像’-‘pose’字典来获取目标点的pose
        image_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/target_image'+str(max_value_index)+'.jpg'
        target_pose_list.append(image_pose_dict[image_path])
    print("target is: ", result_point)
    #发布导航人物，执行导航
    print("starting navigation......")
    #pub_pose(target_pose_list)