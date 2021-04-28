# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 下午5:02
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : centre_crop.py
# @Software: PyCharm
import cv2


def center_crop(img, dim):
    """Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
    width, height = img.shape[1], img.shape[0]

    # process crop width and height for max available dimension
    crop_width = dim[0] if dim[0] < img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1] < img.shape[0] else img.shape[0]
    mid_x, mid_y = int(width / 2), int(height / 2)
    cw2, ch2 = int(crop_width / 2), int(crop_height / 2)
    crop_img = img[mid_y - ch2:mid_y + ch2, mid_x - cw2:mid_x + cw2]
    return crop_img


def scale_image(img, factor=1):
    """Returns resize image by scale factor.
	This helps to retain resolution ratio while resizing.
	Args:
	img: image to be scaled
	factor: scale factor to resize
	"""
    return cv2.resize(img, (int(img.shape[1] * factor), int(img.shape[0] * factor)))


if __name__ == "__main__":
    image = cv2.imread('/media/luolu/U盘大师U盘/test2/00140.png')

    ccrop_img = center_crop(image, (576, 576))
    # scale_img = scale_image(image, factor=1.5)

    cv2.imwrite("center_crop.jpg", ccrop_img)
    # cv2.imwrite("Kuvempu_scaled.jpg", scale_img)
