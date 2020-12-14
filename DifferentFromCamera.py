import cv2 as cv
import numpy as np

def main():
    cap = cv.VideoCapture(0)
    scaling = 0.5
    preF = get_frame(cap,scaling)
    curF = get_frame(cap,scaling)
    nextF = get_frame(cap,scaling)
    while 1:
        cv.imshow('Object',frame_diff(preF,curF,nextF))
        preF = curF
        curF = nextF
        nextF = get_frame(cap,scaling)
        if cv.waitKey(1)==ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def get_frame(cap,scalar):
    _,frame = cap.read()
    frame = cv.resize(frame,None,fx=scalar,fy=scalar,interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(frame,cv.COLOR_RGB2GRAY)
    return gray

def frame_diff(preF,curF,nextF):
    dF1 = cv.absdiff(nextF,curF)    
    dF2 = cv.absdiff(curF,preF)    
    return_diff = cv.absdiff(dF1,dF2)
    th_hold = len(return_diff[np.where(return_diff>2)])
    if th_hold>500:
        print('th_hold>200 : ',th_hold)
    return return_diff

if __name__ == "__main__":
    main()

