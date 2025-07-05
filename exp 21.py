import cv2
import numpy as np

# Step 1: Load image in grayscale
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)  # Replace with your image

# Step 2: Define the Laplacian kernel (with diagonal neighbors)
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Step 3: Apply the kernel
sharpened = cv2.filter2D(img, -1, kernel)

# Step 4: Display results
cv2.imshow("Original", img)
cv2.imshow("Sharpened with Diagonal Laplacian", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
