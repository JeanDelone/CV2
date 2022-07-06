import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.path.join(os.path.dirname(__file__))


img = cv.imread(path + "/Images/trzecie prof 2.png")
img = cv.imread(path + "/Images/janek4.jpg")
# img = cv.imread(path + "/Images/awatar low res.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 140, 255, -1)
masked = cv.bitwise_and(gray, gray, mask = circle)


cv.imshow("img", img)
cv.imshow("gray", gray)
cv.imshow("masked", masked)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
gray_hist_masked = cv.calcHist([gray], [0], masked, [256], [0,256])

plt.plot(gray_hist)
plt.plot(gray_hist_masked)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)