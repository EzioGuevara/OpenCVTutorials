#图像阈值分割
import cv2 as cv
import numpy as np
from joblib.numpy_pickle_utils import xrange
from matplotlib import pyplot as plt

def Global_Threshold():
    img = cv.imread('data/gradient.png', 0)
    rlt, thresh1 = cv.threshold(img, 127, 250, cv.THRESH_BINARY)
    rlt, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    rlt, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
    rlt, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
    rlt, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

    img2 = cv.imread('data/sudoku.png', 0)
    thresh6 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
    thresh7 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)

    titles = ['org', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv', 'org2', 'adpt_mean', 'adpt_gauss']
    imgs = [img, thresh1, thresh2, thresh3, thresh4, thresh5, img2, thresh6, thresh7]
    for i in xrange(9):
        plt.subplot(3, 3, i + 1), plt.imshow(imgs[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
def Adapted_Threshold():
    img3 = cv.imread('data/pic2.png',0)
    ret1,th1 = cv.threshold(img3,127,255,cv.THRESH_BINARY)
    ret2,th2 = cv.threshold(img3,127,255,cv.THRESH_BINARY)
    ret3,th3 = cv.threshold(img3,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #高斯滤波后再采用OTSU
    blur = cv.GaussianBlur(img3,(5,5),0)
    ret3,thr3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    #绘制所有图像以及其直方图

    titles = ['org','histogram','global_th',
                'org','histogram','OTSU1',
                'gauss','histogram','OTSU2']
    imgs2 = [img3,0,th1,
             img3,0,th2,
             blur,0,th3]

    for i in xrange(3):
        plt.subplot(3,3,i*3+1),plt.imshow(imgs2[i*3],'gray')
        plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+2),plt.hist(imgs2[i*3].ravel(),256)
        plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
        plt.subplot(3,3,i*3+3),plt.imshow(imgs2[i*3+2],'gray')
        plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
    plt.show()

def manual_otsu1():
    #mg = cv.imread('noisy2.png', 0)
    img = cv.imread('data/sudoku.png',0)
    blur = cv.GaussianBlur(img, (5, 5), 0)
    # 寻找归一化直方图和对应的累积分布函数
    hist = cv.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel() / hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in xrange(1, 256):
        p1, p2 = np.hsplit(hist_norm, [i])  # 概率
        if Q[i] == 0:
            q1 = 1
        # q1, q2 = Q[i], Q[255] - Q[i]  # 对类求和
        q2 = Q[255] - Q[i]  # 对类求和
        if q2 == 0:
            q2 = 1

        b1, b2 = np.hsplit(bins, [i])  # 权重
        # 寻找均值和方差
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2
        # 计算最小化函数
        fn = v1 * q1 + v2 * q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    # 使用OpenCV函数找到otsu的阈值
    ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    print("{} {}".format(thresh, ret))

def manual_otsu():
    img = cv.imread('data/sudoku.png',0)
    blur = cv.GaussianBlur(img,(5,5),0)
    hist = cv.calcHist([blur], [0], None, [256], [0, 256])
    hist_norm = hist.ravel()/hist.max()
    Q = hist_norm.cumsum()
    bins = np.arange(256)
    fn_min = np.inf
    thresh = -1
    for i in xrange(1,256):
        p1,p2 = np.hsplit(hist_norm,[i])#概率
        q1,q2 = Q[i],Q[255]-Q[i]#同类求和
        b1,b2 = np.hsplit(bins,[i])#权重
        #寻找均值和方差
        m1,m2 = np.sum(p1*b1)/q1,np.sum(p2*b2)/q2
        v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
        #计算最小化函数
        fn = v1*q1 + v2*q2
        if fn < fn_min:
            fn_min = fn
            thresh = i
    ret,otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
    print("{}{}".format(thresh,ret))
if __name__ == "__main__":
   # Global_Threshold()
   # Adapted_Threshold()
   manual_otsu1()
   img = cv.imread('data/sudoku.png',0)
   rlt1,th1 = cv.threshold(img,0,97,cv.THRESH_BINARY)
   rlt2,th2 = cv.threshold(img,0,255,cv.THRESH_OTSU)
   cv.imshow('global',th2)
   cv.imshow('otsu',th2)
   cv.waitKey(0)
   cv.destroyAllWindows()