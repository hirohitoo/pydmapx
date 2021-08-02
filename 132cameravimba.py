#opencv_acquire_streaming_images

import cv2
import time
import matplotlib.pyplot as plt

from typing import Optional
from time import sleep
#pymba
from pymba import Vimba
from pymba import Frame

#from examples.camera._display_frame import display_frame

def display_frame(frame: Frame, delay: Optional[int] = 1) -> None:
    """
    Displays the acquired frame.
    :param frame: The frame object to display.
    :param delay: Display delay in milliseconds, use 0 for indefinite.
    """
    #print('frame {}'.format(frame.data.frameID))

    # get a copy of the frame data
    image = frame.buffer_data_numpy()
    
    large = cv2.resize(image, (0,0), fx=3, fy=3)
    cropped = large[350:545,500:700]  # Crop from {x, y, w, h } => [y:y+dy,x:x+dx]

    # convert colour space if desired
    #try:
        #image = cv2.cvtColor(image, PIXEL_FORMATS_CONVERSIONS[frame.pixel_format])
    #except KeyError:
    #    pass
    # Draw a rectangle
    cv2.rectangle(image,     # source image
              (185, 135),          # upper left corner vertex
              (210, 160),         # lower right corner vertex
              (0, 255, 0),        # color
              thickness=1,        # line thickness
              lineType=cv2.LINE_8  # line type
    )
    cv2.imshow('Si3N4 window', image)
    cv2.imshow('Cropped window', cropped)

    cv2.waitKey(delay)

if __name__ == '__main__':

    with Vimba() as vimba:
        camera = vimba.camera(0)
        camera.open()

        camera.arm('Continuous', display_frame)
        camera.start_frame_acquisition()

        loop_forever = True
        while loop_forever:
               try:
                  time.sleep(60)
               except KeyboardInterrupt:
                  loop_forever = False

        camera.stop_frame_acquisition()
        camera.disarm()

        camera.close()