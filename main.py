#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:20:56 2019

@author: stefan
"""

from mapSolver.AstarSolver import Astar
from ImageTools.Tools import grayscale, loadImage, maxPoolResize, scaleCoordinates, drawPath, display, resize
import os

start=(319, 169)
end=(4, 154)
	
map=loadImage(os.path.join(os.getcwd(), "map.png"))
gmap=grayscale(map)
nmap,_,_=maxPoolResize(gmap, 2)
nstart=scaleCoordinates(start, 2)
nend=scaleCoordinates(end, 2)
path=Astar(nmap, nstart, nend)
img=drawPath(resize(map, 2), path)
display(img)
