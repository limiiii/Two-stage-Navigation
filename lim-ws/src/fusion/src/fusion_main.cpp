#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/PointCloud2.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>
#include <iostream>
#include "autoware_msgs/PointsImage.h"
using namespace std;


void pointCloudCallback(const autoware_msgs::PointsImagePtr& msg)
{
    for(int i=0;i<307200;i++){
        float x = msg->distance[i];
	ROS_INFO("distance of %d:%f", i, x);
}

    ROS_INFO("SUCCESSED");

}


int main(int argc, char** argv)
{
    ros::init(argc, argv, "fusion");

    ros::NodeHandle nh;

    // 订阅点云像素坐标话题
    ros::Subscriber pointCloudSub = nh.subscribe("/points_image", 1, pointCloudCallback);

    ros::spin();

    return 0;
}

