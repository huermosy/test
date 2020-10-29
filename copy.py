import cv2 as cv
import numpy as np


# 把图像从一个区域拷贝到另一个区域
img = cv.imread('MyPic.png')
my_roi = img[0:100, 0:100]
img[150:250, 150:250] = my_roi
cv.imshow('change', img)
cv.waitKey()