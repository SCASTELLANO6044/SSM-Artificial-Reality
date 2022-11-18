import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./reference/qr.jpg')

# Initiate ORB detector
orb = cv2.ORB_create()

# # find the keypoints with ORB
# kp = orb.detect(img, None)
# # compute the descriptors with ORB
# kp, des = orb.compute(img, kp)

kp_model, des_model = orb.detectAndCompute(img, None)

# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp_model, img, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()
cv2.imshow('keypoints',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()