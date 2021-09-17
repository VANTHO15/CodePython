from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from threading import Thread
from itertools import groupby


class PlotCanvas(FigureCanvas):
    def __init__(self, parent, x, y, width, height, num_show=100, dpi=100, real_show=1):
        self.data = {}
        self.x_ = x
        self.y_ = y
        self.width_ = width
        self.height_ = height
        self.num_show = num_show
        self.step = num_show//real_show
        fig = Figure(figsize=(width/dpi, height/dpi), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)
        self.figure.subplots_adjust(0, 0, 1, 1)
        self.ax = self.figure.add_subplot(111)
        self.ax.axis('off')
        self.setGeometry(x, y, width, height)
        self.ax.margins(0, 0)
        self.show()
        self.ani = animation.FuncAnimation(self.figure, self.animate, interval=30)
        Thread(target=self.init).start()

    def init(self):
        time.sleep(1)
        self.ani.event_source.stop()

    def start_plot(self):
        self.clear_all()
        self.ani.event_source.start()

    def stop_plot(self):
        self.ani.event_source.stop()

    def import_data(self, name, value):
        if self.data.get(name) is None:
            self.data[name] = []
        self.data[name].append(value)

    def clear_all(self):
        self.data = {}
        self.ax.clear()

    def setGeometry(self, x, y, w, h):
        self.move(x, y)
        FigureCanvas.resize(self, w, h)
        self.x_ = x
        self.y_ = y
        self.width_ = w
        self.height_ = h

    def animate(self, i):
        if len(self.data) > 0:
            self.ax.clear()
            if len(self.data) > self.num_show:
                num_show = max(0, (len(self.data) - self.num_show) - (len(self.data) % self.step) - 1)
            else:
                num_show = -self.num_show
            self.ax.plot(self.data[num_show::self.step])
        self.ax.axis('off')