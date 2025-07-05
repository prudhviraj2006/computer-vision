import cv2
import numpy as np

img = cv2.imread('D:\computer vision lab\exp 1.png')
src = np.float32([[50,50],[300,50],[50,300],[300,300]])
dst = np.float32([[0,0],[400,0],[0,400],[400,400]])

# DLT via getPerspectiveTransform (OpenCV handles linear system internally)
matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (400, 400))

cv2.imshow("DLT Transform", result)
cv2.waitKey(0); cv2.destroyAllWindows()
