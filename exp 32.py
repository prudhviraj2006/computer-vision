import cv2
import numpy as np

img = cv2.imread(r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png", 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Closing Operation", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
