# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 下午12:47
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : find_hash.py
# @Software: PyCharm


# Python rogram to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib


def hash_file(filename):
    """"This function returns the SHA-1 hash
   of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


message = hash_file("/home/luolu/PycharmProjects/video-processing/out_frames/z1.mp4")
# 8c4ae54360efad5204cf3fd58dd6e0b580114ee0
# d9dbd20135bb5716b0f99ae408ef7f46f15731e8
print(message)
