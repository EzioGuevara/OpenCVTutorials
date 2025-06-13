import numpy as np
import cv2 as cv 
from matplotlib import pyplot as plt
img = cv.imread('C:\\Users\ezioli01\\OneDrive - myidemia\Bureau\\0522\\IMG_1524.jpg')
plt.subplot(231)
plt.imshow(img,'gray'),plt.title('Sheet')
plt.show()