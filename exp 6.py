import cv2

# Load the video
video = cv2.VideoCapture('D:\computer vision lab\exp 6.mp4')  # Replace with your filename

# Function to play video at custom speed
def play_video(speed_label, delay):
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow(speed_label, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# Normal speed
play_video("Normal Speed", delay=30)

# Slow motion (higher delay)
play_video("Slow Motion", delay=100)

# Fast motion (lower delay, skip frames)
video = cv2.VideoCapture('car_video.mp4')
cv2.namedWindow("Fast Motion")
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imshow("Fast Motion", frame)
    video.set(cv2.CAP_PROP_POS_FRAMES, video.get(cv2.CAP_PROP_POS_FRAMES) + 1)  # Skip frame
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
