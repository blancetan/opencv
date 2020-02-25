#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 25/2/2020 16:47
 @Author:   balanceTan 
 @File:     tutorial_9.py
 @Software: PyCharm
 
"""
'''
numpy中的ravel()、flatten()、squeeze()都有将多维数组转换为一维数组的功能，区别：
ravel()：如果没有必要，不会产生源数据的副本
flatten()：返回源数据的副本
squeeze()：只能对维数为1的维度降维
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方图")

def image_hist(image):
    # color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        # print("i={0}:, color={1}".format(i, color))
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()
if __name__ == '__main__':
    src = cv.imread('./image/lena.png')
    cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
    cv.imshow('input image', src)
    # plot_demo(src)
    image_hist(src)
    cv.waitKey(0)
    cv.destroyAllWindows()



