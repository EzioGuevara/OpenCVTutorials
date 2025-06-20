# 尽量避免在Python中使用循环，尤其是双/三重循环等。它们本来就很慢。
# 由于Numpy和OpenCV已针对向量运算进行了优化，因此将算法/代码向量化到最大程度。
# 利用缓存一致性。
# 除非需要，否则切勿创建数组的副本。尝试改用视图。数组复制是一项昂贵的操作。

#性能计时
import cv2 as cv
img1 = cv.imread('data\messi5.jpg')
x=5
e1 = cv.getTickCount()
#测试1
# for i in range(5,49,2):
#     img1 = cv.medianBlur(img1,i)
#测试2
#y = x**3
y = x*x*x
e2 = cv.getTickCount()
t1 = (e2-e1)/cv.getTickFrequency()

print(t1)
print(y)
print(cv.useOptimized())
