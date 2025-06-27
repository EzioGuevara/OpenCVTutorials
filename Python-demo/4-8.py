import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from joblib.numpy_pickle_utils import xrange

img = cv.imread('data/messi5.jpg',0)
def build_pyramid(img):
    lower_reso = cv.pyrDown(img)
    higher_reso2 = cv.pyrUp(lower_reso)
    return lower_reso,higher_reso2
def use_pyramid_fusion(A,B):
    #生成A的高斯金字塔
    G = A.copy()
    gpA = [G]
    for i in xrange(6):
        G = cv.pyrDown(G)
        gpA.append(G)
    #生成B的高斯金字塔
    G=B.copy()
    gpB = [G]
    for i in xrange(6):
        G = cv.pyrDown(G)
        gpB.append(G)
    #生成A的拉普拉斯金字塔
    lpA = [gpA[5]]
    for i in xrange(5,0,-1):
        GE = cv.pyrUp(gpB[i])
        L = cv.subtract(gpB[i-1],GE)
        lpA.append(L)
    #生成B的拉普拉斯金字塔
    lpB = [gpB[5]]
    for i in xrange(5,0,-1):
        GE = cv.pyrUp(gpB[i])
        L = cv.subtract(gpB[i-1],GE)
        lpB.append(L)

    #将每个级别中添加左右两半的图像
    LS = []
    for la,lb in zip(lpA,lpB):
        rows,cols,dpt = la.shape
        a1 = cols/2
        ls = np.hstack((la[:,0:int(cols/2)],lb[:,int(cols/2):]))
        LS.append(ls)
    #重建
    ls_ = LS[0]
    for i in xrange(1,6):
        ls_ = cv.pyrUp(ls_)
        ls_ = cv.add(ls_,LS[i])
    #图像与直接连接的每一半
    real = np.hstack((A[:,:int(cols/2)],B[:,int(cols/2):]))
    return ls_,real

def fusion2():
    A = cv.imread('data/apple.jpg')
    B = cv.imread('data/orange.jpg')
    # 生成A的高斯金字塔
    G = A.copy()
    gpA = [G]
    for i in xrange(6):
        G = cv.pyrDown(G)
        gpA.append(G)
    # 生成B的高斯金字塔
    G = B.copy()
    gpB = [G]
    for i in xrange(6):
        G = cv.pyrDown(G)
        gpB.append(G)
    # 生成A的拉普拉斯金字塔
    lpA = [gpA[5]]
    for i in xrange(5, 0, -1):
        GE = cv.pyrUp(gpA[i])
        L = cv.subtract(gpA[i - 1], GE)
        lpA.append(L)
    # 生成B的拉普拉斯金字塔
    lpB = [gpB[5]]
    for i in xrange(5, 0, -1):
        GE = cv.pyrUp(gpB[i])
        L = cv.subtract(gpB[i - 1], GE)
        lpB.append(L)
    # 现在在每个级别中添加左右两半图像
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
        LS.append(ls)
    # 现在重建
    ls_ = LS[0]
    for i in xrange(1, 6):
        ls_ = cv.pyrUp(ls_)
        ls_ = cv.add(ls_, LS[i])
    # 图像与直接连接的每一半
    real = np.hstack((A[:, :cols / 2], B[:, cols / 2:]))

if __name__ == '__main__':
    img = cv.imread('data/messi5.jpg')
    imgApple = cv.imread('data/apple.jpg')
    imgOrange = cv.imread('data/orange.jpg')

    #img1,img2 = build_pyramid(img)
    img1,img2 = use_pyramid_fusion(imgApple,imgOrange)
    plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('org')
    plt.subplot(222), plt.imshow(img1, cmap='gray'), plt.title('img2')
    plt.subplot(223), plt.imshow(img2, cmap='gray'), plt.title('img3')
    plt.show()