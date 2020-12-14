import cv2 as cv
import matplotlib.pyplot as plt

def holding(img,type_):
    return cv.threshold(img,127,255,type_)[1]    
def main():
    img = cv.imread('datas/images/stockshot.png',cv.IMREAD_GRAYSCALE)
    titles = ['o','b','b_inv','tr','to','to_inv','mask','tri']
    type_ = [
                cv.THRESH_BINARY,
                cv.THRESH_BINARY_INV,
                cv.THRESH_TRUNC,
                cv.THRESH_TOZERO,
                cv.THRESH_TOZERO_INV,
                cv.THRESH_MASK,
                cv.THRESH_TRIANGLE
            ]
    # 
    imgs = [holding(img,f_type) for f_type in type_]
    imgs.insert(0,img)
    # 
    for i in range(len(imgs)):
        plt.subplot(2,4,i+1)
        plt.imshow(imgs[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()