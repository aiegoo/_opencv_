import cv2 as cv

def nothing():
    pass
# 
def main():
    cv.namedWindow('canny edge')
    cv.createTrackbar('low','canny edge',0,1000,nothing)
    cv.createTrackbar('high','canny edge',0,1000,nothing)
    img_gray = cv.imread('datas/images/shapes.png',cv.IMREAD_GRAYSCALE)
    # img_gray = cv.imread('datas/images/shapes.png')
    while 1:
        low = cv.getTrackbarPos('low','canny edge')
        high = cv.getTrackbarPos('high','canny edge')
        img_canny = cv.Canny(img_gray,low,high)
        cv.imshow('canny edge',img_canny)
        if cv.waitKey(1)==ord('1'):
            break
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()