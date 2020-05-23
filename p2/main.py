import numpy as np
from PyQt5 import QtWidgets,QtGui,QtCore
from P2 import Ui_MainWindow
import sys
import pyqtgraph as pg

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       

        self.ui.Decode.clicked.connect(self.Browse)
        self.index=[]
       
    def Browse(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Images (*.png *.xpm *.jpg *.jpeg)", options=options)
        if fileName:
                self.file=fileName
                self.Decode()

    def drow(self,image,Q):
        frame = np.asarray(Image.open(image))
        image = pg.ImageItem(frame)
        image.rotate(270)
        Q.addItem(image)

    def Decode(self):
        byte_list = []
        with open(self.file,"rb") as f:

            while True:

                byte = f.read(1).hex()

                if not byte:

                    break

                byte_list.append(byte)

        for i in range(len(byte_list)-1):
            if("ffda"==str(byte_list[i])+str(byte_list[i+1])):
                self.index.append(i)
        print(self.index)
        for i in range(len(self.index)):
            imgData=open(self.file,'rb').read(self.index[i])
            with open("out"+str(i)+'.jpeg','wb') as file:
                file.write(imgData)
                file.write(b'\xff\xd9')
        self.drow("out"+str(1)+'.jpeg',self.ui.Q1)
        self.drow("out"+str(2)+'.jpeg',self.ui.Q2)
        self.drow("out"+str(3)+'.jpeg',self.ui.Q3)
        self.drow("out"+str(4)+'.jpeg',self.ui.Q4)
        self.drow("out"+str(5)+'.jpeg',self.ui.Q5)
        self.drow("out"+str(6)+'.jpeg',self.ui.Q6)
        self.drow("out"+str(7)+'.jpeg',self.ui.Q7)
        self.drow("out"+str(8)+'.jpeg',self.ui.Q8)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
