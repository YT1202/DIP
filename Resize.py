# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:43:48 2020

@author: YiTing
"""


import cv2


#讀取照片
img = cv2.imread('img_selfie.jpg')



# Bilinear interpolation
scaling_factors =  [0.1, 5.0, 30]
for i in scaling_factors:
    rows, cols, channels = img.shape
    img_Bilinear = cv2.resize(img, (int(cols*i), int(rows*i)), interpolation = cv2.INTER_LINEAR)
    cv2.imwrite('img_Bilinear_' + str(i) + '.jpg', img_Bilinear)
    

# Bicubic interpolation
for i in scaling_factors:
    rows, cols, channels = img.shape
    img_Bicubic = cv2.resize(img, (int(cols*i), int(rows*i)), interpolation = cv2.INTER_CUBIC)
    cv2.imwrite('img_Bicubic_' + str(i) + '.jpg', img_Bicubic)





