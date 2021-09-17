from PyQt5 import QtCore, QtGui, QtWidgets
from d_interface import Ui_MainWindow
import sys
from Serial_Connect import *
from threading import Thread
from e_matplotlib import PlotCanvas


class SerialTool:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        # MainWindow.closeEvent = self.__stop
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.Select_init()
        self.event_init()
        self.m = PlotCanvas(MainWindow,
                            x=151, y=10,
                            width=1000, height=271,
                            num_show=1500, dpi=50,
                            real_show=300)
        self.run = False
        MainWindow.show()
        sys.exit(app.exec_())

    def event_init(self):
        self.ui.Run_pb.clicked.connect(self.Run_pb_clicked_event)
        self.ui.Run_pb.setEnabled(False)  # 1
        self.ui.Select_cb.currentIndexChanged.connect(self.Select_cb_IndexChanged_event)

    def Select_init(self):
        self.Serial_port_list = get_SerialPort()
        for port_data in self.Serial_port_list:
            str_ = '{}'.format(port_data['Port'])
            self.ui.Select_cb.addItem(str_)

    def Run_pb_clicked_event(self):
        if self.ui.Run_pb.text() == 'Chạy':
            self.ui.Run_pb.setText('Dừng')
            self.__start()
        elif self.ui.Run_pb.text() == 'Dừng':
            self.ui.Run_pb.setText('Chạy')
            self.__stop()
        print('Run_pb_clicked_event')

    def Select_cb_IndexChanged_event(self):
        if self.ui.Select_cb.currentIndex() > 0:
            self.ui.Run_pb.setEnabled(True)
        else:
            self.ui.Run_pb.setEnabled(False)
        print('Select_cb_IndexChanged_event')

    def __start(self):
        self.ui.Select_cb.setEnabled(False)
        self.Serial = SerialConnect(self.Serial_port_list[self.ui.Select_cb.currentIndex()-1]['Port'])
        self.run = True
        self.m.start_plot()
        Thread(target=self.Serial_start).start()
        Thread(target=self.get_data).start()

    def __stop(self):
        self.run = False
        self.ui.Select_cb.setEnabled(True)
        self.save_file()
        self.Serial.data = []

    def Serial_start(self):
        self.Serial.start()
        while self.run:
            if len(self.Serial.data) > 0:
                self.ui.label.setText('{:.2f}'.format(self.Serial.data[-1]))
                # print('{:.2f}'.format(self.Serial.data[-1]))
        self.Serial.stop()
        print('Count: ', self.Serial.count)

    def save_file(self):
        location = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,
                                                         caption='Choose a storage location',
                                                         filter='Text Files (*.txt)')[0]
        if location is '':
            return
        while not self.Serial.data_queue.empty():
            time.sleep(0.001)
        with open(location, 'w') as file_txt:
            data = self.Serial.data
            str_ = []
            for i in range(0, len(data)):
                str_.append('{}'.format(data[i]))
            file_txt.write('\n'.join(str_))

    def get_data(self):
        try:
            while self.run:
                if len(self.Serial.data) > 0:
                    self.m.data = self.Serial.data
                time.sleep(0.000000000001)
        except BaseException as be:
            print(be)


if __name__ == '__main__':
    SerialTool()
