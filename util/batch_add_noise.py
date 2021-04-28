# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午2:36
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_add_noise.py
# @Software: PyCharm
import cv2
import numpy as np
import glob
import os

from PIL.Image import Image
out_path = "/home/luolu/PycharmProjects/video-processing/encoded_frame/"

for filename in sorted(glob.glob("/home/luolu/PycharmProjects/video-processing/out_frames/*.jpg")):
    # print(filename)
    img = cv2.imread(filename)
    base_name = os.path.basename(filename)
    print(base_name)
    # filename, file_ext = os.path.splitext(filename)
    # print(filename + '.jpg')
    # Generate Gaussian noise
    # gauss = np.random.normal(0, 1, img.size)
    # gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
    # # Add the Gaussian noise to the image
    # img_gauss = cv2.add(img, gauss)
    # Speckle Noise
    gauss = np.random.normal(0, 1, img.size)
    gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
    noise = img + img * gauss
    # save img
    cv2.imwrite(out_path + base_name, noise)

