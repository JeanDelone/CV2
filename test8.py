import cv2 as cv
import os
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__))

img = cv.imread(path + "/Images/janek4.jpg")
b, g, r = cv.split(img)
blues = cv.calcHist([b], [0], None, [256], [0,256])
greens = cv.calcHist([g], [0], None, [256], [0,256])
reds = cv.calcHist([r], [0], None, [256], [0,256])

plt.plot(blues, color = "#0000ff")
plt.plot(greens, color = "#00ff00")
plt.plot(reds, color = "#ff0000")
plt.show()