import cv2 as cv
import os

path = os.path.join(os.path.dirname(__file__))

img = cv.imread(path + "/Images/grupa.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
haar_cascade = cv.CascadeClassifier(path + "/Detectors/frontal_face_default.xml")
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (240,0,240), 2)


cv.imshow("grupa", img)


cv.waitKey(0)