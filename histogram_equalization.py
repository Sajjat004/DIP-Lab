import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('image6.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.equalizeHist(img)

res = np.hstack((img, img1))

cv2.imshow('final result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()