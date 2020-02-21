#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 21/2/2020 8:42
 @Author:   balanceTan 
 @File:     tutorial_5.py
 @Software: PyCharm
 
"""
import cv2 as cv
import numpy as np

#  +, _, *, /  processing

def add_demo(m1, m2):
    dst = cv.add(img1, img2)
    cv.imshow('add_demo', dst)

def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow('subtract_demo', dst)

def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow('divide_demo', dst)

def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow('multiply_demo', dst)

# logic processing

def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1, m2)
    # dst = cv.bitwise_or(m1, m2)
    image = cv.imread('image/lena.png')
    cv.imshow('image', image)
    dst = cv.bitwise_not(image)
    cv.imshow('logic_demo', dst)

def contrast_brightness_demo(image, c, b):
    h, w, ch = image.shape
    blank = np.zeros((h, w, ch), image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow('co-br-demo', dst)

def others_demo(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]

    print(M1)
    print(M2)

    print(dev1)
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)

if __name__ == '__main__':
    print('=================hello OpenCv================')
    image1 = cv.imread('image/linuxlogo.jpg')
    image2 = cv.imread('image/windowlogo.jpg')
    cv.imshow('linuxlogo', image1)
    # cv.imshow('windowlogo', image2)
    # print(image1.shape)
    # print(image2.shape)
    # contrast_brightness_demo(image1, 0.7, 0)
    contrast_brightness_demo(image1, 0.9, 0)
    cv.waitKey(0)
    cv.destroyAllWindows()



