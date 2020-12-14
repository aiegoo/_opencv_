import cv2 as cv
import numpy as np
import pytesseract
from pytesseract import Output

def main():
    img = cv.imread('datas/images/cards.jpg')
    cv.imshow('image',img)
    ww,hh = 250,350
    pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
    pts2 = np.float32([[0,0],[ww,0],[0,hh],[ww,hh]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(ww,hh))
    cv.imshow('output',imgOutput)
    cv.waitKey(0)
    cv.destroyAllWindows()
# 
def tryPerspective():
    img = cv.imread('datas/images/namecard_02.jpg',cv.IMREAD_GRAYSCALE)
    img = cv.resize(img,(640,800))
    # img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow('image',img)
    # cv.waitKey(0)
    ww,hh = 640,800
    pts1 = np.float32([[99,257],[375,205],[214,656],[565,539]])
    pts2 = np.float32([[0,0],[ww,0],[0,hh],[ww,hh]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(ww,hh))
    # _,img_thre = cv.threshold(imgOutput,127,255,cv.THRESH_BINARY_INV)
    cv.imshow('output',imgOutput)
    # cv.imshow('thre',img_thre)
    c_config = r'--oem 3 --psm 6 -l eng'
    words = pytesseract.image_to_data(imgOutput,config=c_config,output_type=Output.DICT)
    n_boxes = len(words['text'])
    for i in range(n_boxes):
        if int(words['conf'][i])>30:
            x,y,w,h = (words['left'][i],words['top'][i],words['width'][i],words['height'][i])
            img = cv.rectangle(imgOutput,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('##',imgOutput)            
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == "__main__":
    # main()
    tryPerspective()