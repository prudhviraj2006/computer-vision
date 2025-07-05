import cv2
import numpy as np

# Step 1: Load the image (grayscale)
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)  # Replace with your image

# Step 2: Blur the image
blurred = cv2.GaussianBlur(img, (9, 9), 10)

# Step 3: Set the boost factor
A = 1.5  # Try 2.0 or 3.0 for stronger sharpening

# Step 4: Apply high-boost filtering
high_boost = cv2.addWeighted(img, A, blurred, -1, 0)

# Step 5: Show results
cv2.imshow("Original", img)
cv2.imshow("High-Boost Sharpening", high_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()
