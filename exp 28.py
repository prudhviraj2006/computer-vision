import cv2
import numpy as np

img = cv2.imread(r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png", 0)
kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
boundary = cv2.filter2D(img, -1, kernel)

cv2.imshow("Boundary Detection", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
