
import cv2
import numpy as np

img = cv2.imread("img/h2.png")
img [:,:,0] = cv2.add(img[:,:,2],1)
img [:,:,2] = cv2.add(img[:,:,2],1)

img [:,:,0] = cv2.multiply(img[:,:,0],255)
img [:,:,1] = cv2.multiply(img[:,:,1],255)
img [:,:,2] = cv2.multiply(img[:,:,2],255)

cv2.imshow("1",img [:,:,1])

cv2.waitKey(0)
cv2.destroyAllWindows()