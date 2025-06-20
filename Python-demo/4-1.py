import cv2 as cv
import numpy as np
#BGR <--> GRAY && BGR <--> HSV
cap = cv.VideoCapture()
#读取帧
_,frame = cap.read()
if not frame :
    frame = cv.imread('data\opencv-logo.png')

hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
#定义HSV中蓝色的范围
lower_blue = np.array([50,50,50])
upper_blue = np.array([130,255,255])
#设置HSV的阈值使得只取蓝色
mask = cv.inRange(hsv,lower_blue,upper_blue)
#将掩膜和图像逐像素相加
rlt = cv.bitwise_and(frame,frame,mask = mask)

cv.imshow('mask',mask)
cv.imshow('rlt',rlt)
cv.waitKey(0)
cv.destroyAllWindows()