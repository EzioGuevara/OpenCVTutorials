import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('silver.bmp',0)

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])#hide X Y axis
plt.show()

img = cv.imread('Python-demo/IMG_3653.jpeg',3)
cv.imshow('image', img)

# k = cv.waitKey(0) & 0xFF #64位计算机
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('silver_copy.bmp',img)
#     cv.destroyAllWindows()
