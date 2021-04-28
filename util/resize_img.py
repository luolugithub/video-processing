# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 上午10:10
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : resize_img.py
# @Software: PyCharm
import os

from PIL import Image

path = "/home/luolu/Desktop/MIT/"
dirs = os.listdir(path)


def resize():
    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            f, e = os.path.splitext(path + item)
            print(f)
            imResize = im.resize((1024, 600), Image.ANTIALIAS)
            imResize.save(f + '.png', 'PNG', quality=100)


resize()
# im = Image.open(path + item)
# f, e = os.path.splitext(path + item)
# print(f)
# imResize = im.resize((640, 368), Image.ANTIALIAS)
# imResize.save(f + '.jpg', 'JPEG', quality=100)