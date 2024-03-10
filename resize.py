import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('saju.jpg', cv2.IMREAD_COLOR)

half = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.8)
bigger = cv2.resize(image, (1200, 1500))
stretch_near = cv2.resize(image, (780, 700), interpolation = cv2.INTER_LINEAR)

Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4
 
for i in range(count):
  plt.subplot(2, 2, i + 1)
  plt.title(Titles[i])
  plt.imshow(images[i])
 
plt.show()