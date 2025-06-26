import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
img = cv.imread('data/messi5.jpg', 0)
rows,cols = img.shape

#旋转图像
m = cv.getRotationMatrix2D(((rows-1)/2,(cols -1)/2),90,1)
dst_rotate = cv.warpAffine(img,m,(rows,cols))

#移动图像
m = np.float32([[1,0,100],[0,1,50]])
dst_move = cv.warpAffine(img,m,(cols,rows))#输入图像，变换矩阵，输出图像的大小（width , height）

#放大图像
res = cv.resize(img,None,fx=2,fy=2,interpolation = cv.INTER_CUBIC)
#or
height,width = img.shape[:2]
res = cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)

#透视变换1
img1 = cv.imread('data/chessboard.png')
rows,cols,sh = img1.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
m = cv.getAffineTransform(pts1,pts2)
dst_aff1 = cv.warpAffine(img1,m,(cols,rows))
dst_aff1 = cv.resize(dst_aff1,None,fx = 0.5,fy = 0.5,interpolation= cv.INTER_CUBIC)

#透视变换2
img2 = cv.imread('data/sudoku.png')
rows,cols,sh = img2.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
m = cv.getPerspectiveTransform(pts1,pts2)
dst_aff2 = cv.warpPerspective(img2,m,(300,300))

plt.subplot(121),plt.imshow(img2),plt.title('Input')
plt.subplot(122),plt.imshow(dst_aff2),plt.title('Output')
plt.show()

cv.imshow('rotate',dst_rotate)
cv.imshow('move',dst_move)
cv.imshow('resize',res)
cv.imshow("toushi1",dst_aff1)
# cv.imshow('toushi2',dst_aff2)
cv.waitKey(0)
cv.destroyAllWindows()