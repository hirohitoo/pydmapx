#opencv_acquire_streaming_images

import cv2
import time

vid = cv2.VideoCapture(0)

while True:

    ret, frame = vid.read()

    cv2.imshow('Controlling my computer camera', frame)
    time.sleep(1)
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()