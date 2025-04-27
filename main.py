# I am Ounis Abdelmalek
# this is my first project in git hub and image processing, I tried to create miniproject about edge detection
# to run this mini project you have to install cv2, numpy, PySide6, os
# I hope to follow me:
# linkedin.com/in/abdelmalek-ounis-484097351
# 


from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import Qt
import sys
from ui import Ui_MainWindow
import cv2
import numpy as np
import os

class ImageProc(QMainWindow):
    def __init__(self):
        super().__init__()
        # to call gui from ui.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = None
        self.filtred_img = None
        # The path to folder wich containe classes filter
        self.path = "filters"


        self.ui.save.clicked.connect(self.download)
        # I can use click here because of create custome lable which i add click signal in it
        self.ui.image.click.connect(self.upload)
        self.ui.run.clicked.connect(self.run)

        self.ui.filters.clear()

        # to get names of filters avalible in folder filters
        list_filters = self.get_filers_list(self.path)

        self.ui.filters.addItems(list_filters)



    def run(self):
        """This methode to process the image"""

        filter_name = self.ui.filters.currentText()
        m = __import__(self.path+"."+str(filter_name),fromlist=filter_name)

        #to create an object based on it string name
        filter_class = getattr(m,filter_name)
        filter_class = filter_class()
        
        self.image = filter_class.run(self.imagePath)
            
        height, width = self.image.shape
        bytes_per_line = width
        # QImage we use to make us an abilty to display image matrix in Qlable throw Qpixma
        q_image = QImage(self.image, width, height, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(q_image)

        pixmap = pixmap.scaled(self.ui.image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.filtered_image.setPixmap(pixmap)


    def upload(self):
        
        image_path = QFileDialog.getOpenFileName(self,"open file","","*.jpg")
        self.imagePath = image_path[0]
        pixmap = QPixmap(self.imagePath)
        pixmap = pixmap.scaled(self.ui.image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.image.setPixmap(pixmap)

    def download(self):
        path = QFileDialog.getSaveFileName(self,"save file","","*.jpg")[0]
        cv2.imwrite(path,self.image)

    def get_filers_list(self,path):
        list = []
        for file in os.listdir(path):
            if file.endswith(".py"):
                list.append(file.split(".")[0])
        return list

app =QApplication(sys.argv)
widget = ImageProc()
widget.resize(1200, 800)
widget.showMaximized()
app.exec()
