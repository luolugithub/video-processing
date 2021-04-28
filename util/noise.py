# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午5:03
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : noise.py
# @Software: PyCharm
import numpy as np
import random
import cv2


def sp_noise(image, prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    # cv.imshow("gasuss", out)
    return out

# img = cv2.imread('/home/luolu/PycharmProjects/video-processing/out_frames/00122.png')
# # img_noise = sp_noise(img, 0.9)
# img_noise = gasuss_noise(img, mean=0, var=0.001)
# img_f = img + img_noise
# cv2.imshow('dst', img_f)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()