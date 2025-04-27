from filter import Filter
import cv2 
import numpy as np

class Laplacine(Filter):
    def run(self,image_path:str):
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

        blur1 = cv2.GaussianBlur(image, (0, 0), sigmaX=1)
        blur2 = cv2.GaussianBlur(image, (0, 0), sigmaX=2)
        
        dog = blur1 - blur2
        dog = cv2.normalize(dog, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        return dog