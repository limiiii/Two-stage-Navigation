// Generated by gencpp from file fusion/nav_resultRequest.msg
// DO NOT EDIT!


#ifndef FUSION_MESSAGE_NAV_RESULTREQUEST_H
#define FUSION_MESSAGE_NAV_RESULTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace fusion
{
template <class ContainerAllocator>
struct nav_resultRequest_
{
  typedef nav_resultRequest_<ContainerAllocator> Type;

  nav_resultRequest_()
    {
    }
  nav_resultRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::fusion::nav_resultRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fusion::nav_resultRequest_<ContainerAllocator> const> ConstPtr;

}; // struct nav_resultRequest_

typedef ::fusion::nav_resultRequest_<std::allocator<void> > nav_resultRequest;

typedef boost::shared_ptr< ::fusion::nav_resultRequest > nav_resultRequestPtr;
typedef boost::shared_ptr< ::fusion::nav_resultRequest const> nav_resultRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fusion::nav_resultRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fusion::nav_resultRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace fusion

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::fusion::nav_resultRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fusion::nav_resultRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::nav_resultRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::nav_resultRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::nav_resultRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::nav_resultRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fusion::nav_resultRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::fusion::nav_resultRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::fusion::nav_resultRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fusion/nav_resultRequest";
  }

  static const char* value(const ::fusion::nav_resultRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fusion::nav_resultRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::fusion::nav_resultRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fusion::nav_resultRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct nav_resultRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fusion::nav_resultRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::fusion::nav_resultRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // FUSION_MESSAGE_NAV_RESULTREQUEST_H