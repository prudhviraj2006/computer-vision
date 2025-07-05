import cv2
import numpy as np
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)

# Custom Laplacian kernel with negative center
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Laplacian Sharpening", sharpened)
cv2.waitKey(0); cv2.destroyAllWindows()
