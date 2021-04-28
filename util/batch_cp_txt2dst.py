# -*- coding: utf-8 -*-
"""
@Time ： 2021-04-17 10:33
@Auth ： LuoLu
@Email : argluolu@gmail.com
@File ：batch_img_aud_txt2video.py
@IDE ：PyCharm
@Motto：simple is everything
"""
import math
import os
from gtts import gTTS
import glob
import cv2
import moviepy.editor as mpe
import time
import operator

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from shutil import copyfile
import shutil

# counter:  56557
# mp3: 53509


dst = "/home/luolu/Desktop/txt_spider_amazon/"
src_dir = "/home/luolu/Desktop/spider_amazon"
pathVideoOut = "/home/luolu/Desktop/video_sp_amazon"
counter = 0
# for filename in os.listdir(directory):
for filename in glob.iglob(src_dir + "/**/*.txt", recursive=True):
    print(filename)
    # copyfile(filename, dst + filename.split('.')[-1])
    # shutil.copy2('/src/file.ext', '/dst/dir')  # target filename is /dst/dir/file.ext
    shutil.copy2(filename, dst)  # target filename is /dst/dir/file.ext
    counter +=1
print("counter: ", counter)
