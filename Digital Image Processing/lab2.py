import numpy as np
import cv2
img = cv2.imread('mira.jpeg')

matrix1 = np.ones(img.shape, dtype = "uint8") * 2
matrix2 = np.ones(img.shape, dtype = "uint8") - 200

#multiplication
img_brighter = cv2.multiply(img, matrix1)

#substraction
img_darker = cv2.subtract(img, matrix2)

#display
cv2.imshow("Original image", img)
cv2.imshow("brighter image", img_brighter)
cv2.imshow("Darker image", img_darker)
cv2.waitKey(5000)