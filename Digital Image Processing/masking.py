import cv2 as cv
import numpy as np

img = cv.imread('pokemon.jpg')
cv.imshow('Original image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),200,255, -1)
cv.imshow('Mask',circle)

masked = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Masked Image', masked)

cv.waitKey(5000)