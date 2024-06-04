# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "fusion: 0 messages, 5 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(fusion_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_custom_target(_fusion_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "fusion" "/home/yang/lim-ws/src/fusion/srv/BBox.srv" ""
)

get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_custom_target(_fusion_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "fusion" "/home/yang/lim-ws/src/fusion/srv/movement.srv" ""
)

get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_custom_target(_fusion_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "fusion" "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" ""
)

get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_custom_target(_fusion_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "fusion" "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" ""
)

get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_custom_target(_fusion_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "fusion" "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(fusion
  "/home/yang/lim-ws/src/fusion/srv/BBox.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
)
_generate_srv_cpp(fusion
  "/home/yang/lim-ws/src/fusion/srv/movement.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
)
_generate_srv_cpp(fusion
  "/home/yang/lim-ws/src/fusion/srv/nav_result.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
)
_generate_srv_cpp(fusion
  "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
)
_generate_srv_cpp(fusion
  "/home/yang/lim-ws/src/fusion/srv/get_photo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
)

### Generating Module File
_generate_module_cpp(fusion
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(fusion_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(fusion_generate_messages fusion_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_dependencies(fusion_generate_messages_cpp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_dependencies(fusion_generate_messages_cpp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_dependencies(fusion_generate_messages_cpp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_dependencies(fusion_generate_messages_cpp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_dependencies(fusion_generate_messages_cpp _fusion_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(fusion_gencpp)
add_dependencies(fusion_gencpp fusion_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS fusion_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(fusion
  "/home/yang/lim-ws/src/fusion/srv/BBox.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
)
_generate_srv_eus(fusion
  "/home/yang/lim-ws/src/fusion/srv/movement.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
)
_generate_srv_eus(fusion
  "/home/yang/lim-ws/src/fusion/srv/nav_result.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
)
_generate_srv_eus(fusion
  "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
)
_generate_srv_eus(fusion
  "/home/yang/lim-ws/src/fusion/srv/get_photo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
)

### Generating Module File
_generate_module_eus(fusion
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(fusion_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(fusion_generate_messages fusion_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_dependencies(fusion_generate_messages_eus _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_dependencies(fusion_generate_messages_eus _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_dependencies(fusion_generate_messages_eus _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_dependencies(fusion_generate_messages_eus _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_dependencies(fusion_generate_messages_eus _fusion_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(fusion_geneus)
add_dependencies(fusion_geneus fusion_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS fusion_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(fusion
  "/home/yang/lim-ws/src/fusion/srv/BBox.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
)
_generate_srv_lisp(fusion
  "/home/yang/lim-ws/src/fusion/srv/movement.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
)
_generate_srv_lisp(fusion
  "/home/yang/lim-ws/src/fusion/srv/nav_result.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
)
_generate_srv_lisp(fusion
  "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
)
_generate_srv_lisp(fusion
  "/home/yang/lim-ws/src/fusion/srv/get_photo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
)

### Generating Module File
_generate_module_lisp(fusion
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(fusion_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(fusion_generate_messages fusion_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_dependencies(fusion_generate_messages_lisp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_dependencies(fusion_generate_messages_lisp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_dependencies(fusion_generate_messages_lisp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_dependencies(fusion_generate_messages_lisp _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_dependencies(fusion_generate_messages_lisp _fusion_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(fusion_genlisp)
add_dependencies(fusion_genlisp fusion_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS fusion_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(fusion
  "/home/yang/lim-ws/src/fusion/srv/BBox.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
)
_generate_srv_nodejs(fusion
  "/home/yang/lim-ws/src/fusion/srv/movement.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
)
_generate_srv_nodejs(fusion
  "/home/yang/lim-ws/src/fusion/srv/nav_result.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
)
_generate_srv_nodejs(fusion
  "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
)
_generate_srv_nodejs(fusion
  "/home/yang/lim-ws/src/fusion/srv/get_photo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
)

### Generating Module File
_generate_module_nodejs(fusion
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(fusion_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(fusion_generate_messages fusion_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_dependencies(fusion_generate_messages_nodejs _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_dependencies(fusion_generate_messages_nodejs _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_dependencies(fusion_generate_messages_nodejs _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_dependencies(fusion_generate_messages_nodejs _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_dependencies(fusion_generate_messages_nodejs _fusion_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(fusion_gennodejs)
add_dependencies(fusion_gennodejs fusion_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS fusion_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(fusion
  "/home/yang/lim-ws/src/fusion/srv/BBox.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
)
_generate_srv_py(fusion
  "/home/yang/lim-ws/src/fusion/srv/movement.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
)
_generate_srv_py(fusion
  "/home/yang/lim-ws/src/fusion/srv/nav_result.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
)
_generate_srv_py(fusion
  "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
)
_generate_srv_py(fusion
  "/home/yang/lim-ws/src/fusion/srv/get_photo.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
)

### Generating Module File
_generate_module_py(fusion
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(fusion_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(fusion_generate_messages fusion_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/BBox.srv" NAME_WE)
add_dependencies(fusion_generate_messages_py _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/movement.srv" NAME_WE)
add_dependencies(fusion_generate_messages_py _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/nav_result.srv" NAME_WE)
add_dependencies(fusion_generate_messages_py _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/yolo_model.srv" NAME_WE)
add_dependencies(fusion_generate_messages_py _fusion_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/yang/lim-ws/src/fusion/srv/get_photo.srv" NAME_WE)
add_dependencies(fusion_generate_messages_py _fusion_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(fusion_genpy)
add_dependencies(fusion_genpy fusion_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS fusion_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/fusion
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(fusion_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/fusion
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(fusion_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/fusion
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(fusion_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/fusion
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(fusion_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/fusion
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(fusion_generate_messages_py std_msgs_generate_messages_py)
endif()
