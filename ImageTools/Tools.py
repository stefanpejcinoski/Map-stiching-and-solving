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


def maxPoolResize(image, factor):
    
    newrows=image.shape[1]//factor
    newcols=image.shape[0]//factor
    newim=np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for x in np.arange(0, image.shape[0], factor):
        for y in np.arange(0, image.shape[1], factor):
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
	return (coordinates[0]//2, coordinates[1]//2)                 

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
