import cv2 as cv
import os
import time

path = os.path.join(os.path.dirname(__file__),)

img = cv.imread(path + "/Images/janek4.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

capture = cv.VideoCapture(0)
_, frame = capture.read()
gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
n = 0
threshhold, thresh = cv.threshold(gray, n, 255, cv.THRESH_BINARY)

while True:
    _, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    threshhold, thresh = cv.threshold(gray, n, 255, cv.THRESH_BINARY)
    n+=1
    cv.imshow("thresh", thresh)

    if cv.waitKey(1) == ord("q"):
        break



    cv.imshow("Gray", gray)


capture.release()
cv.destroyAllWindows()