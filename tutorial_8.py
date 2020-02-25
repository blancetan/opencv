#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 25/2/2020 14:55
 @Author:   balanceTan 
 @File:     tutorial_8.py
 @Software: PyCharm
 
"""
import cv2 as cv
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv

def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]         #blue
            g = image[row, col, 1]         #green
            r = image[row, col, 2]         #red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    return image

if __name__ == '__main__':
    src = cv.imread('./image/lena.png')
    cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('Gaussian Blur', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('Gaussian Noise', cv.WINDOW_AUTOSIZE)
    cv.imshow('input image', src)
    t_start = cv.getTickCount()
    gussian_nosie = gaussian_noise(src)
    t_stop = cv.getTickCount()
    time = (t_stop - t_start) / cv.getTickFrequency() *1000
    print('spend_time:', time)
    cv.imshow('Gaussian Noise', gussian_nosie)

    dst = cv.GaussianBlur(gussian_nosie, (0, 0), 2)
    cv.imshow('Gaussian Blur', dst)


    cv.waitKey(0)
    cv.destroyAllWindows()
