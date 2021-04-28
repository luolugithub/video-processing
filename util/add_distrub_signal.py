# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 下午4:44
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : add_distrub_signal.py
# @Software: PyCharm
import acoustics as acoustics
import numpy as np
import cv2


def add_noise(signal, snr):
    """
    signal: np.ndarray
    snr: float

    returns -> np.ndarray
    """

    # Generate the noise as you did
    noise = acoustics.generator.white(signal.size).reshape(*signal.shape)
    # For the record I think np.random.random does exactly the same thing

    # work out the current SNR
    current_snr = np.mean(signal) / np.std(noise)

    # scale the noise by the snr ratios (smaller noise <=> larger snr)
    noise *= (current_snr / snr)

    # return the new signal with noise
    return signal + noise


img = cv2.imread('/home/luolu/PycharmProjects/video-processing/out_frames/00122.png')

# Speckle Noise
# gauss = np.random.normal(0, 1, img.size)
# gauss = gauss.reshape(img.shape[0], img.shape[1], img.shape[2]).astype('uint8')
# noise = img + img * gauss
noise = add_noise(img, 0.9)

cv2.imshow('img', noise)
cv2.waitKey(0)
cv2.destroyAllWindows()