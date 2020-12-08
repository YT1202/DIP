# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 05:30:20 2020

@author: YiTing
"""



import cv2
import matplotlib.pyplot as plt

# 讀取照片
img = cv2.imread('img_selfie.jpg')


# 將圖片轉為灰階
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('img_gray.jpg', img_gray)


# 處理前的直方圖
hist = cv2.calcHist([img_gray],[0],None,[256],[0,255])


# Histogram Equalization
img_HE = cv2.equalizeHist(img_gray)


# 處理後的直方圖
hist_E = cv2.calcHist([img_HE],[0],None,[256],[0,255])


# plot 直方圖
plt.plot(hist, 'b',  label = 'Original')
plt.plot(hist_E, 'r', label = 'Histogram Equalization')
plt.legend(loc = 'upper left' , fontsize = 8, shadow = True)
plt.savefig('img_hist.png')
plt.show()


# 儲存照片
cv2.imwrite('img_HE.jpg', img_HE)
