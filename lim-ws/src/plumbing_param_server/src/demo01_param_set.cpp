#include "ros/ros.h"


/*实现参数的新增与修改
     
     需求：1.首先设置机器人共享的参数，类型、半径
          2.再修改半径 
     实现：通过两套api实现：ros::NodeHandle
                             setparam
                        ros::param
                             set()
*/
 int main(int argc, char *argv[])
 {
    setlocale(LC_ALL,"");
    //初始化ROS节点
    ros::init(argc,argv,"set_param_c");

    //创建ROS节点句柄
    ros::NodeHandle nh;



    //实现参数的新增操作---------------------第一个参数表示健，第二个参数表示值，nh.setParam()==ros::param::set()
        //方案1：nh
        nh.setParam("type","xiaohuang");
        nh.setParam("radius",0.15);

        //方案2：ros：：param
        ros::param::set("type_param","xiaobai");
        ros::param::set("radius_param",0.15);



    //实现参数的修改操作-------------
        //方案1：nh(重复使用相同名称的健即可覆盖原来的健值)
        nh.setParam("type","xiaoxiao");
        nh.setParam("type_param","你好");
        
        //方案2：param
        ros::param::set("radius",1.1);
        ros::param::set("radius_param",1.11);

    return 0;
 }
 