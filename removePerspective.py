import numpy as np
import cv2

# top left, top right, bottom left, bottom right
pts = [(0,0),(0,0),(0,0),(0,0)]
pointIndex = 0
cam = cv2.VideoCapture(1)
_,img = cam.read()
ASPECT_RATIO = (420,480)#h,w
#ASPECT_RATIO = (500*(150/130),500)
pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])


def draw_circle(event,x,y,flags,param):
	global img
	global pointIndex
	global pts
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(img,(x,y),0,(255,0,0),-1)
		pts[pointIndex] = (x,y)
		pointIndex = pointIndex + 1

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

def selectFourPoints():
	global img
	global pointIndex
	print "Please select 4 points, by double clicking on each of them in the order: \n\
	top left, top right, bottom left, bottom right."
	while(pointIndex != 4):
		cv2.imshow('image',img)
		key = cv2.waitKey(20) & 0xFF
		if key == 27:
			return False
	return True


while(1):
	if(selectFourPoints()):
		pts1 = np.float32([\
			[pts[0][0],pts[0][1]],\
			[pts[1][0],pts[1][1]],\
			[pts[2][0],pts[2][1]],\
			[pts[3][0],pts[3][1]] ])

		M = cv2.getPerspectiveTransform(pts1,pts2)

		while(1):

			_,frame = cam.read()
			if frame!=None:

				dst = cv2.warpPerspective(frame,M,(ASPECT_RATIO[1],ASPECT_RATIO[0]))

				cv2.imshow("output",dst)

				if cv2.waitKey(1) & 0xFF == ord('q'):
					cv2.imwrite("output.jpg", dst)
					break
		else:
			print "Exit"

		break

cam.release()
cv2.destroyAllWindows()