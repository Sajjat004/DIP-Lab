import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('saju.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()