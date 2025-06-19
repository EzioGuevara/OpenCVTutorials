import numpy as np
import cv2 as cv
from Cython.Shadow import returns
#img1 = cv.imread('opencv-logo.png')
img = cv.imread('gold.bmp')
if img is  None:
    returns()
#访问图像中的元素
px = img[100,100]
print(px)
img[100,100] = [255,255,255]
print(img[100,100])
#访问red值
img.item(10,10,2)
#修改red值
img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.shape)#输出行列通道数
print(img.size)#输出总像素数
print(img.dtype)#输出数据类型

#ROI区域(复制ROI区域图像)
_2dcode  = img[300:400,800:900]
img[273:373,100:200] = _2dcode

#拆分合并通道
# b,g,r = cv.split(img)#较为耗时

# cv.waitKey(0)
# img = cv.merge((b,g,r))
#or
b = img[:,:,0]
#将红色通道全部设置为0
#g = img[:,:,2] = 0

cv.imshow('b',b)

#cv.imshow('g',g)
# cv.imshow('r',r)

#设置边框

replicate  = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
reflect_101 = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT_101)
warp = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT)

cv.imshow('MC',img)
cv.imshow('MC_replicate',replicate)
cv.imshow('MC_reflect',reflect)
cv.imshow('MC_reflect_101',reflect_101)
cv.imshow('MC_warp',warp)
cv.waitKey(0)
