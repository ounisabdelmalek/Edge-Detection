from filter import Filter
import cv2 
import numpy as np
class soble(Filter):
    def run(self,image_path:str):
        ksize=5
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        gradient_x = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=ksize)
        gradient_y = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=ksize)
        image_sob= np.sqrt(gradient_x**2 + gradient_y**2)
        norm = cv2.normalize(image_sob, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        return norm