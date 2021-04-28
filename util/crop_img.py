# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午12:58
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : crop_img.py
# @Software: PyCharm
import cv2
img = cv2.imread("/home/luolu/PycharmProjects/video-processing/match_images/cys1.png")
x = 237
y = 60
h = 480
w = 540
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)