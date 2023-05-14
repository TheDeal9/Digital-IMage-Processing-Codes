import cv2
import numpy as np

img = cv2.imread('gigi.jpg',0)

kernel_3 = np.ones((11,11), dtype=np.float32)/121

output = cv2.filter2D(img, -1, kernel_3)

cv2.imshow('blur image', output)
cv2.imshow("Original Image", img)

cv2.waitKey(5000)
cv2.destroyAllWindows()
