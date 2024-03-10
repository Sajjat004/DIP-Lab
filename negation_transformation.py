import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('saju.jpg', cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape
for i in range(rows):
  for j in range(cols):
    img[i][j] = 255 - img[i][j]


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()