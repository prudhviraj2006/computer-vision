import cv2

img = cv2.imread('D:\computer vision lab\exp 1.png', 0)  # Check file name/path

if img is not None:
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    cv2.imshow("Sobel X", cv2.convertScaleAbs(sobelx))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
