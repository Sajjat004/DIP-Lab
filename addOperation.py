import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('image2.jpg', cv2.IMREAD_COLOR)
img = cv2.add(img1, img2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
