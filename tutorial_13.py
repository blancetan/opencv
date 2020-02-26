#!/usr/bin/env python3
#_*_ coding: utf-8 _*_

"""
 @DateTime: 26/2/2020 11:35
 @Author:   balanceTan 
 @File:     tutorial_13.py
 @Software: PyCharm
 
"""
'''
cv.matchTemplate()

'''
import cv2 as cv
import numpy as np

def  template_demo():
    tp = cv.imread('./image/ROI_image.jpg')
    target = cv.imread('./image/1.jpg')
    cv.imshow('tp', tp)
    cv.imshow('target', target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCOEFF_NORMED, cv.TM_CCORR_NORMED]
    # methods = [cv.TM_SQDIFF_NORMED,]
    font = cv.FONT_HERSHEY_SIMPLEX
    h, w = tp.shape[:2]
    print('h:', h)
    print('w:', w)
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tp, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            t1 = min_loc
        else:
            t1 = max_loc
        print(t1)

        br = (t1[0] + w, t1[1] + h)
        print(br)
        cv.rectangle(target, t1, br, (0, 0, 255), 2)
        cv.imshow(''.join(('match-', np.str(md))), target)
        cv.putText(target, 'height:{0}, width:{1}'.format(h, w), t1, font, 1.0, (0, 0, 255), 1)
        print(result)



if __name__ == '__main__':

    template_demo()

    cv.waitKey(0)
    cv.destroyAllWindows()