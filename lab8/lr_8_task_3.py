# -*- coding: utf-8 -*-
"""LR_8_task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bb1gDPtdqQFxFdlGou400bsIMF3ibWYs
"""

import cv2
from google.colab.patches import cv2_imshow
import numpy as np

img = cv2.imread("DIACHENKO.jpg")
print(img.shape)

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[46:119, 352:495]

# Вивід оригінального зображення
cv2_imshow(img)
print("\n")
# Вивід зміненого розміру зображення
cv2_imshow(imgResize)
print("\n")
# Вивід вирізаного зображення
cv2_imshow(imgCropped)
print("\n")
cv2.waitKey(0)