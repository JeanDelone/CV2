import cv2 as cv
import os

path = os.path.join(os.path.dirname(__file__))

img = cv.imread(path + "/Images/janek4.jpg")
# img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(path + "/Detectors/frontal_face_default.xml")

capture = cv.VideoCapture(0)

_, frame = capture.read()

while True:
    _, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rects = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)
    for (x,y,w,h) in faces_rects:
        cv.rectangle(frame, (x,y), (x+h, y+h), (240,0,240), 3)


    cv.imshow("Cam0", frame)
    if cv.waitKey(1) == ord("q"):
        break


capture.release()
cv.destroyAllWindows()
