#!/usr/bin/env python
"""
@file				Route.py
@author			Hequn Zhang
@date				08-04-2013
@version		0.1

Definition of route
"""

class Route:
	
	def __init__(self, iId, iEdges, iColor = None):
		self.mId = iId
		self.mEdges = iEdges
		self.mColor = iColor

	def getId(self):
		return self.mId

	def getEdges(self):
		return self.mEdges

	def getColor(self):
		return self.mColor
	
	

		
	
