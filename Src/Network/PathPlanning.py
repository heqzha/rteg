#!/usr/bin/env python
"""
@file				PathPlanning.py
@author			Hequn Zhang
@date				09-04-2013
@version		0.1

Planning the path from origin to destination
"""
import pdb
import random

class PathPlanning:

	def __init__(self, iMap):
		self.mMap = iMap
		self.mOrig = None
		self.mDest = None
	
	def setOrigDest(self, iOrig, iDest):
		self.mOrig = iOrig
		self.mDest = iDest

	def pickRandomOrigDest(self, iOrigDestList):
		orig = None
		dest = None
		odList = iOrigDestList
		while((orig is None)or (dest is None)):	
			randIndex = random.choice(odList)
			random.shuffle(odList)
			if orig is None:
				orig = self.mMap[randIndex[0]][randIndex[1]]
			else:
				randNode = self.mMap[randIndex[0]][randIndex[1]]
				if randNode is not orig:
					dest = randNode
		
		self.mOrig = orig
		self.mDest = dest


	def randomPath(self):
		oPath = []
		#A node has at least one edge
		#Get a edge randomly which is connected with the node
		allEdges = self.mOrig.getAllAdjEdges()
		edgeIndex = random.choice((list(allEdges.keys())))
		node = allEdges[edgeIndex].getTo()
		#Debug code:
		#pdb.set_trace()	

		#Orign Node
		oPath.append(allEdges[edgeIndex])

		while(1 != node.getLenAdjEdges()):
			allEdges = node.getAllAdjEdges()
			edgeIndex = random.choice((list(allEdges.keys())))
			node = allEdges[edgeIndex].getTo()
			oPath.append(allEdges[edgeIndex])

		#Destination Node
		#allEdges = node.getAllAdjEdges()
		#edgeIndex = random.choice((list(allEdges.keys())))
		#oPath.append(allEdges[edgeIndex])
		return oPath

	def shortestPath(self):
		#Dijkstr
		pass
