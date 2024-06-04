#include "ros/ros.h"
#include "turtlesim/Pose.h"
#include "tf2_ros/transform_broadcaster.h"
#include "geometry_msgs/TransformStamped.h"
#include "tf2/LinearMath/Quaternion.h"
/*发布方：需要订阅乌龟的位姿信息，转换成相对于世界窗体的坐标关系，并发布
  准  备：
        话题：/turtle1/pose
        消息：/turtlesim/Pose
       

   流程：
      1.包含头文件
      2.初始化操作（设置编码、节点、Nodeandle创建）
      3.创建订阅对象。订阅turtle1/pose
      4.回调函数处理订阅的消息：把订阅到的位姿信息转换成坐标相对关系并发布（关键）
      5.spin()
*/

void dopose(const turtlesim::Pose::ConstPtr& pose){ 
    //获取位姿信息，转换成坐标系相对关系，并发布
    //a.创建tf发布对象
     static tf2_ros::TransformBroadcaster pub;
    //b.组织被发布的数据
    geometry_msgs::TransformStamped ts;
    ts.header.frame_id="world";
    ts.child_frame_id="turtle1";
    ts.header.stamp=ros::Time::now();
    //坐标系偏移量设置
    ts.transform.translation.x=pose->x;
    ts.transform.translation.y=pose->y;
    ts.transform.translation.z=0;
    //坐标系四元数:位姿信息中没有四元数，但是2d不存在翻滚、fuyang角度，只有偏航角度，并且因此欧拉角为（0，0，theta）

    tf2::Quaternion qtn;
    qtn.setRPY(0,0,pose->theta);

    ts.transform.rotation.x=qtn.getX();
    ts.transform.rotation.y=qtn.getY();
    ts.transform.rotation.z=qtn.getZ();
    ts.transform.rotation.w=qtn.getW();
    //c.发布
    pub.sendTransform(ts);
}

int main(int argc, char *argv[])
{
    //   1.包含头文件
    //   2.初始化操作（设置编码、节点、Nodeandle创建）
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"dynamic_pub");
    ros::NodeHandle nh;
    //   3.创建订阅对象。订阅turtle1/pose
    ros::Subscriber sub =nh.subscribe("turtle1/pose",100,dopose);
    //   4.回调函数处理订阅的消息：把订阅到的位姿信息转换成坐标相对关系并发布（关键）
    //   5.spin()
    ros::spin();
    return 0;
}


/*结果显示：
    1.roscore启动核心
    2.rosrun turtlesim turtlesim_node 启动乌龟节点
    3.rosrun turtlesim turtle_teleop_key 启动键盘控制乌龟运动

    4.新建窗口启动订阅
      source ./devel/setup.bash
      rosrun tf2_dynamic demo01_dynamic_pub(启动包、节点名称)
    5.可视化
       rviz
        
*/