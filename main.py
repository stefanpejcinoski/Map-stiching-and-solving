#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:20:56 2019

@author: stefan
"""
from matplotlib import pyplot as plt 
from mapSolver.AstarSolver import Astar
from ImageTools.Tools import shortenPath,shortPath,paralelizedMaxPoolResize,  grayscale, loadImage, maxPoolResize, scaleCoordinates, drawPath, display, resize, moveCommands
import os
import numpy as np
import cv2

if __name__ == '__main__':
    start=(1304, 32)
    end=(510, 1043)
    
    
    map=loadImage(os.path.join(os.getcwd(), "mapa.png"))
    gmap=grayscale(map)
    nmap,_,_=paralelizedMaxPoolResize(gmap, 10)
    print("done")
    plt.imshow(nmap, cmap="gray")
    plt.show()
    nstart=scaleCoordinates(start, 10)
    nend=scaleCoordinates(end, 10)
    path=Astar(nmap, nstart, nend)
    img=drawPath(resize(map, 10), path)
    #display(img)
    move=moveCommands(path)
    print (move)
     
    for el in move:
        	cv2.line(map, (el[0][1]*10, el[0][0]*10), (el[1][1]*10, el[1][0]*10), (0, 0, 255),  thickness=2)
    plt.imshow(map)
    plt.show()
    move = shortPath(move, nmap)[1]
    print("done")
    print (move)
    map=loadImage(os.path.join(os.getcwd(), "mapa.png"))
    for el in move:
        	cv2.line(map, (el[0][1]*10, el[0][0]*10), (el[1][1]*10, el[1][0]*10), (0, 0, 255),  thickness=2)
        
    plt.imshow(map)
    plt.show()
