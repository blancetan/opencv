#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 19/2/2020 15:51
 @Author:   balanceTan 
 @File:     tutorial_1.py
 @Software: PyCharm
 
"""
import cv2 as cv
import numpy as np
import os

IMAGE_BASE_DIR = "image"

def video_demo():
    caputer = cv.VideoCapture(0)
    while True:
        ret, frame = caputer.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixelData = np.array(image)
    print(pixelData)


if __name__ == '__main__':
    print("====================opencv demo==================")
    src = cv.imread(os.path.join(IMAGE_BASE_DIR, 'example.PNG'))
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    get_image_info(src)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imwrite("demo_results/result.PNG", gray)
    while True:
        c = cv.waitKey(0)
        if c == 27:
            break
    cv.destroyAllWindows()
