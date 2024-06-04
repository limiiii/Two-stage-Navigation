; Auto-generated. Do not edit!


(cl:in-package fusion-srv)


;//! \htmlinclude nav_result-request.msg.html

(cl:defclass <nav_result-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass nav_result-request (<nav_result-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <nav_result-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'nav_result-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<nav_result-request> is deprecated: use fusion-srv:nav_result-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <nav_result-request>) ostream)
  "Serializes a message object of type '<nav_result-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <nav_result-request>) istream)
  "Deserializes a message object of type '<nav_result-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<nav_result-request>)))
  "Returns string type for a service object of type '<nav_result-request>"
  "fusion/nav_resultRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'nav_result-request)))
  "Returns string type for a service object of type 'nav_result-request"
  "fusion/nav_resultRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<nav_result-request>)))
  "Returns md5sum for a message object of type '<nav_result-request>"
  "9bda93c4597d4f36521d8edb72019720")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'nav_result-request)))
  "Returns md5sum for a message object of type 'nav_result-request"
  "9bda93c4597d4f36521d8edb72019720")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<nav_result-request>)))
  "Returns full string definition for message of type '<nav_result-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'nav_result-request)))
  "Returns full string definition for message of type 'nav_result-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <nav_result-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <nav_result-request>))
  "Converts a ROS message object to a list"
  (cl:list 'nav_result-request
))
;//! \htmlinclude nav_result-response.msg.html

(cl:defclass <nav_result-response> (roslisp-msg-protocol:ros-message)
  ((isget
    :reader isget
    :initarg :isget
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass nav_result-response (<nav_result-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <nav_result-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'nav_result-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<nav_result-response> is deprecated: use fusion-srv:nav_result-response instead.")))

(cl:ensure-generic-function 'isget-val :lambda-list '(m))
(cl:defmethod isget-val ((m <nav_result-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fusion-srv:isget-val is deprecated.  Use fusion-srv:isget instead.")
  (isget m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <nav_result-response>) ostream)
  "Serializes a message object of type '<nav_result-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'isget) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <nav_result-response>) istream)
  "Deserializes a message object of type '<nav_result-response>"
    (cl:setf (cl:slot-value msg 'isget) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<nav_result-response>)))
  "Returns string type for a service object of type '<nav_result-response>"
  "fusion/nav_resultResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'nav_result-response)))
  "Returns string type for a service object of type 'nav_result-response"
  "fusion/nav_resultResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<nav_result-response>)))
  "Returns md5sum for a message object of type '<nav_result-response>"
  "9bda93c4597d4f36521d8edb72019720")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'nav_result-response)))
  "Returns md5sum for a message object of type 'nav_result-response"
  "9bda93c4597d4f36521d8edb72019720")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<nav_result-response>)))
  "Returns full string definition for message of type '<nav_result-response>"
  (cl:format cl:nil "bool isget~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'nav_result-response)))
  "Returns full string definition for message of type 'nav_result-response"
  (cl:format cl:nil "bool isget~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <nav_result-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <nav_result-response>))
  "Converts a ROS message object to a list"
  (cl:list 'nav_result-response
    (cl:cons ':isget (isget msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'nav_result)))
  'nav_result-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'nav_result)))
  'nav_result-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'nav_result)))
  "Returns string type for a service object of type '<nav_result>"
  "fusion/nav_result")