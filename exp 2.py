import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image_path = 'D:\computer vision lab\exp 2.png'  # Make sure this is the correct file name and path
image = cv2.imread(image_path)

# Debug check
if image is None:
    print(f"Error: Unable to load image at path '{image_path}'. Please check the file name or location.")
else:
    # Step 2: Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (11, 11), 0)  # (11,11) = kernel size

    # Step 3: Display original and blurred images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Blurred Image (Gaussian Blur)")
    plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.tight_layout()
    plt.show()

