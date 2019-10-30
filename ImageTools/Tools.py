#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:58:44 2019

@author: stefan
"""

import cv2 
import numpy as np 

def loadImage(path):
    return cv2.imread(path, 1)

def distFunction(point1, point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def maxPoolResize(image, factor):
    
    newrows=image.shape[1]//factor
    newcols=image.shape[0]//factor
    newim=np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for x in np.arange(0, image.shape[0]-factor, factor):
        for y in np.arange(0, image.shape[1]-factor, factor):
            whitePixCounter=0
            for x1 in np.arange(0, factor):
                for y1 in np.arange(0, factor):
                    if image[x+x1][y+y1]>0:
                        whitePixCounter+=1
            if whitePixCounter==factor**2:
                newim[x//factor][y//factor]=255
            else:
                newim[x//factor][y//factor]=0
	
    return newim, newrows, newcols
                        
def scaleCoordinates(coordinates, factor):
	return (coordinates[0]//factor, coordinates[1]//factor)                 

def binarize(image, factor):
    return image>factor


def grayscale(image):
	return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def drawPath(image, path):
	for x, y in path:
		image[x][y]=(0, 0, 255)
	return image

def display(image):
	cv2.imshow("image", image)
	cv2.waitKey(0)                    
                    
def resize(image, scale):
	return cv2.resize(image, (image.shape[1]//scale, image.shape[0]//scale))           

def distPoint2Line(P1, P2, P3):
	return np.abs((P2[1]-P1[1])*P3[0]-(P2[0]-P1[0])*P3[1]+P2[0]*P1[1]-P2[1]*P1[0])/np.sqrt((P2[1]-P1[1])**2+(P2[0]-P1[0])**2)
	
def moveCommands(path):
		
		
		p1=np.array(path[0])
		p2=np.array(path[1])
		
		cnt=0
		pathlist=[]
		
			
		for ind, elem in enumerate(path):
			if distPoint2Line(p1, p2, elem)<2:
				cnt+=1
			else:
				pathlist.append((tuple(p1), tuple(elem), cnt, np.arctan2(p1[1]-elem[1], p1[0]-elem[0])*180/np.pi))
				p1=np.array(elem)
				
				cnt=0
				if ind!=len(path)-1:
					p2=np.array(path[ind+1])
				
				else:
					continue
		if cnt>0:
			pathlist.append((tuple(p1), tuple(elem), cnt, np.arctan2(p1[1]-elem[1], p1[0]-elem[0])*180/np.pi))
		return pathlist

def checkObjects(map, p1, p2):
	poly=np.poly1d(np.polyfit([p1[1], p2[1]], [p1[0], p2[0]], 1))
	for x in range(p1[1], p2[1]):
		if map[x][int(np.round(poly(x)))]<250:
			return False
	return True

def distance(d1, d2, angle):
	return np.sqrt(d1**2+d2**2-2*d1*d2*np.cos(angle))
	
def shortPath(path, map):
	newpath=[]
	change=False
	for i in range(0 , len(path)-1):
		if checkObjects(map, path[i][0], path[i+1][1]):
			print("yes")
			print (i)
			print (path[i][0])
			print(path[i+1][1])
			newpath.append((path[i][0], path[i+1][1], distance(path[i][2], path[i+1][2], path[i+1][3]), np.arctan2(path[i][0][0]-path[i+1][1][0], path[i][0][1]-path[i+1][1][1])*180/np.pi))
			change=True
		else:
			print("no")
			newpath.append(path[i])
	
	return change, newpath
		
	
def shortenPath(path, map):
	newpath=path
	for x in range(0 , len(path)):
		data=shortPath(newpath, map)
		if data[0]:
			newpath=data[1]
		else:
			return newpath
			
	
	
	
