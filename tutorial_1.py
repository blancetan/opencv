#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 19/2/2020 15:51
 @Author:   balanceTan 
 @File:     tutorial_1.py
 @Software: PyCharm
 
"""
'''
一, image operate
1. imread()
2. imshow()
3. imwrite()
二，video  operate
1. VideoCapture()
2. imshow()
3. waitkey()
4. destroyAllWindows()

'''
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
        cv.imwrite("demo_results/demo.avi", frame)
        c = cv.waitKey(50)
        if c == 27:
            break
        caputer.release()
        cv.destroyAllWindows()

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixelData = np.array(image)
    print(pixelData)



if __name__ == '__main__':
    print("====================opencv image_demo==================")
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
