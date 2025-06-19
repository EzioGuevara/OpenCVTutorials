import cv2 as cv
import numpy as np

# x = np.unit8([250])
# x = np.uint8(250)
# y = np.unit8([10])
# y = np.uint8(10)
# print(cv.add(x,y))

img1 = cv.imread('Python-demo\Dove.bmp')
img2 = cv.imread('Python-demo\Dove_2Dcode.bmp')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)




cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()