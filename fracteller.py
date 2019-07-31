import cv2
import numpy as np

def padimg(img, x=4):
    i = img[x:-x,x:-x,:]
    i = np.pad(i, ((x, x), (x, x), (0, 0)), 'constant', constant_values=255)
    return i

def frackteller(img, n=5):
    one = recursiveFunc(img, n)
    two = np.rot90(one)
    three = np.rot90(two)
    four = np.rot90(three)
    
    final = np.hstack([np.vstack([two, three]), np.vstack([one, four])])
    return final
    
def recursiveFunc(img, n):
    if n == 1:
        topright = 255 * np.ones(img.shape).astype(np.uint8)
        img_p = padimg(img)
        final = np.hstack([np.vstack([topright, img_p]), np.vstack([topright, topright])])
        return final
    else:
        imghalf = cv2.resize(img, None, fx=0.5,fy=0.5)
        top = recursiveFunc(imghalf, n-1)
        right = recursiveFunc(imghalf, n-1)
        topright = 255 * np.ones(img.shape).astype(np.uint8)
                           
        top_p = padimg(top)
        right_p = padimg(right)
        img_p = padimg(img)
        
        final = np.hstack([np.vstack([top_p, img_p]), np.vstack([topright, right_p])])
        return final
        
if __name__ == __main__:
    img = cv2.imread('xxxxxxx.jpg')
    zz = frackteller(img)
    cv2.imwrite('out.png', zz)
