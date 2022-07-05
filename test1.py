import cv2 as cv

capture = cv.VideoCapture(0)
n = 0
greyBol = False
value = 50

while True:

    n += value

    wut, frame = capture.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    if greyBol:
        actual_frame = hsv
    else:
        actual_frame = frame

    if n >= 100:
        value = value * -1
        greyBol = True
    if n <= 0:
        value = value * -1
        greyBol = False

    cv.imshow("Cam0", actual_frame)


    if cv.waitKey(1) == ord("q"):
        break


capture.release()
cv.destroyAllWindows()