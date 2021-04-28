# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午2:46
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_img_logic.py
# @Software: PyCharm
import cv2
import numpy as np
import glob
import os

from PIL.Image import Image
out_path = "/home/luolu/PycharmProjects/video-processing/encoded_frame/"


path_image2 = "/home/luolu/PycharmProjects/video-processing/match_images/z217.png"
image2 = cv2.imread(path_image2)

for filename in sorted(glob.glob("/home/luolu/Desktop/MIT/*.png")):
    # print(filename)
    frame = cv2.imread(filename)
    base_name = os.path.basename(filename)
    if 0 <= int(base_name.split(".")[0]) <= 1580:
        print(base_name)
        frame = cv2.add(frame, image2)
        # save img
        # cv2.imwrite(filename, frame)
        cv2.imwrite(filename, frame)