# -*- coding: utf-8 -*-
# @Time    : 2021/2/16 下午3:11
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : png2jpg.py
# @Software: PyCharm
import os
import glob
from PIL import Image

file_path = "/home/luolu/Desktop/MIT"

extention_file = ".png"
new_extention_file = ".jpg"

if __name__ == '__main__':
    for file in sorted(glob.glob(file_path + "/*" + extention_file)):
        base_name = os.path.basename(file)
        # print(base_name)
        pre_base_name = file.split('.')[0]
        print(pre_base_name)
        im = Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(pre_base_name + new_extention_file)
