import cv2
import numpy as np
import time
import sys
from astar_python.astar import Astar
import random


def pathfinder(point,target,obstacles):
	print(point,target)
	area = np.zeros((500,500), np.uint8)
	frame = np.zeros((500,500,3), np.uint8)
	for i in obstacles:
		area[i[0]][i[1]] = 1
		frame[i[1]][i[0]] = (255,255,255)
		#print(i[0],i[1])

	area[point[0]][point[1]]=0
	area[target[0]][target[1]]=0
	
	astar = Astar(area)
	path = astar.run(point,target)
	for i in path:
		frame[i[1]][i[0]] = (0,0,255)
		#print(i)
	cv2.namedWindow("FollowMeCooler Pathfinder")
	cv2.imshow("FollowMeCooler Pathfinder", frame)
	key = cv2.waitKey(1) & 0xFF
	np.set_printoptions(threshold=sys.maxsize)
	#print(frame[frame > 0])
	
	

while True:
	#time.sleep(0.1)
	obstacles = [[random.randint(0,499),random.randint(0,499)],[random.randint(0,499),random.randint(0,499)]]
	for i in range(0,1000): obstacles.append([random.randint(0,499),random.randint(0,499)])
	pathfinder((100,random.randint(0,499)),(400,random.randint(0,499)),obstacles)