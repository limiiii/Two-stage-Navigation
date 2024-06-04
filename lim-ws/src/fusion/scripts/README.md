'''仿真环境下根据语言进行导航方法研究'''

0. 关键可执行文件：
	servevrs.py        #开启各类服务节点，包括捕获摄像头图像、是否到达目标、发布导航点、获取前端发布的导航点、获取yolo检测框结果等
	pre_load.py        #根据pose中存储的导航点进行初次导航，获取目标点的图像和深度图，以供后续仿真导航使用
	test_main_xxx.py   #各种方法的消融实验（clip网络、cliplim网络、dijkstra算法、orien算法）


1. cliplim       #修改clip网络后，添加了深度信息的depth_Transformer的融合网络
	my_net_test.py #进入虚拟环境(source /home/yang/anaconda3/bin/activate pytorch3.8)仿真环境中的测试图片，测试模型性能
	nets.clip.py   #修改后的网络
	
2. clip-pytorch     #原网络，用以对比测试

3. images/small_house #存储仿真环境中目标点的图像


4.24修改dijkstra+cliplim+orien：
	348行添加 target_list.append("otherfurniture")
	146行 n = len(cliplim[0])
	187行修改判断条件if k in orientation_set and maximun < Q[i][k]:
	
	最好的参数：depth_feature * 0.01; dis = dis * 1.0
