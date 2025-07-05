import cv2

image_path = r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png"
img = cv2.imread(image_path)
template = img[100:300, 100:300]  # Adjust based on known object area
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
_, _, _, max_loc = cv2.minMaxLoc(res)
h, w = template.shape[:2]
cv2.rectangle(img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

cv2.imshow("Template Match", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
