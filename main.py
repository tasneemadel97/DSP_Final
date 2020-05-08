import os, sys
from p3 import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidget, QVBoxLayout, QTableWidgetItem
import cv2
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
from music import *
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
        self.ui.drum.clicked.connect(self.Play)
        

        self.setGeometry(100, 90, 1000, 800)

    
    def Play(self):

        n = Note("A2", type='whole')

        drumPart = stream.Part()
        drumPart.insert(0, instrument.BassDrum())

        drumMeasure = stream.Measure()
        drumMeasure.append(n)
        drumPart.append(drumMeasure)


        sp = midi.realtime.StreamPlayer(drumPart)
        sp.play()

   


  

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()
   
