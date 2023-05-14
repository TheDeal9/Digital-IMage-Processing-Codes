import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('gigi.jpg',0)
#0 is for greyscale image
#1 is for colour images
x,y = image.shape
z=np.zeros((x,y))
for i in range (0,x):
    for j in range(0,y):
        if(image[i][j]>30 and image[i][j]<150):
            z[i][j]=255
        else:
            z[i][j] = 0
slicing = np.hstack((image, z))
plt.title("Original Image and Grayscale image slicing with background")
plt.imshow(slicing, 'gray')
plt.show()