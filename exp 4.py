import cv2
from matplotlib import pyplot as plt
import numpy as np

# Step 1: Read the image
image = cv2.imread('D:\computer vision lab\exp 4.png')  # replace with your filename

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Threshold to binary
_, binary_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)

# Step 4: Dilation
kernel = np.ones((5, 5), np.uint8)
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# Step 5: Display results
plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Binary Image")
plt.imshow(binary_image, cmap='gray')
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Dilated Image")
plt.imshow(dilated_image, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()
