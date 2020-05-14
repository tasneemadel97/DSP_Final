import struct
import PIL.Image, PIL.ImageFile
import cv2, time
import numpy as np
import math
from matplotlib import pyplot as plt
from zigzag import *
from scipy.fftpack import dct, idct
from scipy import fftpack
from PIL import Image
import PIL.Image, PIL.ImageFile
from PyQt5 import QtWidgets,QtGui,QtCore
from P2 import Ui_MainWindow
import sys
import pyqtgraph as pg

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Q1.setBackground('w')
        self.ui.Q1.getPlotItem().hideAxis('left')
        self.ui.Q1.getPlotItem().hideAxis('bottom')

        self.ui.Q2.setBackground('w')
        self.ui.Q2.getPlotItem().hideAxis('left')
        self.ui.Q2.getPlotItem().hideAxis('bottom')
        self.ui.Q3.setBackground('w')
        self.ui.Q3.getPlotItem().hideAxis('left')
        self.ui.Q3.getPlotItem().hideAxis('bottom')
        self.ui.Q4.setBackground('w')
        self.ui.Q4.getPlotItem().hideAxis('left')
        self.ui.Q4.getPlotItem().hideAxis('bottom')
        self.ui.Q5.setBackground('w')
        self.ui.Q5.getPlotItem().hideAxis('left')
        self.ui.Q5.getPlotItem().hideAxis('bottom')
        self.ui.Q6.setBackground('w')
        self.ui.Q6.getPlotItem().hideAxis('left')
        self.ui.Q6.getPlotItem().hideAxis('bottom')
        self.ui.Q7.setBackground('w')
        self.ui.Q7.getPlotItem().hideAxis('left')
        self.ui.Q7.getPlotItem().hideAxis('bottom')
        self.ui.Q8.setBackground('w')
        self.ui.Q8.getPlotItem().hideAxis('left')
        self.ui.Q8.getPlotItem().hideAxis('bottom')

        self.ui.Decode.clicked.connect(self.Browse)
        self.block_size=4


    
    def Browse(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Images (*.png *.xpm *.jpg)", options=options)
        if fileName:
                self.file=fileName
              
                     
                self.drow(self.Decode(10),self.ui.Q1)
                self.drow(self.Decode(20) ,self.ui.Q2)
                self.drow(self.Decode(30),self.ui.Q3)
                self.drow(self.Decode(50),self.ui.Q4)
                self.drow(self.Decode(60),self.ui.Q5)
                self.drow(self.Decode(70),self.ui.Q6)
                self.drow(self.Decode(100),self.ui.Q7)
                self.drow(self.Decode(200),self.ui.Q8)




    def drow(self,arr,Q):
        image = pg.ImageItem(arr)
        image.rotate(270)
        Q.addItem(image)

    def Decode(self,quality):
            img = PIL.Image.open(self.file)
            destination = "new_image.jpeg"
            im=img.save(destination, "JPEG", quality=quality, progressive=True)
            file = cv2.imread("new_image.jpeg",0)

            padded_img = file
            h  = len(file) 
            w = len(file[0]) 

            nbh = math.ceil(h/self.block_size)
            nbh = np.int32(nbh)

            nbw = math.ceil(w/self.block_size)
            nbw = np.int32(nbw)
    
            H =  self.block_size * nbh
            W =  self.block_size * nbw

            padded_img = np.zeros((H,W))

            for i in range(h):
                for j in range(w):
                        pixel = file[i,j]
                        padded_img[i,j] = pixel 
            # plt.imshow(padded_img,cmap='gray')
            # plt.show()

            for i in range(nbh):
                    row_ind_1 = i*int(self.block_size)
                    row_ind_2 = row_ind_1+int(self.block_size)
                    for j in range(nbw):

                        col_ind_1 = j*int(self.block_size)

                        col_ind_2 = col_ind_1+int(self.block_size)

                        block = padded_img[ row_ind_1 : row_ind_2 , col_ind_1: col_ind_2 ]
                
                        reshaped= np.reshape(block,(int(self.block_size)*int(self.block_size)))
                    
                        reordered = inverse_zigzag(reshaped, int(self.block_size), int(self.block_size))
                        IDCT=idct(reordered)
                        padded_img[ row_ind_1 : row_ind_2 , col_ind_1 : col_ind_2 ] = IDCT

            padded_img = np.uint8(padded_img)
            # decoded_img = padded_img[0:int(h),0:int(w)]
            # plt.imshow(padded_img,cmap='gray')
            # plt.show()
            return padded_img
           
     
            


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
