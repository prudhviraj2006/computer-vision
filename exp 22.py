import cv2
import numpy as np

# Step 1: Load image (grayscale)
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)  # Replace with your image

# Step 2: Define the kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Step 3: Apply the kernel
sharpened = cv2.filter2D(img, -1, kernel)

# Step 4: Show images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened (Positive Center)", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
