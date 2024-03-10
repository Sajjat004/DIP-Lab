import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('image5.jpg', cv2.IMREAD_GRAYSCALE)

histr = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr)
plt.show()
