;; Auto-generated. Do not edit!


(when (boundp 'fusion::yolo_model)
  (if (not (find-package "FUSION"))
    (make-package "FUSION"))
  (shadow 'yolo_model (find-package "FUSION")))
(unless (find-package "FUSION::YOLO_MODEL")
  (make-package "FUSION::YOLO_MODEL"))
(unless (find-package "FUSION::YOLO_MODELREQUEST")
  (make-package "FUSION::YOLO_MODELREQUEST"))
(unless (find-package "FUSION::YOLO_MODELRESPONSE")
  (make-package "FUSION::YOLO_MODELRESPONSE"))

(in-package "ROS")





(defclass fusion::yolo_modelRequest
  :super ros::object
  :slots ())

(defmethod fusion::yolo_modelRequest
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

(defclass fusion::yolo_modelResponse
  :super ros::object
  :slots (_Class _xmid _ymid ))

(defmethod fusion::yolo_modelResponse
  (:init
   (&key
    ((:Class __Class) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:xmid __xmid) (make-array 0 :initial-element 0 :element-type :integer))
    ((:ymid __ymid) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _Class __Class)
   (setq _xmid __xmid)
   (setq _ymid __ymid)
   self)
  (:Class
   (&optional __Class)
   (if __Class (setq _Class __Class)) _Class)
  (:xmid
   (&optional __xmid)
   (if __xmid (setq _xmid __xmid)) _xmid)
  (:ymid
   (&optional __ymid)
   (if __ymid (setq _ymid __ymid)) _ymid)
  (:serialization-length
   ()
   (+
    ;; string[] _Class
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _Class)) 4
    ;; int64[] _xmid
    (* 8    (length _xmid)) 4
    ;; int64[] _ymid
    (* 8    (length _ymid)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _Class
     (write-long (length _Class) s)
     (dolist (elem _Class)
       (write-long (length elem) s) (princ elem s)
       )
     ;; int64[] _xmid
     (write-long (length _xmid) s)
     (dotimes (i (length _xmid))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _xmid i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _xmid i)) (= (length ((elt _xmid i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _xmid i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _xmid i) . bv) 1) -1) s))
             ((and (class (elt _xmid i)) (= (length ((elt _xmid i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _xmid i) . bv) 0) s)
              (write-long (if (>= (elt _xmid i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _xmid i) s)(write-long (if (>= (elt _xmid i) 0) 0 #xffffffff) s)))
       )
     ;; int64[] _ymid
     (write-long (length _ymid) s)
     (dotimes (i (length _ymid))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _ymid i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _ymid i)) (= (length ((elt _ymid i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _ymid i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _ymid i) . bv) 1) -1) s))
             ((and (class (elt _ymid i)) (= (length ((elt _ymid i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _ymid i) . bv) 0) s)
              (write-long (if (>= (elt _ymid i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _ymid i) s)(write-long (if (>= (elt _ymid i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _Class
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Class (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _Class i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; int64[] _xmid
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _xmid (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _xmid i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _xmid i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;; int64[] _ymid
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _ymid (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _ymid i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _ymid i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(defclass fusion::yolo_model
  :super ros::object
  :slots ())

(setf (get fusion::yolo_model :md5sum-) "413fba5d33e359512198fd983aafb45c")
(setf (get fusion::yolo_model :datatype-) "fusion/yolo_model")
(setf (get fusion::yolo_model :request) fusion::yolo_modelRequest)
(setf (get fusion::yolo_model :response) fusion::yolo_modelResponse)

(defmethod fusion::yolo_modelRequest
  (:response () (instance fusion::yolo_modelResponse :init)))

(setf (get fusion::yolo_modelRequest :md5sum-) "413fba5d33e359512198fd983aafb45c")
(setf (get fusion::yolo_modelRequest :datatype-) "fusion/yolo_modelRequest")
(setf (get fusion::yolo_modelRequest :definition-)
      "---
string[] Class
int64[] xmid
int64[] ymid

")

(setf (get fusion::yolo_modelResponse :md5sum-) "413fba5d33e359512198fd983aafb45c")
(setf (get fusion::yolo_modelResponse :datatype-) "fusion/yolo_modelResponse")
(setf (get fusion::yolo_modelResponse :definition-)
      "---
string[] Class
int64[] xmid
int64[] ymid

")



(provide :fusion/yolo_model "413fba5d33e359512198fd983aafb45c")


