from PyQt4 import QtGui, QtCore

import sys
import ui_main
import numpy as np
import pyqtgraph
import Paudio

class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption("background", 'w')
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.FFT.plotItem.showGrid(True, True, 0.7)
        self.PCM.plotItem.showGrid(True, True, 0.7)
        self.maxFFT = 0
        self.maxPCM = 0
        self.audio=Paudio.Paudio()
        self.audio.record_start()

    def update(self):
        if not self.audio.pcmData is None and not self.audio.fft is None:
            pcmMax = np.max(np.abs(self.audio.pcmData))
            if pcmMax > self.maxPCM:
                self.maxPCM=pcmMax
                self.PCM.plotItem.setRange(yRange=[-pcmMax, pcmMax])
            if np.max(self.audio.fft)>self.maxFFT:
                self.maxFFT=np.max(np.abs(self.audio.fft))
                self.FFT.plotItem.setRange(yRange=[0,1])
            pen=pyqtgraph.mkPen(color='b')
            self.PCM.plot(self.audio.datax, self.audio.pcmData, pen=pen, clear=True)
            pen=pyqtgraph.mkPen(color='r')
            self.FFT.plot(self.audio.fftx, self.audio.fft/self.maxFFT, pen=pen, clear=True)

        QtCore.QTimer.singleShot(1, self.update)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update()
    result = app.exec_()
    User = raw_input("Press Enter to Exit:")
    if User == '':
        form.audio.close()
        sys.exit()
                                           
