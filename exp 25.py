import cv2
import numpy as np

image = cv2.imread(r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
gradient = cv2.magnitude(sobel_x, sobel_y)
gradient = cv2.convertScaleAbs(gradient)

cv2.imshow("Gradient Edge Sharpening", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
