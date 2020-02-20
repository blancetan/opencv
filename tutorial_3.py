#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 20/2/2020 14:41
 @Author:   balanceTan 
 @File:     tutorial_3.py
 @Software: PyCharm
 
"""
import cv2 as cv
import numpy as np
import os
import random

IMAGE_BASE_DIR = 'image'

def access_pixels(image):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s channels : %s"%(width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow('image_demo', image)

def invert(image):
    dst = cv.bitwise_not(image)
    cv.imshow('invert_demo', dst)

def create_image():

    # m = np.ones([3, 3], dtype=np.uint8)
    # m.fill(1000)
    # print(m)

    # m1 = m.reshape([1,9])
    # print(m1)
    # m2 = np.array([[1, 2], [3, 4], [5, 6]], np.uint8)
    # m2.fill(20)
    # print(m2)
    # image = np.zeros([512, 512, 3])

    image = np.ones([512, 512, 3], np.uint8)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s channels : %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = random.randint(0, 255)
    cv.imshow('create_image', image)

if __name__ == '__main__':
    src = cv.imread(os.path.join(IMAGE_BASE_DIR, 'lena.png'))
    # cv.imshow('input_image', src)
    print(src.shape)
    start_t = cv.getTickCount()
    # access_pixels(src)
    # invert(src)
    create_image()
    end_t = cv.getTickCount()

    time = ((end_t - start_t) / cv.getTickFrequency())* 1000
    print('time is {}ms'.format(time))
    cv.waitKey(0)
    cv.destroyAllWindows()