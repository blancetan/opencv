#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
 @DateTime: 20/2/2020 16:28
 @Author:   balanceTan 
 @File:     tutorial_4.py
 @Software: PyCharm
 
"""
import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow('mask', mask)
        cv.imshow('video', frame)
        cv.imshow('dst', dst)
        c = cv.waitKey(40)
        if c == ord('q'):
            break


def color_space_demo(image):
    cv.imshow('input image', image)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow('Ycrcb', Ycrcb)


if __name__ == '__main__':
    src = cv.imread('./image/lena.png')
    cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
    cv.imshow('input image', src)
    # color_space_demo(src)
    '''
    used: split and merge
    b, g, r = cv.split(src)
    cv.imshow('blue', b)
    cv.imshow('green',g)
    cv.imshow('red', r)

    dst = cv.merge((r, g, b))
    cv.imshow('changed image', dst)
    
    dst = cv.merge((b, g, r))
    cv.imshow('unchanged image', dst)
    
    '''
    extrace_object_demo()
    cv.waitKey(0)
    cv.destroyAllWindows()
