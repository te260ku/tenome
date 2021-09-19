import cv2

DEVICE_ID = 1
cap = cv2.VideoCapture(DEVICE_ID)

while True:
    ret, frame = cap.read()
    if not ret:
        print('failed to capture')
        break

    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()