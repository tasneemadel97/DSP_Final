import os, sys
from p3 import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
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
       


    
    def PlayPiano(self, n):

        if( n==1):
            p = Note("C----", type='whole')
        elif( n==2):
            p = Note("D--", type='whole')
        elif( n==3):
            p = Note("F--", type='whole')
        elif( n==4):
            p= Note("G--", type='whole')
        elif( n==5):
            p = Note("A--", type='whole')
        elif( n==6):
            p = Note("B#4", type='whole')
        elif( n==7):
            p= Note("B#6", type='whole')

        PianoPart= stream.Part()
        PianoPart.insert(0, instrument.Piano())

        pianoMeasure = stream.Measure()
        pianoMeasure.append(p)
        PianoPart.append(pianoMeasure)

        sp = midi.realtime.StreamPlayer(PianoPart)
        sp.play()


    def PlayFlute(self,m):
        if m==1:
            f = Note("A----", type='whole')
        elif m==2:
            f =Note("A---",type='whole')
        elif m==3:
            f=Note("A--",type='whole')
        elif m==4:
            f=Note("A-`",type='whole')
        elif m==5:
            f=Note("A-",type='whole')
        elif m==6:
            f=Note("A`",type='whole')
        elif m==7:
            f=Note("A~",type='whole')
        elif m==8:
            f=Note("B",type='whole')
        elif m==9:
            f=Note("B##",type='whole')
        elif m==10:
            f=Note("B####",type='whole')
        elif m==11:
            f=Note("B#5",type='whole')
        elif m==12:
            f=Note("B#6",type='whole')
      


        FlutePart = stream.Part()
        FlutePart.insert(0, instrument.PanFlute())

        fluteMeasure = stream.Measure()
        fluteMeasure.append(f)
        FlutePart.append(fluteMeasure)

        sp = midi.realtime.StreamPlayer(FlutePart)
        sp.play()



  

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == '__main__':
    main()
   
