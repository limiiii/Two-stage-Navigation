#include "ros/ros.h"

int main(int argc, char  *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"hello_c");

    ROS_INFO("hello");
    return 0;
}
