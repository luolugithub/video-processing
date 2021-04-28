# -*- coding: utf-8 -*-
# @Time : 2020/3/5 上午9:46
# @Author : LuoLu
# @FileName: single_color_replace.py
# @Software: PyCharm
# @Github ：https://github.com/luolugithub
# @E-mail ：argluolu@gmail.com
import glob
import os

import cv2 as cv
import numpy as np
from PIL import Image
import numpy as np

# fen R: 254 G: 195 B: 180 | 255, 192, 192
# light Blue 0, 255, 255
# caolv R: 0 G: 136 B: 126 | 0, 128, 128
# caolv = (0, 128, 128)
# lb = (0, 255, 255)
# fen = (255, 192, 192)


dst_path = "/home/luolu/Desktop/cm_frames/"

if __name__ == '__main__':
    for filename in glob.glob('/home/luolu/Desktop/90frames/*.png'):
        img = cv.imread(filename)
        # print(filename)
        base_name = os.path.basename(filename)
        print(base_name)
        # Make all perfectly green pixels white
        img[np.all(img == (254, 254, 248), axis=-1)] = (163, 163, 158)
        img[np.all(img == (195, 151, 112), axis=-1)] = (189, 174, 160)
        img[np.all(img == (251, 246, 192), axis=-1)] = (213, 156, 118)
        img[np.all(img == (255, 242, 214), axis=-1)] = (168, 160, 141)
        img[np.all(img == (26, 23, 16), axis=-1)] = (0, 0, 0)
        img[np.all(img == (28, 28, 28), axis=-1)] = (0, 5, 5)
        img[np.all(img == (29, 29, 29), axis=-1)] = (0, 0, 10)
        img[np.all(img == (31, 27, 224), axis=-1)] = (0, 0, 0)
        # add x y line of center
        # img[286:288:, :] = [240, 240, 240]
        # img[:, 382:384] = [255, 255, 255]
        #
        # img[np.all(img, axis=-1).] = [0, 0, 0]
        # img[np.all(img, axis=-1).diagonal(2)] = [190, 190, 190]


        # im2.save("/home/luolu/PycharmProjects/color_detection/data/result_qaak/caolv_mask/" + base_name)
        cv.imwrite(dst_path + base_name, img)
