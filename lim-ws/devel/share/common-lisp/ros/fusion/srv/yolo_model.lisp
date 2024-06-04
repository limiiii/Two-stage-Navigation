; Auto-generated. Do not edit!


(cl:in-package fusion-srv)


;//! \htmlinclude yolo_model-request.msg.html

(cl:defclass <yolo_model-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass yolo_model-request (<yolo_model-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yolo_model-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yolo_model-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<yolo_model-request> is deprecated: use fusion-srv:yolo_model-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yolo_model-request>) ostream)
  "Serializes a message object of type '<yolo_model-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yolo_model-request>) istream)
  "Deserializes a message object of type '<yolo_model-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yolo_model-request>)))
  "Returns string type for a service object of type '<yolo_model-request>"
  "fusion/yolo_modelRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo_model-request)))
  "Returns string type for a service object of type 'yolo_model-request"
  "fusion/yolo_modelRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yolo_model-request>)))
  "Returns md5sum for a message object of type '<yolo_model-request>"
  "413fba5d33e359512198fd983aafb45c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yolo_model-request)))
  "Returns md5sum for a message object of type 'yolo_model-request"
  "413fba5d33e359512198fd983aafb45c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yolo_model-request>)))
  "Returns full string definition for message of type '<yolo_model-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yolo_model-request)))
  "Returns full string definition for message of type 'yolo_model-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yolo_model-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yolo_model-request>))
  "Converts a ROS message object to a list"
  (cl:list 'yolo_model-request
))
;//! \htmlinclude yolo_model-response.msg.html

(cl:defclass <yolo_model-response> (roslisp-msg-protocol:ros-message)
  ((Class
    :reader Class
    :initarg :Class
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (xmid
    :reader xmid
    :initarg :xmid
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (ymid
    :reader ymid
    :initarg :ymid
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass yolo_model-response (<yolo_model-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yolo_model-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yolo_model-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fusion-srv:<yolo_model-response> is deprecated: use fusion-srv:yolo_model-response instead.")))

(cl:ensure-generic-function 'Class-val :lambda-list '(m))
(cl:defmethod Class-val ((m <yolo_model-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fusion-srv:Class-val is deprecated.  Use fusion-srv:Class instead.")
  (Class m))

(cl:ensure-generic-function 'xmid-val :lambda-list '(m))
(cl:defmethod xmid-val ((m <yolo_model-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fusion-srv:xmid-val is deprecated.  Use fusion-srv:xmid instead.")
  (xmid m))

(cl:ensure-generic-function 'ymid-val :lambda-list '(m))
(cl:defmethod ymid-val ((m <yolo_model-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fusion-srv:ymid-val is deprecated.  Use fusion-srv:ymid instead.")
  (ymid m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yolo_model-response>) ostream)
  "Serializes a message object of type '<yolo_model-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'Class))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'Class))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'xmid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    ))
   (cl:slot-value msg 'xmid))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'ymid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    ))
   (cl:slot-value msg 'ymid))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yolo_model-response>) istream)
  "Deserializes a message object of type '<yolo_model-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'Class) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'Class)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'xmid) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'xmid)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'ymid) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'ymid)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yolo_model-response>)))
  "Returns string type for a service object of type '<yolo_model-response>"
  "fusion/yolo_modelResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo_model-response)))
  "Returns string type for a service object of type 'yolo_model-response"
  "fusion/yolo_modelResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yolo_model-response>)))
  "Returns md5sum for a message object of type '<yolo_model-response>"
  "413fba5d33e359512198fd983aafb45c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yolo_model-response)))
  "Returns md5sum for a message object of type 'yolo_model-response"
  "413fba5d33e359512198fd983aafb45c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yolo_model-response>)))
  "Returns full string definition for message of type '<yolo_model-response>"
  (cl:format cl:nil "string[] Class~%int64[] xmid~%int64[] ymid~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yolo_model-response)))
  "Returns full string definition for message of type 'yolo_model-response"
  (cl:format cl:nil "string[] Class~%int64[] xmid~%int64[] ymid~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yolo_model-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'Class) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'xmid) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'ymid) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yolo_model-response>))
  "Converts a ROS message object to a list"
  (cl:list 'yolo_model-response
    (cl:cons ':Class (Class msg))
    (cl:cons ':xmid (xmid msg))
    (cl:cons ':ymid (ymid msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'yolo_model)))
  'yolo_model-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'yolo_model)))
  'yolo_model-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo_model)))
  "Returns string type for a service object of type '<yolo_model>"
  "fusion/yolo_model")