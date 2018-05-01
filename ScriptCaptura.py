import numpy as np
import cv2 as cv

#from picamera import PiCamera
#from picamera.array import PiRGBArray
import time


camera =cap.VideoCaputre(0)
camera.resolution= (640, 480)

camera.framerate = 32
#rawCapture = PiRGBArray(camera, size =(640,480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format ="bgr", use_video_port=True):
    image = frame.array
    cv.imshow("Frame",image)
    
    rawCapture.truncate(0)
    

    if cv.waitKey(1) & 0xFF == ord ('q'):
       
        cv.destroyAllWindows()
        break
