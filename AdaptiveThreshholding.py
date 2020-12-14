import cv2 as cv
import matplotlib.pyplot as plt

def holding(img,type_):
    return cv.threshold(img,127,255,type_)[1]    
def holding_adp(img,type_,num):
    return cv.adaptiveThreshold(img,255,type_,cv.THRESH_BINARY,11,num)[1]        
def main():
    img = cv.imread('datas/images/sudoku.jpg',cv.IMREAD_GRAYSCALE)
    titles = ['o','b','b_inv','tr','to','to_inv','mask','tri']
    type_ = [
                cv.ADAPTIVE_THRESH_MEAN_C,
                cv.ADAPTIVE_THRESH_GAUSSIAN_C,
            ]
    # 
    num = 0
    imgs = [holding_adp(img,f_type,num+1) for f_type in type_]
    imgs.insert(0,holding(img,cv.THRESH_BINARY))
    # 
    for i in range(len(imgs)):
        plt.subplot(1,4,i+1)
        plt.imshow(imgs[i],'gray',vmin=0,vmax=255)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()