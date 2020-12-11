import cv2 as cv
import os
import pytesseract 
from pytesseract import Output

img = cv.imread('/home/tony/Downloads/receipt1.jpeg')

custom_config = r'--oem 3 --psm 6 -l kor+kor_vert+eng'
words_string = pytesseract.image_to_string(img)
words = pytesseract.image_to_data(img, config=custom_config,
output_type=Output.DICT)

print(words.keys())
n_boxes = len(words['text'])
for i in range(n_boxes):
    if int(words['conf'][i]) > 60:
        (x, y, w, h) = (words['left'][i], words['top'][i], words['width'][i], words['height'][i])
        img = cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 1)

cv.imshow('Resource', img)