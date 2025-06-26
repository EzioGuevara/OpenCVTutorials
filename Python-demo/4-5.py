#形态学运算
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def manual_morphological(img):
    kernel =  np.ones((5,5),np.uint8)
    rlt1 = cv.erode(img,kernel,iterations = 1)#腐蚀
    rlt2 = cv.dilate(img,kernel,iterations = 1)#膨胀
    rlt3 = cv.morphologyEx(img,cv.MORPH_OPEN,kernel)#开运算
    rlt4 = cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)#闭运算
    rlt5 = cv.morphologyEx(img,cv.MORPH_GRADIENT,kernel)#形态学梯度
    kernel =  np.ones((9,9),np.uint8)
    rlt6 = cv.morphologyEx(img,cv.MORPH_TOPHAT,kernel)#顶帽运算 输入图像和图像开运算之差
    rlt7 = cv.morphologyEx(img,cv.MORPH_BLACKHAT,kernel)#黑帽子运算 输入图像和闭运算之差
    return rlt1,rlt2,rlt3,rlt4,rlt5,rlt6,rlt7

if __name__ == '__main__':
    img = cv.imread('data/j.png',0)
    erosion,dilation,opening,closing,gardient,tophat,blackhat = manual_morphological(img)

    struct1 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    struct2 = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
    plt.subplot(331),plt.imshow(img),plt.title('org')
    plt.subplot(332),plt.imshow(erosion),plt.title('erosion')
    plt.subplot(333),plt.imshow(dilation),plt.title('dilation')
    plt.subplot(334),plt.imshow(opening),plt.title('opening')
    plt.subplot(335),plt.imshow(closing),plt.title('closing')
    plt.subplot(336),plt.imshow(gardient),plt.title('gardient')
    plt.subplot(337),plt.imshow(tophat),plt.title('tophat')
    plt.subplot(338),plt.imshow(blackhat),plt.title('blackhat')
    plt.xticks([]),plt.yticks([])
    print(struct1)
    print(struct2)
    plt.show()
    cv.waitKey()