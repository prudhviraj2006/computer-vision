import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('D:\computer vision lab\exp 1.png')  # Replace with your file name or path

# Step 2: Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Display the result
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Grayscale")
plt.imshow(gray_image, cmap='gray')
plt.axis("off")

plt.show()
