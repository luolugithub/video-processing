# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 下午4:52
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : frames_counter.py
# @Software: PyCharm
import cv2

path_video = "/home/luolu/PycharmProjects/video-processing/data_video/jidoudou.mp4"

# vidcap = cv2.VideoCapture(path_video)
# success, image = vidcap.read()
# count = 0
# while success:
#     # cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
#     success, image = vidcap.read()
#     print('Read a new frame: ', success)
#     count += 1
#
# print("video frames:", count)

# Start capturing the feed
cap = cv2.VideoCapture(path_video)
# Find the number of frames
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print("Number of frames: ", video_length)