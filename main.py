from PyQt4 import QtGui, QtCore

import sys
import ui_main
import numpy as np
import pyqtgraph
import Paudio
from threading import Thread

styleData="""
QWidget {
    background-color: #DADADA;
    background-color: #575757;
}
QPushButton
{
    border: 1px solid #199909;
    border-radius: 6px;
    background-color: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 0.67, "stop: 0 #22c70d, stop: 1 #116a06);
}
QPushButton:pressed
{
    border: 1px solid #333333;
    background-color: #222222
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #444444, stop: 1 #222222);
}
"""
class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption("background", 'k')
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.FFT.plotItem.showGrid(True, True, 1)
        self.PCM.plotItem.showGrid(True, True, 1)
        self.maxFFT = 0
        self.maxPCM = 0
        #self.sendData.clicked.connect(self.sending)
        self.stopData.clicked.connect(self.stopping)
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

    def stopping(self):
        self.audio.close()

"""
    def sending(self):
        self.newthread = ClientThread(self.audio.pcmData, 1)
        self.newthread.start()


class ClientThread(Thread):
    def __init__(self, conn, flag):
        Thread.__init__(self)

        self.data = conn
        self.flag = flag

    def run(self):
        while self.flag == 1:
"""

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
                                           
