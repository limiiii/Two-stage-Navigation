# Install script for directory: /home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/yang/lim-ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/yang/lim-ws/build/aws-robomaker-small-house-world-ros1/catkin_generated/installspace/aws_robomaker_small_house_world.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_house_world/cmake" TYPE FILE FILES
    "/home/yang/lim-ws/build/aws-robomaker-small-house-world-ros1/catkin_generated/installspace/aws_robomaker_small_house_worldConfig.cmake"
    "/home/yang/lim-ws/build/aws-robomaker-small-house-world-ros1/catkin_generated/installspace/aws_robomaker_small_house_worldConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_house_world" TYPE FILE FILES "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/aws_robomaker_small_house_world" TYPE DIRECTORY FILES
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/launch"
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/models"
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/worlds"
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/maps"
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/photos"
    "/home/yang/lim-ws/src/aws-robomaker-small-house-world-ros1/routes"
    )
endif()

