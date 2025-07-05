import cv2

video_path = r"C:\Users\lekka\OneDrive\Videos\sample_video.mp4"  # Replace this with your actual video file
cap = cv2.VideoCapture(video_path)
frames = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

for frame in reversed(frames):
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
