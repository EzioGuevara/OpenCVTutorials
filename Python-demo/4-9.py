#opencv轮廓
import cv2 as cv
import matplotlib.pyplot as plt

def find_bin_contours():
    img = cv.imread('data/silver.bmp')
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_gray = cv.blur(img_gray,(9,9))
    rlt,th1 = cv.threshold(img_gray,118,255,cv.THRESH_BINARY)
    contours,hierarchy = cv.findContours(th1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) #(源图像，廓检索模式，轮廓逼近方法)
    cv.drawContours(img,contours,-1,(0,255,0),3)
    # cv.drawContours(img,contours,)
    return img,th1

if __name__ == '__main__':
    img,th1 = find_bin_contours()
    cv.imshow('org_and_contours',img)
    cv.imshow('th1',th1)
    cv.waitKey()
