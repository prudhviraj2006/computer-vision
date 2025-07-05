import cv2

image = cv2.imread(r"C:\Users\lekka\OneDrive\Pictures\lake-with-radha-and-krishna-desktop-tyhs0z5a2zbs2vvk (1).png")

# Add watermark text
watermarked = image.copy()
cv2.putText(watermarked, "© Lekkala", (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
            1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("Watermarked Image", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
