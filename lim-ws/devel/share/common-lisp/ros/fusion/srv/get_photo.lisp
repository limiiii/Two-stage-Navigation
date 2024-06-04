; Auto-generated. Do not edit!


(cl:in-package fusion-srv)


;//! \htmlinclude get_photo-request.msg.html

(cl:defclass <get_photo-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass get_photo-request (<get_photo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <get_photo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'get_photo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<get_photo-request> is deprecated: use fusion-srv:get_photo-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <get_photo-request>) ostream)
  "Serializes a message object of type '<get_photo-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <get_photo-request>) istream)
  "Deserializes a message object of type '<get_photo-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<get_photo-request>)))
  "Returns string type for a service object of type '<get_photo-request>"
  "fusion/get_photoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'get_photo-request)))
  "Returns string type for a service object of type 'get_photo-request"
  "fusion/get_photoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<get_photo-request>)))
  "Returns md5sum for a message object of type '<get_photo-request>"
  "ccf1bf44aca57c0fac7595ea9e4b924c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'get_photo-request)))
  "Returns md5sum for a message object of type 'get_photo-request"
  "ccf1bf44aca57c0fac7595ea9e4b924c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<get_photo-request>)))
  "Returns full string definition for message of type '<get_photo-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'get_photo-request)))
  "Returns full string definition for message of type 'get_photo-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <get_photo-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <get_photo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'get_photo-request
))
;//! \htmlinclude get_photo-response.msg.html

(cl:defclass <get_photo-response> (roslisp-msg-protocol:ros-message)
  ((is_done
    :reader is_done
    :initarg :is_done
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass get_photo-response (<get_photo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <get_photo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'get_photo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<get_photo-response> is deprecated: use fusion-srv:get_photo-response instead.")))

(cl:ensure-generic-function 'is_done-val :lambda-list '(m))
(cl:defmethod is_done-val ((m <get_photo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fusion-srv:is_done-val is deprecated.  Use fusion-srv:is_done instead.")
  (is_done m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <get_photo-response>) ostream)
  "Serializes a message object of type '<get_photo-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'is_done) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <get_photo-response>) istream)
  "Deserializes a message object of type '<get_photo-response>"
    (cl:setf (cl:slot-value msg 'is_done) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<get_photo-response>)))
  "Returns string type for a service object of type '<get_photo-response>"
  "fusion/get_photoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'get_photo-response)))
  "Returns string type for a service object of type 'get_photo-response"
  "fusion/get_photoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<get_photo-response>)))
  "Returns md5sum for a message object of type '<get_photo-response>"
  "ccf1bf44aca57c0fac7595ea9e4b924c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'get_photo-response)))
  "Returns md5sum for a message object of type 'get_photo-response"
  "ccf1bf44aca57c0fac7595ea9e4b924c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<get_photo-response>)))
  "Returns full string definition for message of type '<get_photo-response>"
  (cl:format cl:nil "bool is_done~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'get_photo-response)))
  "Returns full string definition for message of type 'get_photo-response"
  (cl:format cl:nil "bool is_done~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <get_photo-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <get_photo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'get_photo-response
    (cl:cons ':is_done (is_done msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'get_photo)))
  'get_photo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'get_photo)))
  'get_photo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'get_photo)))
  "Returns string type for a service object of type '<get_photo>"
  "fusion/get_photo")