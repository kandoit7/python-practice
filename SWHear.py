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
        def __init__(self, device=None, rate=None, updatesPerSecond=10):
                self.p = pyaudio.PyAudio()
                self.RATE = rate
                self.CHUNK = 4096
                self.updatesPerSecond=updatesPerSecond
                self.FORMAT = pyaudio.paInt16
                self.CHANNELS = 1
                self.device = device
                self.chunksRead=0

        def valid_low_rate(self, device):
                for testrate in [48000]:
                        if self.valid_test(device, testrate):
                                return testrate
                return None

        def valid_test(self, device, rate=48000):
                try:
                        self.info = self.p.get_device_info_by_index(device)
                        if not self.info["maxInputChannels"] > 0:
                                return False
                        stream = self.p.open(format=pyaudio.paInt16, channels=self.CHANNELS,
                                             input_device_index=device, frames_per_buffer=self.CHUNK,
                                             rate=int(self.info["defaultSampleRate"]), input=True)
                        stream.close()
                        return True
                except:
                        return False

        def valid_input_devices(self):
                mics = []
                for device in range(self.p.get_device_count()):
                        if self.valid_test(device):
                                mics.append(device)
                if len(mics) == 0:
                        print("no microphone devices found!")
                else:
                        print("found %d microphone devices: %s" % (len(mics), mics))
                return mics

        def initiate(self):
                if self.device is None:
                        self.device = self.valid_input_devices()[0]  # pick the first one
                if self.RATE is None:
                        self.RATE = self.valid_low_rate(self.device)
                self.CHUNK = int(self.RATE / self.updatesPerSecond)  # hold one tenth of a second in memory
                if not self.valid_test(self.device, self.RATE):
                        print("guessing a valid microphone device/rate...")
                        self.device = self.valid_input_devices()[0]  # pick the first one
                        self.RATE = self.valid_low_rate(self.device)
                self.datax = np.arange(self.CHUNK) / float(self.RATE)
                print self.datax.size
                msg = 'recording from "%s" ' % self.info["name"]
                msg += '(device %d) ' % self.device
                msg += 'at %d Hz' % self.RATE
                print(msg)

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
                self.initiate()
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
	
