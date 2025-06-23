import cv2
import numpy as np

# Open video (0 = webcam or replace with 'your_video.mp4')
cap = cv2.VideoCapture(0)

# Define source and destination points
src_pts = np.float32([[100, 100], [500, 100], [100, 400], [500, 400]])
dst_pts = np.float32([[0, 0], [400, 0], [0, 300], [400, 300]])

# Get perspective transform matrix
matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transformation
    transformed = cv2.warpPerspective(frame, matrix, (400, 300))

    # Show original and transformed video
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
