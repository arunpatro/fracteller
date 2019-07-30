import cv2
import numpy as np

padimg = lambda img: img #np.pad(img, ((2, 0), (0, 2), (0, 0)), 'constant', constant_values=255)

def frackteller(img):
    
    one = recursiveFunc(img, 5)
    two = np.rot90(one)
    three = np.rot90(two)
    four = np.rot90(three)
    
    final = np.hstack([np.vstack([two, three]), np.vstack([one, four])])
    return final
    
def recursiveFunc(img, n):
    if n == 1:
        topright = 255 * np.ones(img.shape).astype(np.uint8)
        topright_p = padimg(topright)
        img_p = padimg(img)
        final = np.hstack([np.vstack([topright_p, img_p]), np.vstack([topright_p, topright_p])])
        return final
    else:
        imghalf = cv2.resize(img, None, fx=0.5,fy=0.5)
        top = recursiveFunc(imghalf, n-1)
        right = recursiveFunc(imghalf, n-1)
        topright = 255 * np.ones(img.shape).astype(np.uint8)
                           
        top_p = padimg(top)
        right_p = padimg(right)
        topright_p = padimg(topright)
        img_p = padimg(img)
        
        # print(f'{top_p.shape, right_p.shape, topright_p.shape, img_p.shape}')
        final = np.hstack([np.vstack([top_p, img_p]), np.vstack([topright_p, right_p])])
        return final
        
if __name__ == __main__:
    img = cv2.imread('xxxxxxx.jpg')
    zz = frackteller(img)
    cv2.imwrite('out.png', zz)


        
        
