import cv2

image = cv2.imread(r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png")

# Crop region
crop = image[50:150, 100:200]  # adjust coordinates as needed

# Paste it elsewhere
image[200:300, 300:400] = crop

cv2.imshow("Cropped and Pasted Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
