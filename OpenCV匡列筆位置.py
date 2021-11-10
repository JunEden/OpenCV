import cv2
import numpy as np

p1=cv2.VideoCapture("img/h3.mp4")

while p1.isOpened() == True:
	ret ,m1 = p1.read()
	hsv = cv2.cvtColor(m1, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([100,60,0])
	upper_blue = np.array([124,255,255])
	mask = cv2.inRange(hsv, lower_blue,upper_blue)
	
	a,b = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	# cv2.drawContours(m1,a,-1,(0,0,255),3)
	
	for cnt in a:
		area = cv2.contourArea(cnt)
		print(area)
		if area > 1000:
			peri = cv2.arcLength(cnt, True)
			approx = cv2.approxPolyDP(cnt,0.02 * peri,True)
			x , y,w,h = cv2.boundingRect(approx)
			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),5)


			if ret == True:
				cv2.imshow("m3",m1)
				cv2.waitKey(33)
cv2.destroyAllWindows()
