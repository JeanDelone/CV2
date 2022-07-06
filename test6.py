import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

_, frame = capture.read()
blank = np.zeros((frame.shape[:2]), dtype="uint8")
circle = cv.circle(blank, (frame.shape[1]//2, frame.shape[0]), 115, (255,255,255), -1)



while True:

    _, frame = capture.read()
    cv.imshow("frame", frame)
    cv.imshow("circle", circle)
    masked = cv.bitwise_and(frame, frame, mask = circle)

    cv.imshow("essa", masked)







    if cv.waitKey(1) == ord("q"):
        break


capture.release()
cv.destroyAllWindows()