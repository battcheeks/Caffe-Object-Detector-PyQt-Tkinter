import cv2
import numpy as np
from time import sleep
def nothing(x):
    pass

cap = cv2.VideoCapture(1)
w=cv2.namedWindow("Trackbars for HSV Values")
cv2.createTrackbar("LH", "Trackbars for HSV Values", 160, 180, nothing)
cv2.createTrackbar("HH", "Trackbars for HSV Values", 180, 180, nothing)
cv2.createTrackbar("LS", "Trackbars for HSV Values", 100, 255, nothing)
cv2.createTrackbar("HS", "Trackbars for HSV Values", 255, 255, nothing)
cv2.createTrackbar("LV", "Trackbars for HSV Values", 100, 255, nothing)
cv2.createTrackbar("HV", "Trackbars for HSV Values", 255, 255, nothing)
cv2.createTrackbar("X", "Trackbars for HSV Values", 250, 255, nothing)
cv2.createTrackbar("Y", "Trackbars for HSV Values", 255, 255, nothing)


if cap.isOpened():
            while (True):
                ret, frame = cap.read()
                frame_gau_blur = cv2.GaussianBlur(frame, (3, 3), 0)
                hsv = cv2.cvtColor(frame_gau_blur, cv2.COLOR_BGR2HSV)
                l_h = cv2.getTrackbarPos("LH", "Trackbars for HSV Values")
                h_h = cv2.getTrackbarPos("HH", "Trackbars for HSV Values")
                l_s = cv2.getTrackbarPos("LS", "Trackbars for HSV Values")
                h_s = cv2.getTrackbarPos("HS", "Trackbars for HSV Values")
                l_v = cv2.getTrackbarPos("LV", "Trackbars for HSV Values")
                h_v = cv2.getTrackbarPos("HV", "Trackbars for HSV Values")
                x_l = cv2.getTrackbarPos("X", "Trackbars for HSV Values")
                y_h = cv2.getTrackbarPos("Y", "Trackbars for HSV Values")
                min_l = cv2.getTrackbarPos("min", "Trackbars for HSV Values")
                max_h = cv2.getTrackbarPos("max", "Trackbars for HSV Values")
                lower_blue = np.array([l_h, l_s, l_v])
                higher_blue = np.array([h_h, h_s, h_v])
                blue_range = cv2.inRange(hsv, lower_blue, higher_blue)
                res_blue = cv2.bitwise_and(frame_gau_blur, frame_gau_blur, mask=blue_range)
                blue_s_gray = cv2.cvtColor(res_blue, cv2.COLOR_BGR2GRAY)
                canny_edge = cv2.Canny(blue_s_gray, x_l, y_h)
                circles = cv2.HoughCircles(canny_edge, cv2.HOUGH_GRADIENT, dp=2, minDist=100, param1=30, param2=150,
                                           minRadius=0, maxRadius=140)
                cir_cen = []
                if circles is not None:
                    for i in circles[0, :]:
                        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                        cv2.circle(frame, (i[0], i[1]), 1, (0, 0, 255), 3)
                        cir_cen.append((i[0] + i[1]) / 2)
                sum = 0
                for i in range(0, len(cir_cen)):
                    # print((cir_cen[i]))
                    sum = sum + cir_cen[i]
                if circles is not None:
                    print(sum / len(cir_cen))
                cv2.imshow('circles', frame)

                # cv2.imshow('gray', blue_s_gray)
                cv2.imshow('canny', canny_edge)

                # print((lines[0]+lines[1])/2)
                sleep(0.005)
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break

            cv2.destroyAllWindows()
else:
            print('no cam')