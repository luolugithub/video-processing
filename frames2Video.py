# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 上午10:40
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : frames2Video.py
# @Software: PyCharm
import cv2
import numpy as np
import os
from os.path import isfile, join
# ffmpeg -framerate 1 -pattern_type glob -i '*.png' -c:v libx264 -r 1 -pix_fmt yuvj420p etyh001.mp4
# ffmpeg -framerate 1 -pattern_type glob -i '*.png' -c:v libx264 -r 30 -pix_fmt yuvj420p imgc1.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"
# ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -vcodec libx264 -y -an ynrtmp.mp4
# ffmpeg -i ert1_2p_v.mp4 -i c135.wav -c:v copy -c:a aac ert1_2p.mp4

pathIn = './encoded_frame/'
pathOut = 'result_imgs/test_t4.avi'
fps = 25
# frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
for i in range(len(files)):
    filename = pathIn + files[i]
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()