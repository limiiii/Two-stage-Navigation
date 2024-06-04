;; Auto-generated. Do not edit!


(when (boundp 'fusion::get_photo)
  (if (not (find-package "FUSION"))
    (make-package "FUSION"))
  (shadow 'get_photo (find-package "FUSION")))
(unless (find-package "FUSION::GET_PHOTO")
  (make-package "FUSION::GET_PHOTO"))
(unless (find-package "FUSION::GET_PHOTOREQUEST")
  (make-package "FUSION::GET_PHOTOREQUEST"))
(unless (find-package "FUSION::GET_PHOTORESPONSE")
  (make-package "FUSION::GET_PHOTORESPONSE"))

(in-package "ROS")





(defclass fusion::get_photoRequest
  :super ros::object
  :slots ())

(defmethod fusion::get_photoRequest
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

(defclass fusion::get_photoResponse
  :super ros::object
  :slots (_is_done ))

(defmethod fusion::get_photoResponse
  (:init
   (&key
    ((:is_done __is_done) nil)
    )
   (send-super :init)
   (setq _is_done __is_done)
   self)
  (:is_done
   (&optional (__is_done :null))
   (if (not (eq __is_done :null)) (setq _is_done __is_done)) _is_done)
  (:serialization-length
   ()
   (+
    ;; bool _is_done
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _is_done
       (if _is_done (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _is_done
     (setq _is_done (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass fusion::get_photo
  :super ros::object
  :slots ())

(setf (get fusion::get_photo :md5sum-) "ccf1bf44aca57c0fac7595ea9e4b924c")
(setf (get fusion::get_photo :datatype-) "fusion/get_photo")
(setf (get fusion::get_photo :request) fusion::get_photoRequest)
(setf (get fusion::get_photo :response) fusion::get_photoResponse)

(defmethod fusion::get_photoRequest
  (:response () (instance fusion::get_photoResponse :init)))

(setf (get fusion::get_photoRequest :md5sum-) "ccf1bf44aca57c0fac7595ea9e4b924c")
(setf (get fusion::get_photoRequest :datatype-) "fusion/get_photoRequest")
(setf (get fusion::get_photoRequest :definition-)
      "---
bool is_done

")

(setf (get fusion::get_photoResponse :md5sum-) "ccf1bf44aca57c0fac7595ea9e4b924c")
(setf (get fusion::get_photoResponse :datatype-) "fusion/get_photoResponse")
(setf (get fusion::get_photoResponse :definition-)
      "---
bool is_done

")



(provide :fusion/get_photo "ccf1bf44aca57c0fac7595ea9e4b924c")


