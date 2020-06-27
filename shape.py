# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shape.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_shape(object):
    def setupUi(self, shape):
        shape.setObjectName("shape")
        shape.resize(215, 89)
        self.centralwidget = QtWidgets.QWidget(shape)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 221, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        shape.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(shape)
        self.statusbar.setObjectName("statusbar")
        shape.setStatusBar(self.statusbar)

        self.retranslateUi(shape)
        QtCore.QMetaObject.connectSlotsByName(shape)

    def retranslateUi(self, shape):
        _translate = QtCore.QCoreApplication.translate
        shape.setWindowTitle(_translate("shape", "MainWindow"))
        self.pushButton.setText(_translate("shape", "Circle"))
        self.pushButton_2.setText(_translate("shape", "Line"))
        self.label.setText(_translate("shape", " Choose type of shape detection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shape = QtWidgets.QMainWindow()
    ui = Ui_shape()
    ui.setupUi(shape)
    shape.show()
    sys.exit(app.exec_())
