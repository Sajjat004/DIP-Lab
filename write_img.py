import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('saju.jpg', cv2.IMREAD_GRAYSCALE)
filename = 'saju_copy.jpg'
check = cv2.imwrite(filename, img)
if check == True:
  print('Image saved successfully')
else:
  print('image save failed')