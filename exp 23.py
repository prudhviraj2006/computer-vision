import cv2
import numpy as np

# Step 1: Read the image (grayscale for simplicity)
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)  # Replace with your image

# Step 2: Blur the image
blurred = cv2.GaussianBlur(img, (9, 9), 10)

# Step 3: Create the mask
mask = cv2.subtract(img, blurred)

# Step 4: Add the mask to the original image (sharpening)
unsharp = cv2.add(img, mask)

# Step 5: Show the images
cv2.imshow("Original", img)
cv2.imshow("Unsharp Mask", unsharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
