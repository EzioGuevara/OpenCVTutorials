import numpy as np
import cv2 as cv
img = cv.imread('OpenCV/OpenCVTutorials/Python-demo/IMG_3653.jpeg',3)
cv.imshow('image', img)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('IMG_3653_gray.png', img)
    cv.destroyAllWindows()
elif k == ord('c'): # wait for 'c' key to close the window
    cv.destroyAllWindows()
elif k == ord('r'): # wait for 'r' key to reload the image
    img = cv.imread('IMG_3653.jpeg', 0)
    cv.imshow('image', img)
    cv.waitKey(0)
else:
    print("Key not recognized. Press ESC to exit, 's' to save, 'c' to close, or 'r' to reload the image.")
    cv.destroyAllWindows()
cv.destroyAllWindows()
# Note: Ensure that 'IMG_3653.jpeg' exists in the same directory as this script.
#test