import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPlainTextEdit
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import imutils
import settings
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow
from sdpx import Ui_OtherWind
from shape import Ui_shape

class Ui_MainWindow(object):
    '''def closeEvent(self, *args, **kwargs):
        super(QtGui.QMainWindow, self).closeEvent(*args, **kwargs)
        print("you just closed the pyqt window!!! you are awesome!")'''
    def openWind(self):
        self.wind=QtWidgets.QMainWindow()
        self.ui= Ui_OtherWind()
        self.ui.setupUi(self.wind)
        self.wind.show()
    def openWin(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_shape()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 230)
        #MainWindow.resize(160, 220)
        MainWindow.move(450,250)
        MainWindow.setStyleSheet(" background-color:rgb(0, 85, 127) ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 150, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 50, 150, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 100, 150, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 150, 150, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        '''self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310,210,100,23))
        self.pushButton_5.setObjectName("pushButton_5")'''
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 0, 250, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_3.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_2.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_4.setStyleSheet(" background-color: rgb(170, 170, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Software Development Project"))
        self.pushButton.setText(_translate("MainWindow", "Shape Detection"))
        self.pushButton_2.setText(_translate("MainWindow", "Object Tracking"))
        self.pushButton_3.setText(_translate("MainWindow", "Haar-Cascade Detection"))
        self.pushButton_4.setText(_translate("MainWindow", "Object Detection"))
        # self.pushButton_5.setText(_translate("MainWindow", "Execute tracking"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Hi welcome to my Software Development Project. The features of my Project includes custom object detection which I have tried to achieve with the help of a custom built neural network. I have also tried to explain different image processing algorithms just to show the different types of algorithms which can help us detect objects. Finally I have combined all the aspects of my project into a GUI that has been coded using two different GUI makers PyQt5 and Tkinter respectively.PyQt5 is used for the first GUI that appears in program and further on Tkinter is used the GUI model which uses Neural Networks for Object Detection.</span></p></body></html>"))
        self.textBrowser.setStyleSheet("background-color: white; color:black;font-size: 12px;height: 40px;width: 110px;");
        self.pushButton_4.clicked.connect(self.on_click)
        self.pushButton_2.clicked.connect(self.openWindow)
        self.pushButton.clicked.connect(self.openWind)
        self.pushButton_3.clicked.connect(self.on_click2)


        '''self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.openWindow())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Shape Detection"))
        self.pushButton_2.setText(_translate("MainWindow", "Object Tracking"))
        self.pushButton_3.setText(_translate("MainWindow", "Haar-Cascade Detection"))
        self.pushButton_4.setText(_translate("MainWindow", "Object Detection"))
        #self.pushButton_5.setText(_translate("MainWindow", "Execute tracking"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Hi welcome to my Software Development Project. The features of my Project includes custom object detection which I have tried to achieve with the help of a custom built neural network. I have also tried to explain different image processing algorithms just to show the different types of algorithms which can help us detect objects. Finally I have combined all the aspects of my project into a GUI that has been coded using two different GUI makers PyQt5 and Tkinter respectively.PyQt5 is used for the first GUI that appears in program and further on Tkinter is used the GUI model which uses Neural Networks for Object Detection.</span></p></body></html>"))
        self.radioButton.setText(_translate("MainWindow", "csrt"))
        self.radioButton_2.setText(_translate("MainWindow", "kcf"))
        self.radioButton_3.setText(_translate("MainWindow", "mosse"))'''

    def on_click2(self):
        print("Starting Haar-Cascade Detection")
        exec (open("face.py").read())

    def appExec():
        app = QApplication(sys.argv)
        # and so on until we reach:
        app.exec_()
        print("my message...")
    def on_click3(self):
        print("Shape Detection")


    def on_click(self):
        print("Executing Object Detection")
        import tkinter as tk
        import cv2
        from PIL import Image, ImageTk
        import numpy as np
        import imutils
        import settings


        def start_video():
            settings.start_video = True
            show_frame()

        def stop_video():
            settings.start_video = False
            settings.start_processing = False
            lmain.config(image='')

        def start_process():
            settings.start_processing = True

        def stop_process():
            settings.start_processing = False

        def show_frame():
            if not settings.start_video:
                return None
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = imutils.resize(frame, width=400)

            if settings.start_processing:
                frame = process_frame(frame)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

        def process_frame(img):
            (h, w) = img.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)),
                                         0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()
            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.8:
                    idx = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    label = "{}: {:.2f}%".format(CLASSES[idx],
                                                 confidence * 100)
                    cv2.rectangle(img, (startX, startY), (endX, endY),
                                  COLORS[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(img, label, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
                    print(label)
            return img

        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "monitor"]

        COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

        # load our serialized model from disk
        print("Loading model...")
        net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
        cap = cv2.VideoCapture(1)

        window = tk.Tk()
        window.title("Tkinter GUI")
        window.geometry('700x420')
        lbl = tk.Label(window, text="Detection using Neural Network.", font=("Arial Bold", 24), fg='blue')
        lbl.grid(column=1, row=0)
        imageFrame = tk.Frame(window, width=600, height=500,bg='black')
        imageFrame.grid(row=1, column=1, padx=10, pady=2)
        lmain = tk.Label(imageFrame, text="Press Start Video", background='black', fg='white')
        lmain.grid(row=1, column=1)
        startVideoStreamBtn = tk.Button(window, text="Start Video", command=start_video, bg='red', fg='white')
        startVideoStreamBtn.grid(column=0, row=3, padx=15)
        stopVideoStreamBtn = tk.Button(window, text="Stop Video", command=stop_video, bg='red', fg='white')
        stopVideoStreamBtn.grid(column=0, row=5, padx=15)
        startProcessBtn = tk.Button(window, text="Start Execution", command=start_process, bg='red', fg='white')
        startProcessBtn.grid(column=2, row=3)
        stopProcessBtn = tk.Button(window, text="Stop Execution", command=stop_process, bg='red', fg='white')
        stopProcessBtn.grid(column=2, row=5)
        '''startFeatureBtn = tk.Button(window, text="Start Feature Detection", command=start_opencv)
        startFeatureBtn.grid(column=2, row=2)
        stopFeatureBtn = tk.Button(window, text="Stop Feature Detection", command=stop_opencv)
        stopFeatureBtn.grid(column=2, row=3)'''
        window.mainloop()
        settings.start_processing = False



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




