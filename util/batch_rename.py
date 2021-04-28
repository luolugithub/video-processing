# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 下午4:21
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_rename.py
# @Software: PyCharm
import os
import glob

file_path = "/home/luolu/Desktop/out_jot"
# dst path must be diff with src file path
# dst_path = "dst_path"
dst_path = "/home/luolu/Desktop/t3"
extention_file = ".jpg"

if __name__ == '__main__':
    for file in sorted(glob.glob(file_path + "/*" + extention_file)):
        base_name = os.path.basename(file)
        # print(base_name)
        pre_base_name = base_name.split('.')[0]
        # print(pre_base_name)
        # if int(pre_base_name) >= 194:
        #     new_pre_base_name = int(pre_base_name) + 25
        # else:
        #     new_pre_base_name = int(pre_base_name)
        new_pre_base_name = int(pre_base_name) + 241
        print(file)
        # print(new_pre_base_name)
        if new_pre_base_name < 10:
            new_name = dst_path + "/0000" + str(new_pre_base_name) + extention_file
            print(new_name)
            os.rename(file, new_name)
        elif new_pre_base_name < 100:
            new_name = dst_path + "/000" + str(new_pre_base_name) + extention_file
            print(new_name)
            os.rename(file, new_name)
        elif new_pre_base_name < 1000:
            new_name = dst_path + "/00" + str(new_pre_base_name) + extention_file
            print(new_name)
            os.rename(file, new_name)
        elif new_pre_base_name < 10000:
            new_name = dst_path + "/0" + str(new_pre_base_name) + extention_file
            print(new_name)
            os.rename(file, new_name)
        else:
            new_name = dst_path + "/" + str(new_pre_base_name) + extention_file
            print(new_name)
            os.rename(file, new_name)