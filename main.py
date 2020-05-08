import os, sys
from p3 import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QVBoxLayout, QTableWidgetItem
# import cv2
import pylab
import wave
import pylab
import matplotlib.pyplot as pylab
import scipy
from scipy import signal
from scipy.io import wavfile
import numpy as np
from glob import glob
from numpy import asarray
# from music import *
import music21
from music21 import note, stream, pitch, duration, instrument, tempo, chord
from music21.note import Note, Rest
from music21.chord import Chord
from music21 import midi




class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Play)
        # self.p=[self.ui.p1,self.ui.p2,self.ui.p3,self.ui.p4,self.ui.p5,self.ui.p6,self.ui.p7,self.ui.p8,self.ui.p9,self.ui.p10,self.ui.p11,self.ui.p12,self.ui.p13,self.ui.p14,self.ui.p15]
        # for i in range(len(self.p)):
        self.ui.p1.clicked.connect(lambda: self.PlayFlute(1))
        self.ui.p2.clicked.connect(lambda: self.PlayFlute(2))
        self.ui.p3.clicked.connect(lambda: self.PlayFlute(3))
        self.ui.p4.clicked.connect(lambda: self.PlayFlute(4))
        self.ui.p5.clicked.connect(lambda: self.PlayFlute(5))
        self.ui.p6.clicked.connect(lambda: self.PlayFlute(6))
        self.ui.p7.clicked.connect(lambda: self.PlayFlute(7))
        self.ui.p8.clicked.connect(lambda: self.PlayFlute(8))
        self.ui.p9.clicked.connect(lambda: self.PlayFlute(9))
        self.ui.p10.clicked.connect(lambda: self.PlayFlute(10))
        self.ui.p11.clicked.connect(lambda: self.PlayFlute(11))
        self.ui.p12.clicked.connect(lambda: self.PlayFlute(12))
       


        

        # self.setGeometry(100, 90, 1000, 800)

    
    def Play(self):

        n = Note("A2", type='whole')

        drumPart = stream.Part()
        drumPart.insert(0, instrument.BassDrum())

        drumMeasure = stream.Measure()
        drumMeasure.append(n)
        drumPart.append(drumMeasure)


        sp = midi.realtime.StreamPlayer(drumPart)
        sp.play()
    def PlayFlute(self,m):
        if m==1:
            self.n = Note("A----", type='whole')
        elif m==2:
            self.n=Note("A---",type='whole')
        elif m==3:
            self.n=Note("A--",type='whole')
        elif m==4:
            self.n=Note("A-`",type='whole')
        elif m==5:
            self.n=Note("A-",type='whole')
        elif m==6:
            self.n=Note("A`",type='whole')
        elif m==7:
            self.n=Note("A~",type='whole')
        elif m==8:
            self.n=Note("B#",type='whole')
        elif m==9:
            self.n=Note("B#~",type='whole')
        elif m==10:
            self.n=Note("B##",type='whole')
        elif m==11:
            self.n=Note("B###",type='whole')
        elif m==12:
            self.n=Note("B####",type='whole')
      


        FlutePart = stream.Part()
        FlutePart.insert(0, instrument.PanFlute())

        drumMeasure = stream.Measure()
        drumMeasure.append(self.n)
        FlutePart.append(drumMeasure)


        sp = midi.realtime.StreamPlayer(FlutePart)
        sp.play()

   


  

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()
   
