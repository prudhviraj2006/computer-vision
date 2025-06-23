import cv2

cap = cv2.VideoCapture(0)
mode = 'normal'

print("Press: n = Normal | s = Slow | f = Fast | q = Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('n'): mode = 'normal'
    elif key == ord('s'): mode = 'slow'
    elif key == ord('f'): mode = 'fast'
    elif key == ord('q'): break

    if mode == 'normal':
        cv2.waitKey(30)
    elif mode == 'slow':
        cv2.waitKey(100)
    elif mode == 'fast':
        cap.read()  # skip frame
        cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()
