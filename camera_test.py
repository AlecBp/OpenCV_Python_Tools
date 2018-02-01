import cv2
import numpy as np
# initialize the camera
try:
    cam = cv2.VideoCapture(1)
except:
    print "ERROR"
    exit()

while (True):
    ret, frame = cam.read()
    if frame != None:
        #equ = cv2.equalizeHist(frame)
        cv2.imshow('VideoStream', frame)

        #cv2.imshow('Equ', equ)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()