#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:55:05 2019

@author: stefan
"""

class Node:
    def __init__ (self, position=None, parent=None):
        self.position=position
        self.parent=parent
        self.gcost=0
        self.hcost=0
        self.fcost=0
        
    def __lt__(self, other):
        return self.fcost<other.fcost