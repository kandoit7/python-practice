# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(943, 673)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet(_fromUtf8("backround-color: rgb(0, 0, 0);"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.FFT = PlotWidget(self.centralwidget)
        self.FFT.setGeometry(QtCore.QRect(8, 400, 921, 261))
        self.FFT.setStyleSheet(_fromUtf8("border: 0px"))
        self.FFT.setObjectName(_fromUtf8("FFT"))
        self.PCM = PlotWidget(self.centralwidget)
        self.PCM.setGeometry(QtCore.QRect(8, 51, 921, 291))
        self.PCM.setStyleSheet(_fromUtf8("border: 0px"))
        self.PCM.setObjectName(_fromUtf8("PCM"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 4, 271, 41))
        self.label.setStyleSheet(_fromUtf8("font: 63 16pt \"Segoe UI Semibold\";\n"
"border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(7, 350, 256, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 63 16pt \"Segoe UI Semibold\";\n"
"border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sendData = QtGui.QPushButton(self.centralwidget)
        self.sendData.setGeometry(QtCore.QRect(290, 4, 111, 41))
        self.sendData.setStyleSheet(_fromUtf8("border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
""))
        self.sendData.setObjectName(_fromUtf8("sendData"))
        self.stopData = QtGui.QPushButton(self.centralwidget)
        self.stopData.setGeometry(QtCore.QRect(407, 4, 111, 41))
        self.stopData.setStyleSheet(_fromUtf8("border: 2px solid #333333;\n"
"border-radius: 6px;\n"
"background-color: #222222;\n"
"background-color: QlinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #444444, stop: 1 #222222);\n"
"color: white;\n"
""))
        self.stopData.setObjectName(_fromUtf8("stopData"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.centralwidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "Raw Data (PCM):", None))
        self.label_2.setText(_translate("MainWindow", "Frequency Data (FFT):", None))
        self.sendData.setText(_translate("MainWindow", "Send", None))
        self.stopData.setText(_translate("MainWindow", "Stop", None))

from pyqtgraph import PlotWidget
