import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image
img = cv2.imread('D:\computer vision lab\exp 5.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary
_, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Erode the image
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(binary, kernel, iterations=1)

# Show images
plt.subplot(1, 2, 1)
plt.title("Binary")
plt.imshow(binary, cmap='gray')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Eroded")
plt.imshow(eroded, cmap='gray')
plt.axis("off")

plt.show()
