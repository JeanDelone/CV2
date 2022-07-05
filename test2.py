import cv2 as cv
import numpy as np
import os
import sys

wd_path = os.path.join(os.path.dirname(__file__))


# img = cv.imread(wd_path + "/Images/trzecieprof 1.png")
img = cv.imread(wd_path + "/Images/trzecie prof 1.png")
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)


if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, b, g])
cv.imshow("merged", merged)

merged_blue = cv.merge([b, blank, blank])
merged_green = cv.merge([blank, g, blank])
merged_red = cv.merge([blank, blank, r])

merged2 = cv.merge([merged_blue, merged_green, merged_red])
cv.imshow("merged", merged2)

cv.imshow("merged_blue", merged_blue)
cv.imshow("merged_green", merged_green)
cv.imshow("merged_red", merged_red)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("fmal.jpg", img)