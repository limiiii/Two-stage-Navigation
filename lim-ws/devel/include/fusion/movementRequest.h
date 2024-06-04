// Generated by gencpp from file fusion/movementRequest.msg
// DO NOT EDIT!


#ifndef FUSION_MESSAGE_MOVEMENTREQUEST_H
#define FUSION_MESSAGE_MOVEMENTREQUEST_H


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
struct movementRequest_
{
  typedef movementRequest_<ContainerAllocator> Type;

  movementRequest_()
    : xmax(0)
    , xmin(0)
    , ymin(0)
    , ymax(0)  {
    }
  movementRequest_(const ContainerAllocator& _alloc)
    : xmax(0)
    , xmin(0)
    , ymin(0)
    , ymax(0)  {
  (void)_alloc;
    }



   typedef int64_t _xmax_type;
  _xmax_type xmax;

   typedef int64_t _xmin_type;
  _xmin_type xmin;

   typedef int64_t _ymin_type;
  _ymin_type ymin;

   typedef int64_t _ymax_type;
  _ymax_type ymax;





  typedef boost::shared_ptr< ::fusion::movementRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::fusion::movementRequest_<ContainerAllocator> const> ConstPtr;

}; // struct movementRequest_

typedef ::fusion::movementRequest_<std::allocator<void> > movementRequest;

typedef boost::shared_ptr< ::fusion::movementRequest > movementRequestPtr;
typedef boost::shared_ptr< ::fusion::movementRequest const> movementRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::fusion::movementRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::fusion::movementRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::fusion::movementRequest_<ContainerAllocator1> & lhs, const ::fusion::movementRequest_<ContainerAllocator2> & rhs)
{
  return lhs.xmax == rhs.xmax &&
    lhs.xmin == rhs.xmin &&
    lhs.ymin == rhs.ymin &&
    lhs.ymax == rhs.ymax;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::fusion::movementRequest_<ContainerAllocator1> & lhs, const ::fusion::movementRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace fusion

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::fusion::movementRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::fusion::movementRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::movementRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::fusion::movementRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::movementRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::fusion::movementRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::fusion::movementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "05b4d605c3540d174c215ee6e529e83d";
  }

  static const char* value(const ::fusion::movementRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x05b4d605c3540d17ULL;
  static const uint64_t static_value2 = 0x4c215ee6e529e83dULL;
};

template<class ContainerAllocator>
struct DataType< ::fusion::movementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fusion/movementRequest";
  }

  static const char* value(const ::fusion::movementRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::fusion::movementRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 xmax\n"
"int64 xmin\n"
"int64 ymin\n"
"int64 ymax\n"
;
  }

  static const char* value(const ::fusion::movementRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::fusion::movementRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.xmax);
      stream.next(m.xmin);
      stream.next(m.ymin);
      stream.next(m.ymax);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct movementRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::fusion::movementRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::fusion::movementRequest_<ContainerAllocator>& v)
  {
    s << indent << "xmax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmax);
    s << indent << "xmin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmin);
    s << indent << "ymin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymin);
    s << indent << "ymax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymax);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FUSION_MESSAGE_MOVEMENTREQUEST_H