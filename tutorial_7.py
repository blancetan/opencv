#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 25/2/2020 12:22
 @Author:   balanceTan 
 @File:     tutorial_7.py
 @Software: PyCharm
 
"""
'''
blur, medianBlur, filter2D

'''
import cv2 as cv
import numpy as np

def blur_demo(image):
    dst = cv.blur(image, (5, 5))
    return dst

def median_blur(image):
    dst = cv.medianBlur(image, 5)
    return dst
def custom_blur_demo(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]],np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    return dst

if __name__ == '__main__':
    src = cv.imread('./image/morph02.png')
    cv.namedWindow('logo', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('blur', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('median_blur', cv.WINDOW_AUTOSIZE)
    cv.namedWindow('custom_blur_demo', cv.WINDOW_AUTOSIZE)
    cv.imshow('logo', src)
    blur = blur_demo(src)
    cv.imshow('blur', blur)
    median_blur = median_blur(src)
    cv.imshow('median_blur', median_blur)
    custom_blur_demo = custom_blur_demo(src)
    cv.imshow('custom_blur_demo', custom_blur_demo)
    cv.waitKey(0)
    cv.destroyAllWindows()