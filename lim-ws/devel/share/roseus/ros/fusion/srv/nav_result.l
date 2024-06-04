;; Auto-generated. Do not edit!


(when (boundp 'fusion::nav_result)
  (if (not (find-package "FUSION"))
    (make-package "FUSION"))
  (shadow 'nav_result (find-package "FUSION")))
(unless (find-package "FUSION::NAV_RESULT")
  (make-package "FUSION::NAV_RESULT"))
(unless (find-package "FUSION::NAV_RESULTREQUEST")
  (make-package "FUSION::NAV_RESULTREQUEST"))
(unless (find-package "FUSION::NAV_RESULTRESPONSE")
  (make-package "FUSION::NAV_RESULTRESPONSE"))

(in-package "ROS")





(defclass fusion::nav_resultRequest
  :super ros::object
  :slots ())

(defmethod fusion::nav_resultRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass fusion::nav_resultResponse
  :super ros::object
  :slots (_isget ))

(defmethod fusion::nav_resultResponse
  (:init
   (&key
    ((:isget __isget) nil)
    )
   (send-super :init)
   (setq _isget __isget)
   self)
  (:isget
   (&optional (__isget :null))
   (if (not (eq __isget :null)) (setq _isget __isget)) _isget)
  (:serialization-length
   ()
   (+
    ;; bool _isget
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _isget
       (if _isget (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _isget
     (setq _isget (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass fusion::nav_result
  :super ros::object
  :slots ())

(setf (get fusion::nav_result :md5sum-) "9bda93c4597d4f36521d8edb72019720")
(setf (get fusion::nav_result :datatype-) "fusion/nav_result")
(setf (get fusion::nav_result :request) fusion::nav_resultRequest)
(setf (get fusion::nav_result :response) fusion::nav_resultResponse)

(defmethod fusion::nav_resultRequest
  (:response () (instance fusion::nav_resultResponse :init)))

(setf (get fusion::nav_resultRequest :md5sum-) "9bda93c4597d4f36521d8edb72019720")
(setf (get fusion::nav_resultRequest :datatype-) "fusion/nav_resultRequest")
(setf (get fusion::nav_resultRequest :definition-)
      "---
bool isget

")

(setf (get fusion::nav_resultResponse :md5sum-) "9bda93c4597d4f36521d8edb72019720")
(setf (get fusion::nav_resultResponse :datatype-) "fusion/nav_resultResponse")
(setf (get fusion::nav_resultResponse :definition-)
      "---
bool isget

")



(provide :fusion/nav_result "9bda93c4597d4f36521d8edb72019720")


