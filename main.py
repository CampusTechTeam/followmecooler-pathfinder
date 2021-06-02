import cv2
import numpy as np
import time
import sys


def pathfinder(point,target,obstacles):
	areas = np.zeros((500,500), np.uint8)
	frame = np.zeros((500,500,3), np.uint8)
	for i in obstacles:
		print(i)
		areas[i[0]][i[1]] = 1
		print(frame[i[0]][i[1]])
		frame[i[0]][i[1]] = (255,255,255)
		print(frame[i[0]][i[1]])
	while True:
		cv2.namedWindow("FollowMeCooler Pathfinder")
		cv2.imshow("FollowMeCooler Pathfinder", frame)
		key = cv2.waitKey(1) & 0xFF
		np.set_printoptions(threshold=sys.maxsize)
		print(frame[frame > 0])
		
		time.sleep(1)

pathfinder((250,10),(230,450),((240,30),(235,40)))