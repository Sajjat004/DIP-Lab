import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)

histr = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr)
plt.show()

rows, cols = img.shape

d = {}

for i in range(rows):
  for j in range(cols):
    x = img[i][j]
    if x in d:
      d[x] += 1
    else:
      d[x] = 1

sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

print("map input to output")
cnt = 0
d1 = {}
for key, value in sorted_items:
    print(cnt, " = ", key)
    d1[key] = cnt
    cnt += 1

for i in range(rows):
  for j in range(cols):
    img[i][j] = d1[img[i][j]]

histr = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(histr)
plt.show()