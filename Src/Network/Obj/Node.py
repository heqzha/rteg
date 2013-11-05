#!/usr/bin/env python
"""
@file				Node.py
@author			Hequn Zhang
@date				25-03-2013
@version		0.1

Definition of traffic Node
"""
import pdb

class Node:
	NODE_TYPE_PRIORITY			= "priority"
	NODE_TYPE_TRAFFIC_LIGHT = "traffic_light"
	NODE_TYPE_RIGHT_BEFORE_LEFT = "right_before_left"
	NODE_TYPE_UNREGULATED = "unregulated"

	ADJ_EDGES_NORTH = 0
	ADJ_EDGES_SOUTH = 1
	ADJ_EDGES_WEST  = 2
	ADJ_EDGES_EAST  = 3

	def __init__(self, iId, iX, iY, iType):
		self.mId		= iId
		self.mX 		= iX
		self.mY			= iY
		self.mType	= iType
		self.mAdjEdges = {}

	def getId(self):
		return self.mId

	def getX(self):
		return self.mX

	def getY(self):
		return self.mY

	def getType(self):
		return self.mType
	
	def getAllAdjEdges(self):
		return self.mAdjEdges

	def getAdjEdges(self, iDirect):
		if self.mAdjEdges.has_key(iDirect):
			return self.mAdjEdges.get(iDirect)
		else:
			return None
	
	def getLenAdjEdges(self):
		return len(self.mAdjEdges)

	def setAdjEdge(self, iDirect,iAdjEdge):
		edge = {iDirect: iAdjEdge}
		self.mAdjEdges.update(edge)

	def getAdjNodeIndex(self, iRow, iCol, iDirct):
		#Debug code:
		#pdb.set_trace()

		if iDirct == Node.ADJ_EDGES_NORTH:
			#North
			return [iRow - 1, iCol]
		elif iDirct == Node.ADJ_EDGES_SOUTH:
			#South
			return [iRow + 1, iCol]
		elif iDirct == Node.ADJ_EDGES_WEST:
			#West
			return [iRow, iCol - 1]
		elif iDirct == Node.ADJ_EDGES_EAST:
			#East
			return [iRow, iCol + 1]


