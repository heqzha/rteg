#!/usr/bin/env python
"""
@file		PolyShape.py
@author		Hequn Zhang
@date		30-04-2013
@version	0.1

Definition of polygon shapes
"""

class PolyPoint:
	def __init__(self, iX, iY):
		self.mX = iX
		self.mY = iY

class PolyShape:
	def __init__(self, iVertex = 3, iRadius = 10):
		if iVertex < 3:
			self.mVertex = 3
		else:
			self.mVertex = iVertex

		if iRadius < 10:
			self.mRadius = 10
		else:
			self.mRadius = iRadius
		
		self.mPoints = []
	
	def getPoints(self):
		return self.mPoints

	def getVertex(self):
		return self.mVertex

	def getRadius(self):
		return self.mRadius
