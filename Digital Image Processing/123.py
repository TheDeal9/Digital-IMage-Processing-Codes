import cv2
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt

image= cv2.imread("mira.jpeg")
cv2.imshow(image)
plt.hist(image)
# cv2.imhist(image)
cv2.waitKey(5000)