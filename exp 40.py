import cv2

image_path = r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png"
img = cv2.imread(image_path)
x, y, w, h = 200, 100, 200, 200
roi = img[y:y+h, x:x+w]

cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Image with Rectangle", img)
cv2.imshow("Extracted Object", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
