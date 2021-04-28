# -*- coding: utf-8 -*-
# @Time    : 2021/2/17 下午4:48
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : baoguang_img.py
# @Software: PyCharm

import skimage
from skimage import io
import glob
import os
# img = io.imread("/home/luolu/Desktop/out_jot/00002.png")
# skimage.io.imshow(img)
# skimage.io.show()

# img_histeq = skimage.exposure.equalize_adapthist (img,20)
# skimage.io.imshow(img_histeq)
# skimage.io.show()
#
# img_gamma = skimage.exposure.adjust_gamma(img, gamma=0.5, gain=1)
# skimage.io.imshow(img_gamma)
# skimage.io.show()
#
# img_sigmoid = skimage.exposure.adjust_sigmoid(img)
# skimage.io.imshow(img_sigmoid)
# skimage.io.show()
path_img = "/home/luolu/Desktop/MIT/"
extention_file = ".png"
if __name__ == '__main__':
    for file in sorted(glob.glob(path_img + "/*" + extention_file)):
        base_name = os.path.basename(file)
        print(base_name)
        # pre_base_name = base_name.split('.')[0]
        img = io.imread(file)
        img_gamma = skimage.exposure.adjust_gamma(img, gamma=0.5, gain=1)
        # skimage.io.imshow(img_gamma)
        io.imsave(file, img_gamma)