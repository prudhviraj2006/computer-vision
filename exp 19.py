import cv2
img = cv2.imread('D:\computer vision lab\exp 1.png', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobelxy = cv2.magnitude(sobelx, sobely)

cv2.imshow("Sobel XY", cv2.convertScaleAbs(sobelxy))
cv2.waitKey(0); cv2.destroyAllWindows()
