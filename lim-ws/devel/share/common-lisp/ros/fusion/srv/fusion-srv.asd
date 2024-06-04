
(cl:in-package :asdf)

(defsystem "fusion-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BBox" :depends-on ("_package_BBox"))
    (:file "_package_BBox" :depends-on ("_package"))
    (:file "get_photo" :depends-on ("_package_get_photo"))
    (:file "_package_get_photo" :depends-on ("_package"))
    (:file "movement" :depends-on ("_package_movement"))
    (:file "_package_movement" :depends-on ("_package"))
    (:file "nav_result" :depends-on ("_package_nav_result"))
    (:file "_package_nav_result" :depends-on ("_package"))
    (:file "yolo_model" :depends-on ("_package_yolo_model"))
    (:file "_package_yolo_model" :depends-on ("_package"))
  ))