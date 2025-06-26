import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration.uft import laplacian

if __name__ == '__main__':
    #sobel laplacian scharr
    img = cv.imread('data/sudoku.png',0)
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize = 5)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize =5)
    absSobelX = np.absolute(sobelx)
    absSobelY = np.uint8(absSobelX)

    # sobelx = cv.normalize(sobelx,(0,255),cv.NORM_MINMAX)
    plt.subplot(221),plt.imshow(img,cmap = 'gray'),plt.title('org')
    plt.subplot(222),plt.imshow(laplacian,cmap = 'gray'),plt.title('laplacian')
    plt.subplot(223),plt.imshow(sobelx,cmap = 'gray'),plt.title('sobelx')
    plt.subplot(224),plt.imshow(absSobelX,cmap = 'gray'),plt.title('sobely')
    plt.xticks([]), plt.yticks([])
    plt.show()