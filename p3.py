# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Tap = QtWidgets.QTabWidget(self.centralwidget)
        self.Tap.setStyleSheet("round button")
        self.Tap.setObjectName("Tap")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.piano2 = QtWidgets.QPushButton(self.tab)
        self.piano2.setGeometry(QtCore.QRect(100, 20, 121, 501))
        self.piano2.setStyleSheet("QPushButton {\n"
"  background-color: white;\n"
"  color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 30px;\n"
"}")
        self.piano2.setText("")
        self.piano2.setObjectName("piano2")
        self.piano3 = QtWidgets.QPushButton(self.tab)
        self.piano3.setGeometry(QtCore.QRect(240, 40, 51, 291))
        self.piano3.setStyleSheet("QPushButton {\n"
"\n"
"  background-color: black;\n"
"  border-color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}")
        self.piano3.setText("")
        self.piano3.setObjectName("piano3")
        self.piano4 = QtWidgets.QPushButton(self.tab)
        self.piano4.setGeometry(QtCore.QRect(310, 20, 121, 501))
        self.piano4.setStyleSheet("QPushButton {\n"
"  background-color: white;\n"
"  color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 30px;\n"
"}")
        self.piano4.setText("")
        self.piano4.setObjectName("piano4")
        self.piano5 = QtWidgets.QPushButton(self.tab)
        self.piano5.setGeometry(QtCore.QRect(450, 40, 51, 291))
        self.piano5.setStyleSheet("QPushButton {\n"
"\n"
"  background-color: black;\n"
"  border-color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}")
        self.piano5.setText("")
        self.piano5.setObjectName("piano5")
        self.piano6 = QtWidgets.QPushButton(self.tab)
        self.piano6.setGeometry(QtCore.QRect(520, 20, 111, 501))
        self.piano6.setStyleSheet("QPushButton {\n"
"  background-color: white;\n"
"  color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 30px;\n"
"}")
        self.piano6.setText("")
        self.piano6.setObjectName("piano6")
        self.piano7 = QtWidgets.QPushButton(self.tab)
        self.piano7.setGeometry(QtCore.QRect(650, 40, 51, 291))
        self.piano7.setStyleSheet("QPushButton {\n"
"\n"
"  background-color: black;\n"
"  border-color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}")
        self.piano7.setText("")
        self.piano7.setObjectName("piano7")
        self.piano1 = QtWidgets.QPushButton(self.tab)
        self.piano1.setGeometry(QtCore.QRect(40, 40, 51, 291))
        self.piano1.setStyleSheet("QPushButton {\n"
"\n"
"  background-color: black;\n"
"  border-color: rgb(0, 0, 0);\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 10px;\n"
"}")
        self.piano1.setText("")
        self.piano1.setObjectName("piano1")
        self.Tap.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.p1 = QtWidgets.QPushButton(self.tab_2)
        self.p1.setGeometry(QtCore.QRect(20, 40, 50, 451))
        self.p1.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p1.setText("")
        self.p1.setObjectName("p1")
        self.p2 = QtWidgets.QPushButton(self.tab_2)
        self.p2.setGeometry(QtCore.QRect(70, 40, 50, 411))
        self.p2.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p2.setText("")
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(self.tab_2)
        self.p3.setGeometry(QtCore.QRect(120, 40, 50, 381))
        self.p3.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p3.setText("")
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QPushButton(self.tab_2)
        self.p4.setGeometry(QtCore.QRect(170, 40, 50, 351))
        self.p4.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(self.tab_2)
        self.p5.setGeometry(QtCore.QRect(220, 40, 50, 321))
        self.p5.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p5.setText("")
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QPushButton(self.tab_2)
        self.p6.setGeometry(QtCore.QRect(270, 40, 50, 281))
        self.p6.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p6.setText("")
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QPushButton(self.tab_2)
        self.p7.setGeometry(QtCore.QRect(320, 40, 50, 251))
        self.p7.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p7.setText("")
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QPushButton(self.tab_2)
        self.p8.setGeometry(QtCore.QRect(370, 40, 50, 231))
        self.p8.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p8.setText("")
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QPushButton(self.tab_2)
        self.p9.setGeometry(QtCore.QRect(420, 40, 50, 211))
        self.p9.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p9.setText("")
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QPushButton(self.tab_2)
        self.p10.setGeometry(QtCore.QRect(470, 40, 50, 191))
        self.p10.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p10.setText("")
        self.p10.setObjectName("p10")
        self.p11 = QtWidgets.QPushButton(self.tab_2)
        self.p11.setGeometry(QtCore.QRect(520, 40, 50, 171))
        self.p11.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p11.setText("")
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QPushButton(self.tab_2)
        self.p12.setGeometry(QtCore.QRect(570, 40, 50, 151))
        self.p12.setStyleSheet("QPushButton {\n"
"  background-color: gold;\n"
"  color: rgb(0, 0, 0);\n"
"\n"
"  border-width: 3px;        \n"
"  border-style: solid;\n"
"  border-radius: 20px;\n"
"}")
        self.p12.setText("")
        self.p12.setObjectName("p12")
        self.Tap.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.Tap, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tap.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tap.setTabText(self.Tap.indexOf(self.tab), _translate("MainWindow", "Piano"))
        self.Tap.setTabText(self.Tap.indexOf(self.tab_2), _translate("MainWindow", "Pan Flute"))
