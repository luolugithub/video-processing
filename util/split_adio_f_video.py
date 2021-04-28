# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 下午5:02
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : split_adio_f_video.py
# @Software: PyCharm

# This is the basic command extracting audio from a given video File:
#
# ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav

import subprocess

command = "ffmpeg -i /media/luolu/U盘大师U盘/20210325油管.mp4 -ab 192k -ac 2 -ar 44100 -vn /home/luolu/Desktop/dzn.wav"

subprocess.call(command, shell=True)