//1.包含头文件
#include "ros/ros.h"
#include "tf2_ros/transform_listener.h"
#include "tf2/LinearMath/Quaternion.h"
#include "tf2_geometry_msgs/tf2_geometry_msgs.h"
#include "geometry_msgs/TransformStamped.h"
#include "geometry_msgs/PointStamped.h"
#include "geometry_msgs/Twist.h"

/*

需求:
    换算出turtle1相对于turtle2的关系
    2.进一步根据距离计算角速度、线速度

*/
int main(int argc, char *argv[])
{   
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"sub_frames");
    ros::NodeHandle nh;

    tf2_ros::Buffer buffer; 
    tf2_ros::TransformListener listener(buffer);

    //A.创建发布对象（用于发布角速度、线速度）
    ros::Publisher pub=nh.advertise<geometry_msgs::Twist>("/turtle2/cmd_vel",100);

    ros::Rate r(10);
    while (ros::ok())
    {
        try
        {
        //   解析 son1 中的点相对于 son2 的坐标
            geometry_msgs::TransformStamped tfs = buffer.lookupTransform("turtle2","turtle1",ros::Time(0));
            ROS_INFO("Son1 相对于 Son2 的坐标关系:父坐标系ID=%s",tfs.header.frame_id.c_str());  //turtle2
            ROS_INFO("Son1 相对于 Son2 的坐标关系:子坐标系ID=%s",tfs.child_frame_id.c_str());   //turtle1
            ROS_INFO("Son1 相对于 Son2 的坐标关系:x=%.2f,y=%.2f,z=%.2f",
                    tfs.transform.translation.x,
                    tfs.transform.translation.y,
                    tfs.transform.translation.z
                    );
            /*B.根据相对计算并组织速度消息,只需要设置线速度的x、角速度的z
                x=系数 * sqrt(x^2+y^2)
                z=系数 * arctan(对边/邻边)
            */
            geometry_msgs::Twist twist;
            twist.linear.x=0.5*sqrt(pow(tfs.transform.translation.x,2)+pow(tfs.transform.translation.y,2));
            twist.angular.z=4*atan2(tfs.transform.translation.y,tfs.transform.translation.x);
            //C.发布
            pub.publish(twist);
        }
        catch(const std::exception& e)
        {
            // std::cerr << e.what() << '\n';
            ROS_INFO("异常信息:%s",e.what());
        }


        r.sleep();
        // 6.spin
        ros::spinOnce();
    }
    return 0;
}
