import cv2 as cv
import numpy as np
def main():
    img = cv.imread('datas/images/lena.png')
    imgCanny = cv.Canny(img,150,200)
    cv.imshow('canny',imgCanny)
    kernel = np.ones((5,5),np.uint8)
    imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
    cv.imshow('dialation',imgDialation)
    imgEroded = cv.erode(imgDialation,kernel,iterations=1)
    cv.imshow('eroded',imgEroded)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()