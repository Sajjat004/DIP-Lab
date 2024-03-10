import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('saju.jpg', cv2.IMREAD_GRAYSCALE)

c = 255/(np.log(1 + np.max(img))) 
gamma = 0.1
rows, cols = img.shape
for i in range(rows):
  for j in range(cols):
    img[i][j] = c * img[i][j] ** gamma

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()