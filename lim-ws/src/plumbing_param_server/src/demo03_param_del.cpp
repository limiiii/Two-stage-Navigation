#include "ros/ros.h"
  /*演示参数的删除，使用两套api
    ros::NodeHandle
        deleteParam("键")
        根据键删除参数，删除成功，返回 true，否则(参数不存在)，返回 false

    ros::param
        del("键")
        根据键删除参数，删除成功，返回 true，否则(参数不存在)，返回 false
  */


int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"param_del_c");
    ros::NodeHandle nh;

    //方案1:NodeHandle----------------------------------------
    bool flag1 = nh.deleteParam("radius");
    if(flag1){
        ROS_INFO("删除flag1成功！");
    }
    else{
        ROS_INFO("flag1删除失败！");
    }
    bool flag2 = nh.deleteParam("radius_param");
    if(flag2){
        ROS_INFO("删除flag2成功！");
    }
    else{
        ROS_INFO("flag2删除失败！");
    }

    //方案2:ros::param-----------------------------------------
    nh.setParam("test1",1);
    nh.setParam("test2",2);
    bool flag3=ros::param::del("test1");
    if(flag3){
        ROS_INFO("删除flag1成功！");
    }
    else{
        ROS_INFO("flag1删除失败！");
    }




    return 0;
}
