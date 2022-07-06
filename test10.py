import cv2 as cv
import os

from cv2 import ADAPTIVE_THRESH_MEAN_C

path = os.path.join(os.path.dirname(__file__))

img = cv.imread(path + "/Images/janek4.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)






adaptive_threshhold = cv.adaptiveThreshold(gray, 255, ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
threshold, thresh = cv.threshold(gray, 110, 255, cv.THRESH_BINARY)

cv.imshow("img", img)
cv.imshow("adaptive", adaptive_threshhold)
cv.imshow("thresh", thresh)

cv.waitKey(0)