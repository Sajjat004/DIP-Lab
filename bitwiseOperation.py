import matplotlib.pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread('image3.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('image4.png', cv2.IMREAD_COLOR)

img = cv2.bitwise_xor(img1, img2, mask = None)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#
