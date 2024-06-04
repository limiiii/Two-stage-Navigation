// Generated by gencpp from file fusion/get_photoRequest.msg
// DO NOT EDIT!


#ifndef FUSION_MESSAGE_GET_PHOTOREQUEST_H
#define FUSION_MESSAGE_GET_PHOTOREQUEST_H


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
struct get_photoRequest_
{
  typedef get_photoRequest_<ContainerAllocator> Type;

  get_photoRequest_()
    {
    }
  get_photoRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::fusion::get_photoRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fusion::get_photoRequest_<ContainerAllocator> const> ConstPtr;

}; // struct get_photoRequest_

typedef ::fusion::get_photoRequest_<std::allocator<void> > get_photoRequest;

typedef boost::shared_ptr< ::fusion::get_photoRequest > get_photoRequestPtr;
typedef boost::shared_ptr< ::fusion::get_photoRequest const> get_photoRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fusion::get_photoRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fusion::get_photoRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace fusion

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::fusion::get_photoRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fusion::get_photoRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::get_photoRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::get_photoRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::get_photoRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::get_photoRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fusion::get_photoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::fusion::get_photoRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::fusion::get_photoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fusion/get_photoRequest";
  }

  static const char* value(const ::fusion::get_photoRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fusion::get_photoRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::fusion::get_photoRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fusion::get_photoRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct get_photoRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fusion::get_photoRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::fusion::get_photoRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // FUSION_MESSAGE_GET_PHOTOREQUEST_H
