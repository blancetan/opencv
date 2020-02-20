#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 20/2/2020 9:09
 @Author:   balanceTan 
 @File:     tutorial_2.py
 @Software: PyCharm
 
"""
"""
1. VideoWrite()

"""
import math
import cv2 as cv
import sys

def main():
    cap = cv.VideoCapture(0)
    cv.namedWindow("video_record", cv.WINDOW_AUTOSIZE)
    fps = 25
    frameSize = (1080, 720)
    codec = cv.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv.VideoWriter('./demo_results/VideoRecord.avi', codec, fps, frameSize)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            start_t = cv.getTickCount()
            output.write(frame)
            cv.imshow("video_record", frame)
            stop_t = ((cv.getTickCount() - start_t) / cv.getTickFrequency()) * 1000
            key = cv.waitKey(max(2, 40 - int(math.ceil(stop_t)))) & 0xFF
            if key == ord('q'):
                print('exit recording!')
                break
    print("the display and recording video tasks take {}ms".format(stop_t))

    cap.release()
    output.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()


