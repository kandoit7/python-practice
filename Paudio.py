import pyaudio
import threading
import numpy as np
import time

def getFFT(pcmData, rate):
        pcmData = pcmData*np.hamming(len(pcmData))
        fft=np.fft.fft(pcmData)
        fft=np.abs(fft)
        freq=np.fft.fftfreq(len(fft), 1.0/rate)
        return freq[:int(len(freq)/2)],fft[:int(len(fft)/2)]

class Paudio():
        def __init__(self, updatesPerSecond=10):
                self.p = pyaudio.PyAudio()
                self.RATE = 48000
                self.CHUNK = 2048
                self.FORMAT = pyaudio.paInt16
                self.CHANNELS = 1
                self.datax = np.arange(self.CHUNK)/float(self.RATE)
                self.chunksRead=0

        def receiveData(self):
                try:
                        self.pcmData = np.fromstring(self.stream.read(self.CHUNK), dtype=np.int16)
                        self.fftx, self.fft = getFFT(self.pcmData, self.RATE)
                except Exception as E:
                        print(E, "\n")
                        self.KeepRecording = False
                if self.KeepRecording:
                        self.thread_start()
                else:
                        self.stream.close()
                        self.p.terminate()
                self.chunksRead+=1

        def close(self):
                self.stream.stop_stream()
                self.p.terminate()

        def thread_start(self):
                self.th = threading.Thread(target=self.receiveData)
                self.th.start()

        def record_start(self):
                self.KeepRecording = True
                self.pcmData = None
                self.fft=None
                self.stream = self.p.open(format=self.FORMAT,
                                          channels=self.CHANNELS,
                                          rate=self.RATE,
                                          input=True,
                                          frames_per_buffer=self.CHUNK
                                          )
                self.thread_start()

if __name__=="__main__":
        record=Paudio(updatesPerSecond=10)
        record.record_start()
        lastRead=record.chunksRead
        while True:
                while lastRead == record.chunksRead:
                        time.sleep(.01)
                lastRead=record.chunksRead
	
