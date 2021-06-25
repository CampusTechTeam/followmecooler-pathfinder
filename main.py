import cv2
import argparse
import numpy as np
import imageio
import time
import random
import sys

import pyastar2d


def pathfinder(point,target,obstacles):
	print(point,target)
	area = np.ones((253,250), np.float32)
	frame = np.zeros((253,253,3), np.uint8)
	for i in obstacles:
		area[i[0]][i[1]] = np.inf
		frame[i[1]][i[0]] = (255,255,255)

		area[i[0]-1][i[1]] = 5
		frame[i[1]][i[0]-1] = (255*0.7,255*0.7,255*0.7)

		area[i[0]][i[1]-1] = 5
		frame[i[1]-1][i[0]] = (255*0.7,255*0.7,255*0.7)

		area[i[0]+1][i[1]] = 5
		frame[i[1]][i[0]+1] = (255*0.7,255*0.7,255*0.7)

		area[i[0]][i[1]+1] = 5
		frame[i[1]+1][i[0]] = (255*0.7,255*0.7,255*0.7)
	
		area[i[0]-2][i[1]] = 5
		frame[i[1]][i[0]-2] = (255*0.7,255*0.7,255*0.7)

		area[i[0]][i[1]-2] = 3
		frame[i[1]-2][i[0]] = (255*0.4,255*0.4,255*0.4)

		area[i[0]+2][i[1]] = 3
		frame[i[1]][i[0]+2] = (255*0.4,255*0.4,255*0.4)

		area[i[0]][i[1]+2] = 3
		frame[i[1]+2][i[0]] = (255*0.4,255*0.4,255*0.4)

		area[i[0]+1][i[1]+1] = 3
		frame[i[1]+1][i[0]+1] = (255*0.4,255*0.4,255*0.4)
		
		area[i[0]-1][i[1]-1] = 3
		frame[i[1]-1][i[0]-1] = (255*0.4,255*0.4,255*0.4)

		area[i[0]-1][i[1]+1] = 3
		frame[i[1]+1][i[0]-1] = (255*0.4,255*0.4,255*0.4)

		area[i[0]+1][i[1]-1] = 3
		frame[i[1]-1][i[0]+1] = (255*0.4,255*0.4,255*0.4)

		


		#print(i[0],i[1])

	area[point[0]][point[1]]=1
	area[target[0]][target[1]]=1
	path = pyastar2d.astar_path(area, point, target, allow_diagonal=False)
	for i in path:
		frame[i[1]][i[0]] = (3,3,255)
		#print(i)
	cv2.namedWindow("FollowMeCooler Pathfinder", flags=cv2.WINDOW_GUI_EXPANDED)
	cv2.imshow("FollowMeCooler Pathfinder", frame)
	key = cv2.waitKey(1) & 0xFF
	np.set_printoptions(threshold=sys.maxsize)
	#print(frame[frame > 0])
	
	

while True:
	obstacles = [[random.randint(15,240),random.randint(15,240)],[random.randint(15,240),random.randint(15,240)]]
	for i in range(3,300): obstacles.append([random.randint(15,240),random.randint(15,240)])
	
	pathfinder((103,random.randint(15,240)),(203,random.randint(15,240)),obstacles)
	time.sleep(3)
	