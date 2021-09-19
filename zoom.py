import cv2

def nothing(x):
    pass

def main(mirror=False):
    cv2.namedWindow('window')
    cv2.createTrackbar('scale', 'window', 50, 50, nothing)

    cap = cv2.VideoCapture(1)

    while True:
        scale = cv2.getTrackbarPos('scale', 'window')

        _, frame = cap.read()

        if mirror: 
            frame = cv2.flip(frame, 1)

        height, width, channels = frame.shape

        cx, cy = int(height/2), int(width/2)
        rx, ry = int(scale*height/100), int(scale*width/100)

        min_x,max_x = cx-rx, cx+rx
        min_y,max_y = cy-ry, cy+ry

        cropped = frame[min_x:max_x, min_y:max_y]
        resized = cv2.resize(cropped, (width, height)) 

        cv2.imshow('window', resized)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k == 49:
            scale += 5
        elif k == 50:
            scale -= 5

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()