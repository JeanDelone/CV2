import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

_, frame = capture.read()
blank = np.zeros(frame.shape[:2], dtype="uint8")

while True:
    _, frame = capture.read()
    b, g, r = cv.split(frame)
    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])


    cv.imshow("Cam0", blue)
    cv.imshow("Cam1", green)
    cv.imshow("Cam2", red)

    if cv.waitKey(1) == ord("q"):
        break


capture.release()
cv.destroyAllWindows()