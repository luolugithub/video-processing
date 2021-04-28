# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 下午7:00
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : batch_m_contrast_bright.py
# @Software: PyCharm
import cv2
import glob


def controller(img, brightness=255,
               contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
        al_pha = (max - shadow) / 255
        ga_mma = shadow

        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)
    else:
        cal = img
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)
        # putText renders the specified text string in the image.
    # cv2.putText(cal, 'B:{},C:{}'.format(brightness,
    #                                     contrast), (10, 30),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cal


file_path = "/home/luolu/Desktop/bcimg/"
brightness = 90
contrast = 77
if __name__ == '__main__':
    for file in sorted(glob.glob(file_path + "*.png")):
        # The function imread loads an image
        # from the specified file and returns it.
        original = cv2.imread(file)
        print(file)
        # Making another copy of an image.
        img = original.copy()

        effect = controller(img, brightness,
                            contrast)

        # The function imshow displays an image
        # in the specified window
        cv2.imwrite(file, effect)
