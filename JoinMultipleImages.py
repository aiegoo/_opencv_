import cv2 as cv
import os
import numpy as np

def main():
    img = cv.imread('datas/images/lena.png')
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    grayToBGR = cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)

    imgHorr = np.hstack((grayToBGR,img,grayToBGR))
    imgHor = np.hstack((img,grayToBGR,img))
    cv.imshow('H',imgHor)
    imgVer = np.vstack((grayToBGR,img))
    imgVer = np.vstack((imgHor,imgHorr))
    cv.imshow('V',imgVer)
    cv.waitKey(0)

def setCap(videoCap,frame_h = 480,frame_w = 640):
    videoCap.set(4,frame_h)
    videoCap.set(3,frame_w)

def playsix():
    img = cv.imread('datas/images/lena.png')
    img = cv.resize(img,(640,480))
    # 
    cap = cv.VideoCapture(0)
    d_cap = cv.VideoCapture(2)
    mp_cap = cv.VideoCapture('datas/videos/Armbot.mp4')
    setCap(cap)
    setCap(d_cap)
    setCap(mp_cap)
    # 
    while 1:
        _,c_img = cap.read()
        _,d_img = d_cap.read()
        success,mp_img = mp_cap.read()
        if not success:
            mp_cap = cv.VideoCapture('datas/videos/Armbot.mp4')
            success,mp_img = mp_cap.read()
        # _,dd_img = dd_cap.read()
        mp_img = cv.resize(mp_img,(640,480))
        d_img = cv.resize(d_img,(640,480))
        d1_img = cv.resize(d_img[0:d_img.shape[0],0:int(d_img.shape[1]/2-1)],(640,480))
        d2_img = cv.resize(d_img[0:d_img.shape[0],int(d_img.shape[1]/2):int(d_img.shape[1]-1)],(640,480))
        # dd_img = cv.resize(dd_img,(640,480))
        imgH = np.hstack((c_img,mp_img,img))
        imgHH = np.hstack((d1_img,d2_img,img))
        imgV = np.vstack((imgH,imgHH))
        cv.imshow('V',imgV)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    mp_cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
    playsix()