import matplotlib.pyplot as plt
import numpy as np
import cv2

src_img = cv2.imread('saju.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = src_img.shape
dest_img = np.zeros((rows, cols))

for i in range(rows):
  for j in range(cols):
    if (src_img[i][j] >= 127):
      dest_img[i][j] = 1

cv2.imshow('Fnal Image', dest_img)
cv2.waitKey(0)
cv2.destroyAllWindows()