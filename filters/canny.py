from filter import Filter
import cv2 
import numpy as np
class canny(Filter):
    def run(self,image_path:str):
        image = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        t_lower = 50  
        t_upper = 150 
        edge = cv2.Canny(image, t_lower, t_upper)
        return edge