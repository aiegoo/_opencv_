import pytesseract
from pytesseract import Output
import cv2 as cv

def main():
    img = cv.imread('datas/images/stockshot.png',cv.IMREAD_GRAYSCALE)
    # img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    img = holding(img)
    c_config = r'--oem 3 --psm 6 -l eng'
    w_string = pytesseract.image_to_string(img)
    words = pytesseract.image_to_data(img,config=c_config,output_type=Output.DICT)

    n_boxes = len(words['text'])
    for i in range(n_boxes):
        if int(words['conf'][i])>30:
            x,y,w,h = (words['left'][i],words['top'][i],words['width'][i],words['height'][i])
            img = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('#',img)
    cv.waitKey(0)
    print()

def holding(img):
    return cv.threshold(img,127,255,8)[1]

if __name__ == "__main__":
    main()
