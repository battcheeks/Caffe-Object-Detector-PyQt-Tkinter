
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWind(object):
    def setupUi(self, OtherWind):
        OtherWind.setObjectName("OtherWind")
        OtherWind.resize(250, 100)
        self.centralwidget = QtWidgets.QWidget(OtherWind)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 100, 75))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 10, 100, 75))
        self.pushButton_3.setObjectName("pushButton_3")
        OtherWind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        OtherWind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWind)
        self.statusbar.setObjectName("statusbar")
        OtherWind.setStatusBar(self.statusbar)
        OtherWind.setStyleSheet(" background-color:rgb(0, 85, 127) ;")
        self.pushButton.setStyleSheet(" background-color: rgb(170, 170, 255);")
        self.pushButton_3.setStyleSheet(" background-color: rgb(170, 170, 255);")


        self.retranslateUi(OtherWind)
        QtCore.QMetaObject.connectSlotsByName(OtherWind)

    def retranslateUi(self, OtherWind):
        _translate = QtCore.QCoreApplication.translate
        OtherWind.setWindowTitle(_translate("OtherWind", "Hough"))
        self.pushButton.setText(_translate("OtherWind", "Hough Lines"))

        self.pushButton_3.setText(_translate("OtherWind", "Hough Circles"))
        self.pushButton.clicked.connect(self.on_click)

        self.pushButton_3.clicked.connect(self.on_click3)
    def on_click(self):
        print("Starting Code for Line Detection")
        import cv2 as cv
        import numpy as np
        import matplotlib.pyplot as plt

        def do_canny(frame):
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            blur = cv.GaussianBlur(gray, (5, 5), 0)
            canny = cv.Canny(blur, 50, 150)
            return canny

        def do_segment(frame):
            height = frame.shape[0]

            polygons = np.array([
                [(0, height), (800, height), (380, 290)]
            ])

            mask = np.zeros_like(frame)

            cv.fillPoly(mask, polygons, 255)

            segment = cv.bitwise_and(frame, mask)
            return segment

        def calculate_lines(frame, lines):
            left = []
            right = []

            for line in lines:
                # Reshapes line from 2D array to 1D array
                x1, y1, x2, y2 = line.reshape(4)
                # Fits a linear polynomial to the x and y coordinates and returns a vector of coefficients which describe the slope and y-intercept
                parameters = np.polyfit((x1, x2), (y1, y2), 1)
                slope = parameters[0]
                y_intercept = parameters[1]
                # If slope is negative, the line is to the left of the lane, and otherwise, the line is to the right of the lane
                if slope < 0:
                    left.append((slope, y_intercept))
                else:
                    right.append((slope, y_intercept))
            # Averages out all the values for left and right into a single slope and y-intercept value for each line
            left_avg = np.average(left, axis=0)
            right_avg = np.average(right, axis=0)
            # Calculates the x1, y1, x2, y2 coordinates for the left and right lines
            left_line = calculate_coordinates(frame, left_avg)
            right_line = calculate_coordinates(frame, right_avg)
            return np.array([left_line, right_line])

        def calculate_coordinates(frame, parameters):
            slope, intercept = parameters
            # Sets initial y-coordinate as height from top down (bottom of the frame)
            y1 = frame.shape[0]
            # Sets final y-coordinate as 150 above the bottom of the frame
            y2 = int(y1 - 150)
            # Sets initial x-coordinate as (y1 - b) / m since y1 = mx1 + b
            x1 = int((y1 - intercept) / slope)
            # Sets final x-coordinate as (y2 - b) / m since y2 = mx2 + b
            x2 = int((y2 - intercept) / slope)
            return np.array([x1, y1, x2, y2])

        def visualize_lines(frame, lines):
            # Creates an image filled with zero intensities with the same dimensions as the frame
            lines_visualize = np.zeros_like(frame)
            # Checks if any lines are detected
            if lines is not None:
                for x1, y1, x2, y2 in lines:
                    # Draws lines between two coordinates with green color and 5 thickness
                    cv.line(lines_visualize, (x1, y1), (x2, y2), (0, 255, 0), 5)
            return lines_visualize

        # The video feed is read in as a VideoCapture object
        cap = cv.VideoCapture("input.mp4")
        while (cap.isOpened()):
            # ret = a boolean return value from getting the frame, frame = the current frame being projected in the video
            ret, frame = cap.read()
            canny = do_canny(frame)
            cv.imshow("canny", canny)
            # plt.imshow(frame)
            # plt.show()
            segment = do_segment(canny)
            hough = cv.HoughLinesP(segment, 2, np.pi / 180, 100, np.array([]), minLineLength=100, maxLineGap=50)

            lines = calculate_lines(frame, hough)
            # Visualizes the lines
            lines_visualize = visualize_lines(frame, lines)
            #cv.imshow("hough", lines_visualize)

            output = cv.addWeighted(frame, 0.9, lines_visualize, 1, 1)

            cv.imshow("output", output)

            if cv.waitKey(10) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def on_click2(self):
        print("Starting Segmentation for Image using Connected Components Analysis")
        exec (open("segmentation.py").read())
    def on_click3(self):
        print("Starting Code for Circle shape Detection")
        exec (open("circle.py").read())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWind = QtWidgets.QMainWindow()
    ui = Ui_OtherWind()
    ui.setupUi(OtherWind)
    OtherWind.show()
    sys.exit(app.exec_())
