# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 328)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Select_cb = QtWidgets.QComboBox(self.centralwidget)
        self.Select_cb.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Select_cb.setFont(font)
        self.Select_cb.setObjectName("Select_cb")
        self.Select_cb.addItem("")
        self.Run_pb = QtWidgets.QPushButton(self.centralwidget)
        self.Run_pb.setGeometry(QtCore.QRect(10, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Run_pb.setFont(font)
        self.Run_pb.setObjectName("Run_pb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 331))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.raise_()
        self.Select_cb.raise_()
        self.Run_pb.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Select_cb.setItemText(0, _translate("MainWindow", "Chọn Port"))
        self.Run_pb.setText(_translate("MainWindow", "Chạy"))
        self.label.setText(_translate("MainWindow", "ABCDEF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
