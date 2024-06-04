#!/home/yang/anaconda3/envs/pytorch3.8/bin/python
# -*- coding: utf-8 -*-
import heapq
import torch
import clip
from PIL import Image
import numpy as np
import rospy
from chatgpt_server import Chatgptserver
from geometry_msgs.msg import PoseStamped
from fusion.srv import nav_result, nav_resultResponse

from torchvision import transforms
from pkg_resources import packaging
from cliplim.nets.clip import CLIP
from typing import Any, Union, List
from cliplim.utils.utils import get_configs
from cliplim.utils.utils_aug import resize, center_crop
from cliplim.nets.simple_tokenizer import SimpleTokenizer as _Tokenizer, tokenize

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

class Solution:
    def __init__(self):
        self.inf = 5000
        ##仿真环境小屋拓扑图
        self.G = [[0, 7, 100, 100, 100, 100, 100, 6, 5],
                  [7, 0, 100, 7, 100, 100, 7, 9, 6],
                  [100, 100, 0, 7, 6, 11, 10, 100, 100],
                  [100, 7, 7, 0, 100, 9, 7, 100, 10],
                  [100, 100, 6, 100, 0, 7, 12, 100, 100],
                  [100, 100, 11, 9, 7, 0, 100, 100, 100],
                  [100, 7, 10, 7, 12, 100, 0, 14, 100],
                  [6, 9, 100, 100, 100, 100, 14, 0, 100],
                  [5, 6, 100, 10, 100, 100, 100, 100, 0]]
        self.neighbormap = {}
        self.init_neighbormap()
        #self.check_neighbor_output()

    def init_neighbormap(self):
        for i in range(len(self.G)):
            flag = False
            for j in range(len(self.G[i])):
                if flag == False and self.G[i][j] < 100 and self.G[i][j] != 0:
                    self.neighbormap[i] = [j]
                    flag = True
                elif self.G[i][j] < 100 and self.G[i][j] != 0:
                    self.neighbormap[i].append(j)
                else:
                    continue
        print("init neighbormap success!")

    def check_neighbor_output(self):
        print("输出节点及其邻居：")
        for key, value in self.neighbormap.items():
            print("key =", key, "value =", value)

    def dijkstra(self):
        n = len(self.G)  # 图的顶点数量
        result = []
        
        for source in range(n):
            dist = [self.inf] * n  # 存储源点到各个顶点的最短距离
            visited = [False] * n  # 标记顶点是否被访问过
            dist[source] = 0  # 源点到自身的距离为0
            
            # 创建一个优先队列，按照距离的增序排列，每个元素存储距离和顶点编号
            pq = [(0, source)]
            heapq.heapify(pq)
            
            while pq:
                u_dist, u = heapq.heappop(pq)

                if visited[u]:
                    continue
                
                visited[u] = True  # 将顶点标记为已访问
                
                # 遍历与顶点u相邻的顶点
                for v in range(n):
                    if self.G[u][v] != 0 and not visited[v]:
                        new_dist = dist[u] + self.G[u][v]  # u到v的距离
                        
                        if new_dist < dist[v]:
                            dist[v] = new_dist  # 更新最短距离
                            heapq.heappush(pq, (dist[v], v))  # 将v加入优先队列
            result.append(dist)
        # 使用softmax对每一行进行归一化
        for i in range(len(result)):
            row = result[i]
            sumexp = sum(row)
            row[:] = [-(value / sumexp) for value in row]
        return result

    def computeQ_getpath(self, cliplim, dis, startnode):
        n = len(cliplim[0])
        m = len(dis)
        print(n)
        print(m)
        Q = [[-self.inf] * m for _ in range(n + 1)]
        path = []
        maximun = -self.inf
        maxindex = startnode

        for i in range(m):
            Q[0][i] = dis[startnode][i]
            if maximun < dis[startnode][i]:
                maximun = dis[startnode][i]
                maxindex = i

        visited = set()
        ans_set = set()
        que = [maxindex]

        for i in range(1, n + 1):
            que.append(maxindex)
            visited.add(maxindex)
            row = dis[maxindex]
            row = sorted(row)
            secondmax = row[-2]
            while que:
                nodev = que.pop(0)
                
                Q[i][nodev] = max(Q[i][nodev], Q[i - 1][nodev] * 0.7 + cliplim[nodev][i - 1])
                neighbor = self.neighbormap[nodev]

                for neighbor_k in neighbor:
                    Q[i][nodev] = max(Q[i][nodev], Q[i][neighbor_k] * 0.8 + dis[nodev][neighbor_k])
                    if neighbor_k not in visited:
                        que.append(neighbor_k)
                        visited.add(neighbor_k)
                if(nodev == maxindex):
                    Q[i][nodev] += secondmax / 3

            maximun = -self.inf
            curindex = 0
            for k in range(m):
                if k == 0:
                    if k != maxindex and maximun < Q[i][k]:
                        maximun = Q[i][k]
                        curindex = k
                #判断是否在方位指示的解集之中，概率更大且跟上一点不同则更新最大值
                elif k not in ans_set and maximun < Q[i][k]:
                    maximun = Q[i][k]
                    curindex = k
            maxindex = curindex
            ans_set.add(maxindex)

            if len(visited) == m:
                print("Q数组第", i, "行计算成功！本次循环使Q取得最大值的节点为-----", maxindex + 1)
                path.append(maxindex)

            visited.clear()

        print("检查计算的Q值：")
        for row in Q:
            print(*("{:.5f}".format(x) for x in row))

        return path
    
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
            #print("get line success!")
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
        print(f"第{index}次循环")
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
                break
    print("Navigation completed")

if __name__ == '__main__':
    rospy.init_node('test_main_d_cliplim')
    rospy.sleep(1)
    gpt = Chatgptserver()
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=5)
    target_client = rospy.ServiceProxy("/gettarget", nav_result)
    target_client.wait_for_service()
    #初始化所有节点
    image_pose_dict = get_image_pose_dict('/home/yang/lim-ws/src/fusion/scripts/pose/small_house/goals.txt')

    #将自然语言指令转换成'目标列表'
    #发送消息Go straight ahead to the chair, then turn back and go straight ahead, When you reach the cabinet, turn right and stop near the television.给ChatGPT并获取回复
    language_instruction = input("input your instruction:")
    target_list = gpt.chat_with_gpt(language_instruction)
    print("ChatGPT:", target_list)
    target_pose_list = []
    #（语义目标， 图片）-->clip网络输出；(网络输出概率，最短路径dis)论文方法加权概率与距离-->
    clipresult = get_probs_array(target_list, image_pose_dict)
    s = Solution()
    dis = s.dijkstra()

    # 检查dis是否正确初始化，Q计算是否正确
    print("输出距离代价矩阵：")
    for row in dis:
        print(*("{:.4f}".format(x) for x in row))

    path = s.computeQ_getpath(clipresult, dis, 8)

    #获取目标物一列中概率最大的行索引，行索引的值对应着“图像/导航点”
    for index, target in enumerate(path):
        image_path = '/home/yang/lim-ws/src/fusion/scripts/images/small_house/target_image'+str(target)+'.jpg'
        target_pose_list.append(image_pose_dict[image_path])
    print("done!")
    #执行导航
    #pub_pose(target_pose_list)