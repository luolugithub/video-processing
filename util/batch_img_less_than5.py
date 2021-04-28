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
from distutils import errors

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

# less than 5 counter:  63345

# dst = "/home/luolu/Desktop/amazontest/test/"
src_dir = "/home/luolu/Desktop/spider_amazon/"
counter = 0
# for filename in os.listdir(directory):
# for filename in glob.iglob(src_dir + "/**/*.txt", recursive=True):

for filename in glob.iglob(src_dir + "/**/*.txt", recursive=True):
    print(filename)
    base_img_name = filename.split('.txt')[0].split('/')[-1]
    img_root_dir = filename.split('.txt')[0]
    imgs_count = len(os.listdir(img_root_dir))
    # print("filename:", filename)
    print("img_root_dir:", img_root_dir)
    # print("base_img_name:", base_img_name)
    print("imgs_count:", imgs_count)
    img0_name = img_root_dir + "/0.jpg"
    try:
        if imgs_count == 1:
            for count, filename in enumerate(os.listdir(img_root_dir)):
                dst = img_root_dir + "/" + str(count) + ".jpg"
                src = img_root_dir + "/" + filename
                # dst = 'xyz' + dst

                # rename() function will
                # rename all the files
                os.rename(src, dst)
            shutil.copy(img0_name, img_root_dir + "/1.jpg")
            shutil.copy(img0_name, img_root_dir + "/2.jpg")
            shutil.copy(img0_name, img_root_dir + "/3.jpg")
            shutil.copy(img0_name, img_root_dir + "/4.jpg")
            shutil.copy(img0_name, img_root_dir + "/5.jpg")
            counter += 1
        elif imgs_count == 2:
            for count, filename in enumerate(os.listdir(img_root_dir)):
                dst = img_root_dir + "/" + str(count) + ".jpg"
                src = img_root_dir + "/" + filename
                # dst = 'xyz' + dst

                # rename() function will
                # rename all the files
                os.rename(src, dst)
            img_name = img_root_dir + "/0.jpg"
            shutil.copy(img_root_dir + "/0.jpg", img_root_dir + "/3.jpg")
            shutil.copy(img_root_dir + "/1.jpg", img_root_dir + "/4.jpg")
            shutil.copy(img0_name, img_root_dir + "/5.jpg")
            counter += 1
        elif imgs_count == 3:
            for count, filename in enumerate(os.listdir(img_root_dir)):
                dst = img_root_dir + "/" + str(count) + ".jpg"
                src = img_root_dir + "/" + filename
                # dst = 'xyz' + dst

                # rename() function will
                # rename all the files
                os.rename(src, dst)
            shutil.copy(img_root_dir + "/0.jpg", img_root_dir + "/3.jpg")
            shutil.copy(img_root_dir + "/1.jpg", img_root_dir + "/4.jpg")
            shutil.copy(img_root_dir + "/2.jpg", img_root_dir + "/5.jpg")
            shutil.copy(img0_name, img_root_dir + "/6.jpg")
            counter += 1
        elif imgs_count == 4:
            for count, filename in enumerate(os.listdir(img_root_dir)):
                dst = img_root_dir + "/" + str(count) + ".jpg"
                src = img_root_dir + "/" + filename
                # dst = 'xyz' + dst

                # rename() function will
                # rename all the files
                os.rename(src, dst)
            shutil.copy(img_root_dir + "/0.jpg", img_root_dir + "/4.jpg")
            shutil.copy(img_root_dir + "/1.jpg", img_root_dir + "/5.jpg")
            shutil.copy(img_root_dir + "/2.jpg", img_root_dir + "/6.jpg")
            shutil.copy(img_root_dir + "/3.jpg", img_root_dir + "/7.jpg")
            shutil.copy(img0_name, img_root_dir + "/8.jpg")
            counter += 1
        elif imgs_count == 5:
            for count, filename in enumerate(os.listdir(img_root_dir)):
                dst = img_root_dir + "/" + str(count) + ".jpg"
                src = img_root_dir + "/" + filename
                # dst = 'xyz' + dst

                # rename() function will
                # rename all the files
                os.rename(src, dst)
            shutil.copy(img_root_dir + "/0.jpg", img_root_dir + "/5.jpg")
            shutil.copy(img_root_dir + "/1.jpg", img_root_dir + "/6.jpg")
            shutil.copy(img_root_dir + "/2.jpg", img_root_dir + "/7.jpg")
            shutil.copy(img_root_dir + "/3.jpg", img_root_dir + "/8.jpg")
            shutil.copy(img_root_dir + "/4.jpg", img_root_dir + "/9.jpg")
            counter += 1
        else:
            pass
        # copyfile(filename, dst + filename.split('.')[-1])
        # shutil.copy2('/src/file.ext', '/dst/dir')  # target filename is /dst/dir/file.ext
        # shutil.copy2(filename, dst)  # target filename is /dst/dir/file.ext
        counter += 1
    except OSError:
        continue

print("counter: ", counter)
