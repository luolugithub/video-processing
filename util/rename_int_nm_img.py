# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 上午10:51
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : rename_int_nm_img.py
# @Software: PyCharm
import glob
import os

path_img = "../out_frames/"
name_new = ""
path_new = "/home/luolu/Desktop/tmp/"
ext = ".png"
counter_file = 0
if __name__ == '__main__':
    for file in glob.glob(path_img + "*.png"):
        base_name = os.path.basename(file)
        # print(base_name)
        name = base_name.split(".")[0]
        print(name)
        if int(name) < 10:
            name_new = "0000" + name
        elif int(name) < 100:
            name_new = "000" + name
        elif int(name) < 1000:
            name_new = "00" + name
        else:
            name_new = name
        os.renames(file, path_new + name_new + ext)
        counter_file += 1
        print(file)
        print(path_new + name_new + ext)

    print("counter_file:", counter_file)