import cv2
import numpy as np

mandms_cascade=cv2.CascadeClassifier('cascade/cascade.xml')

cam=cv2.VideoCapture(0);

while(True):

	ret, frame=cam.read()
	mms=mandms_cascade.detectMultiScale(frame, maxSize=(60,60))
	for[x,y,w,h] in mms:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('frame',frame)

	key=cv2.waitKey(10)
	if key==ord('q'):
		break
	if key==ord('z'):
		cv2.imwrite('zdjecie_8.jpg',frame)
cam.release()
cv2.destroyAllWindows
