<<<<<<< HEAD
Two stage Navigation文档
===============
Ubuntu20.04下，在仿真环境中根据随机生成的自然语言导航指令进行导航，搭建属于自己的服务器.

* 融合重训练多模态网络CLIP，适应室内中光线变换大的环境
* 采用多传感器融合，融合单目相机中采集到的认知信和多线激光采集到的感知信息，使移动机器人能正确地导航到目标半米内。
* 引入方位优化模块，通过提取自然语言指令中的方位信息，筛选掉噪声点。
* 通过距离、融合网络和方位优化共同筛选导航点，提高正确率
* 通过动态规划的方法加权计算匹配值。


基础测试
------------
* chatgpt_server.py中设置api，检查是否过期
	// 提取指令中的目标信息

* chatgpt_server2.py中设置api，检查是否过期
	// 提取指令中的方位信息，用0、1、2、3、4表示无方位、前方、后方、左边、右边


* 全模块代码
   	// test_main_dijkstra_cliplim_orien.py
* LM_Nav对比代码
	// test_main_dijkstra_clip.py （clip模型+无方位模块）
* 消融实验代码
	// test_main_dijkstra_cliplim.py（无方位模块）
	// test_main_cliplim_orien.py（无距离模块）
	// test_main_dijkstra_clip_orien.py（使用clip模型）


* 1-5.png为家庭仿真环境下所创建的二维栅格导航地图，需要初始化各导航点的位姿、图像及程序中用邻接表表示的拓扑图


