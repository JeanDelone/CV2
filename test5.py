import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (blank.shape[1] - 30,blank.shape[0] - 30), (255,0,255), -1)
circle = cv.circle(blank.copy(), (blank.shape[1]//2,blank.shape[0]//2), (blank.shape[1]//2) - 60, (255,0,255), -1)
circle2 = cv.circle(blank.copy(), (blank.shape[1]//2,blank.shape[0]//2), (blank.shape[1]//2), (0,0,255), -1)


cv.imshow("Rectangle", rectangle)
cv.imshow("circle", circle2)

btiwise_and = cv.bitwise_xor(rectangle, circle2)
cv.imshow("and", btiwise_and)

cv.waitKey(0)