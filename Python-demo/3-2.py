import cv2 as cv
import numpy as np

#part 1
# x = np.unit8([250])
# x = np.uint8(250)
# y = np.unit8([10])
# y = np.uint8(10)
# print(cv.add(x,y))

#part 2

# img1 = cv.imread('Python-demo\data\Dove.bmp')
# img2 = cv.imread('Python-demo\data\Dove_2Dcode.bmp')
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)

#part 3
img1 = cv.imread('Python-demo\data\messi5.jpg')
img2 = cv.imread('Python-demo\data\opencv-logo-white.png')
#logo放在左上角
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
#创建logo掩膜以及其补集
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,mask = cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
#创建mask的补集
mask_inv = cv.bitwise_not(mask)
#roi的logo涂黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)#"mask = mask_inv"?
#仅从logo图像中提取出logo区域
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
#将logo放入ROI并修改图像
dst = cv.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

# cv.imshow('roi',roi)
# cv.imshow('img2_fg',img2_fg)
# cv.imshow('img1_bg',img1_bg)
cv.imshow('dst',img1)
cv.waitKey(0)
cv.destroyAllWindows()