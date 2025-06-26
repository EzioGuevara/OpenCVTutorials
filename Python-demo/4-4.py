#图像滤波
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
def manual_filter1(img1):
    kernel = np.ones((5,5),np.float32)/25
    return cv.filter2D(img1,-1,kernel)

def manual_filter2(img1):
    return cv.GaussianBlur(img1,(5,5),0)
    #return cv.blur(img1,(5,5))

if __name__ == '__main__':
    img = cv.imread('data\opencv-logo-white.png')
    #均值滤波
    dst1 = manual_filter2(img)
    #高斯滤波
    dst2 = cv.GaussianBlur(img,(5,5),0)
    #中值滤波
    dst3 = cv.medianBlur(img,5)
    #双边滤波
    dst4 = cv.bilateralFilter(img,9,75,75)
    plt.subplot(221),plt.imshow(img),plt.title('original')
    plt.xticks([]),plt.yticks([])

    plt.subplot(222),plt.imshow(dst1),plt.title('filter_averaging')
    plt.xticks([]),plt.yticks([])

    plt.subplot(223),plt.imshow(dst2),plt.title('filter_gauss')
    plt.xticks([]),plt.yticks([])

    plt.subplot(224),plt.imshow(dst3),plt.title('filter_median')
    plt.xticks([]),plt.yticks([])

    plt.subplot(235),plt.imshow(dst4),plt.title('filter_bilateral')
    plt.xticks([]),plt.yticks([])

    plt.show()
