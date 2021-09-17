import serial
import serial.tools.list_ports as list_ports
from threading import Thread
import random
import time
import queue


def get_SerialPort():
    ports = list_ports.comports()
    avaliable = []
    for port, desc, hwid in sorted(ports):
        avaliable.append({'Port': port,
                          'Name': desc,
                          'Properties': hwid})
    return avaliable


class SerialConnect:
    def __init__(self, port, baudrate=9600,
                 bytesize=serial.EIGHTBITS,
                 parity=serial.PARITY_NONE,
                 stopbits=serial.STOPBITS_ONE,
                 timeout=0.1):

        self.SerialObject = serial.Serial(port,
                                          baudrate=baudrate,
                                          bytesize=bytesize,
                                          parity=parity,
                                          stopbits=stopbits,
                                          timeout=timeout)
        self.run = False
        self.error = False
        self.count = 0
        self.data = []
        self.data_queue = queue.Queue()

    def write(self, msg):
        if self.run:
            if not self.SerialObject.is_open:
                self.SerialObject.open()
            packet = bytearray()
            for ms in msg:
                packet.append(ms)
            self.SerialObject.write(packet)

    def write_thread(self):
        while self.run:
            data_send = random.randint(0, 100)
            self.write([data_send])
            time.sleep(0.01)

    def read_thread(self):
        if not self.SerialObject.is_open:
            self.SerialObject.open()
        while self.run:
            try:
                ser_bytes = self.SerialObject.read()
                if ser_bytes is b'':
                    continue
                self.count += 1
                self.data_queue.put(ser_bytes)
            except BaseException as be:
                print("Keyboard Interrupt", be)
                self.run = False
                self.error = True
                break

    def start(self):
        self.run = True
        self.error = False
        Thread(target=self.read_thread).start()
        # Thread(target=self.write_thread).start()
        Thread(target=self.mean_thread).start()

    def stop(self):
        self.run = False

    def mean_thread(self):
        while True:
            if self.data_queue.empty():
                if not self.run:
                    break
            value = int(self.data_queue.get().hex(), 16)
            if len(self.data) > 0:
                value = (value + self.data[-1])/2
            self.data.append(value)
            # print(value, len(self.data))


if __name__ == '__main__':
    Serial = SerialConnect('COM3')
    Serial.start()
    time.sleep(10)
    Serial.stop()
    print('Count: {}'.format(Serial.count))