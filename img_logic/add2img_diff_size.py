# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 下午5:18
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : add2img_diff_size.py
# @Software: PyCharm

import cv2 as cv


def combine_two_color_images(image1, image2):
    foreground, background = image1.copy(), image2.copy()

    foreground_height = foreground.shape[0]
    foreground_width = foreground.shape[1]
    alpha = 0.9

    # do composite on the upper-left corner of background image.
    blended_portion = cv.addWeighted(foreground,
                                     alpha,
                                     background[:foreground_height, :foreground_width, :],
                                     1 - alpha,
                                     0,
                                     background)
    background[:foreground_height, :foreground_width, :] = blended_portion
    cv.imshow('composited image', background)

    cv.waitKey()


if __name__ == '__main__':
    image1 = cv.imread("/home/luolu/PycharmProjects/video-processing/out_frames/00030.jpg")
    image2 = cv.imread("/home/luolu/PycharmProjects/video-processing/match_images/doctor.png")
    combine_two_color_images(image1, image2)
