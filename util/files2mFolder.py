# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 下午4:14
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : files2mFolder.py
# @Software: PyCharm
import os
import glob
import shutil

files_dir = "/home/luolu/Desktop/video_sp_amazon"
dst_path = "/home/luolu/Desktop/200b_amazon/"
start_count = 0
added = 200
counter = 0
import os
import shutil

# path of imgr Source
path = '/home/luolu/Desktop/video_sp_amazon'

# path of folder Target
folderPath = '/home/luolu/Desktop/200b_amazon'
# 46985/200 = 235
distributionNumber = 235
# new 61 folder numbers as sort_folder_number[61]
sort_folder_number = [x for x in range(0, distributionNumber)]

'''
Tips:
1: os.path.join(path1,path2...)
this function is used to combine the path,it returns a path which is 'path1/path2...'
2: os.makedirs(path)
this function is used to make a directory(new folder) in the path param
3: shutil.move(oldPath,newPath)
this function is used to move file from param1 to param 2
4: os.path.exists(path)
this function is used to check the filePath(param1) whether exists
'''

for number in sort_folder_number:
    new_folder_path = os.path.join(folderPath, 'Part%03d' % number)  # new_folder_path is ‘folderPath\number'

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        print("new a floder named " + str(number) + 'at the path of ' + new_folder_path)

# give the img list
file_list = os.listdir(path)
# print(file_list)
#
'''define the first foloderNumber'''
folderNumber = -1
print('there are ' + str(len(file_list)) + ' files at the source path of ' + path)
for i in range(0, len(file_list)):
    old_file_path = os.path.join(path, file_list[i])
    if os.path.isdir(old_file_path):
        '''if the path is a folder,program will pass it'''
        print('img does not exist ,path=' + old_file_path + ' it is a dir')
        pass
    elif not os.path.exists(old_file_path):
        '''if the path does not exist,program will pass it'''
        print('img does not exist ,path=' + old_file_path)
        pass
    else:
        '''define the number,it decides how many imgs each people process'''
        number = added  # int(len(file_list)/peopleNumber)
        if i % number == 0:
            folderNumber += 1
        new_file_path = os.path.join(folderPath, 'Part%03d' % folderNumber)
        if not os.path.exists(new_file_path):
            print('not exist path:' + new_file_path)
            break
        shutil.copy(old_file_path, new_file_path)
        print('success move file from ' + old_file_path + ' to ' + new_file_path)





