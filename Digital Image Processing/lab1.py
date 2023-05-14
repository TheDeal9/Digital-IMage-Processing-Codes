import cv2
import numpy as np

img = cv2.imread("WhatsApp Image 2023-01-20 at 14.17.19.jpg")

images = []

for _ in range(20):
    img1 = img.copy()
    cv2.randn(img1, (0, 0, 0), (50, 50, 50))
    images.append(img+img1)

img_avg = np.zeros((img.shape[0], img.shape[1], img.shape[2]), np.float32)

for im in images:

    img_avg = img_avg+im/20

    img_avg = np.array(np.round(img_avg), dtype=np.uint8)



cv2.imshow("original image", img)
cv2.imshow("corrupted image", images[1])
cv2.imshow("average image", img_avg)

cv2.waitKey(50000)
cv2.destroyAllWindows()