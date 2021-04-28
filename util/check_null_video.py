# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 上午9:10
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : get_all_frames.py
# @Software: PyCharm
import glob

import cv2
import time
import os
import numpy as np


# from PIL import Image, ImageDraw, ImageFilter

# from util.noise import sp_noise


def video_to_frames(path_video):

    # Start capturing the feed
    cap = cv2.VideoCapture(path_video, 0)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)

    return video_length


if __name__ == "__main__":
    counter = 0
    directory = "/home/luolu/Desktop/200b_amazon"
    # path_video = '/home/luolu/Desktop/200b_amazon/Part000/B01DYO48FG.mp4'
    for filename in glob.iglob(directory + "/**/*.mp4", recursive=True):
        v_len = video_to_frames(filename)
        if v_len == 0:
            counter += 1
            # delete file forever
            os.system("rm -rf " + filename)
    print("heiping v :", counter)
