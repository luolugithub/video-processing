# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午12:45
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : change_hash.py
# @Software: PyCharm
import string
import random
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("filename", help="point to the file that needs hash changed", type=str)
# args = parser.parse_args()
N = 128  # Sets the length of the hash changer, larger means more iterations before same hash is generated
comment = "#"
hash_change = ''.join(random.choices(string.ascii_letters + string.digits,
                                     k=N))  # Generates a string of ascii letters and numbers the length of N
string_to_add = comment + hash_change  # Puts the comment character before the string
# string_to_add =
file_path = "/home/luolu/PycharmProjects/video-processing/out_frames/z1.mp4"
with open(file_path, 'a') as c:
    c.write(string_to_add)  # Adds the comment to the file you put into the program.
