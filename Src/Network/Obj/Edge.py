#!/usr/bin/env python
"""
@file			Edge.py
@author		Hequn Zhang
@date			25-03-2013
@version	0.1

Definition of edges
"""
from EdgeType import EdgeType

class Edge:
#	EDGE_TYPE_ROAD_URBAN = "road.urban"
#	EDGE_TYPE_ROAD_RURAL = "road.rural"
#	EDGE_TYPE_SECONDARY_URBAN = "secondary.urban"
#	EDGE_TYPE_SECONDARY_RURAL = "secondary.rural"
	LANE_DEFAULT_WIDTH = 3.25

	MAP_EDGE_TYPE = {
	"road.urban":EdgeType("road.urban", LANE_DEFAULT_WIDTH, 2, 7, 13.889),
	"road.rural":EdgeType("road.rural", LANE_DEFAULT_WIDTH, 1, 7, 27.778),
	"secondary.urban":EdgeType("secondary.urban", LANE_DEFAULT_WIDTH, 2, 10, 13.889),
	"secondary.rural":EdgeType("secondary.rural", LANE_DEFAULT_WIDTH,1, 10, 27.778)
	}
	
	def __init__(self, iId, iFrom, iTo, iEdgeType, iLength = None, iShape = None, iSpreadType = None):
		self.mId = iId
		self.mFrom = iFrom
		self.mTo = iTo
		self.setEdgeType(iEdgeType)
		self.mLength = iLength
		self.mShape = iShape
		self.mSpreadType = iSpreadType

	def getId(self):
		return self.mId

	def getFrom(self):
		return self.mFrom

	def getTo(self):
		return self.mTo

	def getEdgeType(self):
		return self.mEdgeType

	def getLength(self):
		return self.mLength

	def getShape(self):
		return self.mShape

	def getSpreadType(self):
		return self.mSpreadType

	def setEdgeType(self, iEdgeType):
		if Edge.MAP_EDGE_TYPE.has_key(iEdgeType):
			self.mEdgeType = Edge.MAP_EDGE_TYPE.get(iEdgeType)
		else:
			self.mEdgeType = Edge.MAP_EDGE_TYPE.get("road.urban")	

