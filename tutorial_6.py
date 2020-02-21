#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 21/2/2020 14:59
 @Author:   balanceTan 
 @File:     tutorial_6.py
 @Software: PyCharm
 
"""
'''
introduce  ROI and  floodFill
'''
import cv2 as cv
import numpy as np

def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, : ] = 255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.imshow('mask', mask)
    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == '__main__':
    image = cv.imread('image/1.jpg')
    ROI_image = image[98:378, 190:274]
    image[20:300, 100:184] = ROI_image
    cv.namedWindow('person', cv.WINDOW_NORMAL)
    cv.namedWindow('new_image', cv.WINDOW_NORMAL)
    # cv.moveWindow('person', 200, 200)
    cv.imshow('person', ROI_image)
    cv.imshow('new_image', image)
    # cv.imwrite('image/ROI_image.jpg',ROI_image)

    cv.waitKey(0)
    cv.destroyAllWindows()