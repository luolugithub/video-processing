# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午4:53
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : add_random_noise2img.py
# @Software: PyCharm
import cv2
import random

img = cv2.imread('/home/luolu/PycharmProjects/video-processing/out_frames/00122.png', 1)
imgInfo = img.shape
height = imgInfo[0] - 1  # 防止越界
width = imgInfo[1] - 1

temp = 1000  # 噪声点的个数
for i in range(0, temp):
    if random.randint(1, temp) % 2 == 0:
        img[random.randint(0, height), random.randint(0, width)] = (255, 255, 255)
    if random.randint(1, temp) % 2 != 0:
        img[random.randint(0, height), random.randint(0, width)] = (0, 0, 0)
cv2.imshow('dst', img)
# cv2.imwrite('noise.jpg', img)

cv2.waitKey(0)
