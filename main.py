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

        self.ui.piano1.clicked.connect(lambda: self.PlayPiano(1))
        self.ui.piano2.clicked.connect(lambda: self.PlayPiano(2))
        self.ui.piano3.clicked.connect(lambda: self.PlayPiano(3))
        self.ui.piano4.clicked.connect(lambda: self.PlayPiano(4))
        self.ui.piano5.clicked.connect(lambda: self.PlayPiano(5))
        self.ui.piano6.clicked.connect(lambda: self.PlayPiano(6))
        self.ui.piano7.clicked.connect(lambda: self.PlayPiano(7))
        
    

    
    def PlayPiano(self, n):

        if( n==1):

            n = Note("C----", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)


            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()

        if( n==2):

            n = Note("D--", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)


            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()

        if( n==3):

            n = Note("F--", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)

            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()
   
        if( n==4):

            n = Note("G--", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)

            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()


        if( n==5):

            n = Note("A--", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)

            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()

        if( n==6):

            n = Note("B#4", type='whole')

            PianoPart = stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)

            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()


        if( n==7):

            n = Note("B#6", type='whole')

            PianoPart= stream.Part()
            PianoPart.insert(0, instrument.Piano())

            pianoMeasure = stream.Measure()
            pianoMeasure.append(n)
            PianoPart.append(pianoMeasure)

            sp = midi.realtime.StreamPlayer(PianoPart)
            sp.play()


  

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()
   
