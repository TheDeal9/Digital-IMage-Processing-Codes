import numpy as np
import cv2

img1 = cv2.imread("circle.png")
img2 = cv2.imread("hexawhite.png")

img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

img_and = cv2.bitwise_and(img1, img2, mask = None)
img_or = cv2.bitwise_or(img1, img2, mask = None)
img_not = cv2.bitwise_not(img1, img2, mask = None)
img_xor = cv2.bitwise_xor(img1, img2, mask = None)

#cv2.imshow("original image 1", img1)
#cv2.imshow("original image 2", img2)
cv2.imshow("And-Operation image 2", img_and)
cv2.imshow("Or-Operation image 2", img_or)
cv2.imshow("Not-Operation image 2", img_not)
cv2.imshow("Xor-Operation image 2", img_xor)
cv2.waitKey(5000)
