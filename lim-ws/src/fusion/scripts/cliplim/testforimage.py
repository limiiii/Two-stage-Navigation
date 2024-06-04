#!/usr/bin/python3
# coding=utf-8
import cv2

# 读取图像
image = cv2.imread("/home/yang/lim-ws/src/fusion/scripts/my-clip-pytorch-main/test_depth_img.png")

# 获取图像的通道数
channels = image.shape[2]

print(image.shape[0])
print(image.shape[1])
print(image.shape[2])
