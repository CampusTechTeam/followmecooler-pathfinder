import cv2
import numpy as np
import time

while True:
	frame = np.random.randint(0,255,(500,500,3), np.uint8)
	cv2.namedWindow("FollowMeCooler Pathfinder")
	cv2.imshow("FollowMeCooler Pathfinder", frame)
	key = cv2.waitKey(1) & 0xFF
	time.sleep(0.1)