#!/usr/bin/env python
"""
@file			GridNetwork.py
@author		Hequn Zhang
@date			26-03-2013
@version	0.1

Definition of grid network
"""
from __future__ import division
import pdb
import random
import math
from Obj.Node import Node
from Obj.Edge import Edge
from Obj.EdgeType import EdgeType
from Obj.Vehicle import Vehicle
from Obj.Route import Route
from PathPlanning import PathPlanning
from PolyObj.PolyGen import PolyGen
from PolyObj.Poly import Poly

class Coord2D:
	def __init__(self, iX, iY):
		self.mX = iX
		self.mY = iY

class GridNetwork:
	EDGE_TYPE_ROAD_URBAN = "road.urban"
	EDGE_TYPE_ROAD_RURAL = "road.rural"
	EDGE_TYPE_SECONDARY_URBAN = "secondary.urban"
	EDGE_TYPE_SECONDARY_RURAL = "secondary.rural"

	def __init__(self, iRow = 1, iCol = 1, iLength = 100.0):
		self.mRow = iRow + 2
		self.mCol = iCol + 2
		self.mLength = iLength
		self.mNodesArray = [[None for row in range(self.mCol)] for col in range(self.mRow)]
		self.mNodesOrigDestList = []
		self.mRouteList = []
		self.mVehicleList = []
		self.mPolyList = []
		self.mCenter = Coord2D((self.mCol - 1) / 2, (self.mRow - 1) / 2)
		
	def genGridNodes(self):
		#Debug code:
		#pdb.set_trace()
		centerRow = (self.mRow - 1) / 2
		centerCol = (self.mCol - 1) / 2
		#Set Junction and Origin/Destination Nodes
		for i in range(0,self.mRow):
			for j in range(0,self.mCol):
				nId 	= "nod_%i_%i" %(i,j)
				nX = (j - centerCol) * self.mLength
				nY = (centerRow - i) * self.mLength
				if (i == 0) or (i == self.mRow - 1):
					if (j > 0) and (j < self.mCol - 1):
						#Origin/Destination Nodes
						nType = Node.NODE_TYPE_PRIORITY
						self.mNodesArray[i][j] = Node(nId, nX, nY, nType)
						self.mNodesOrigDestList.append([i,j])
				else:
					if (j > 0) and (j < self.mCol - 1):
						#Junction Nodes
						nType = Node.NODE_TYPE_TRAFFIC_LIGHT
						self.mNodesArray[i][j] = Node(nId, nX, nY, nType)
					else:
						#Origin/Destination Nodes
						nType = Node.NODE_TYPE_PRIORITY
						self.mNodesArray[i][j] = Node(nId, nX, nY, nType)
						self.mNodesOrigDestList.append([i,j])

		return self.mNodesArray

	def genGridAdjArea(self,iEdgeType):
		for i in range(0, self.mRow):
			for j in range(0, self.mCol):
				node = self.mNodesArray[i][j]
				if node is not None:
					#Debug code:
					#pdb.set_trace()

					if i == 0:
						#North Origin/Destination Node
						adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_SOUTH)
						toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
						edge = Edge("edg_%i_%i_S" %(i, j), node, toNode,iEdgeType) 
						node.setAdjEdge(Node.ADJ_EDGES_SOUTH,edge)

					elif i == (self.mRow - 1):
						#South Origin/Destination Nodes
						adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_NORTH)
						toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
						edge = Edge("edg_%i_%i_N" %(i, j), node, toNode,iEdgeType)
						node.setAdjEdge(Node.ADJ_EDGES_NORTH,edge)

					else:
						if j == 0:
							#West Origin/Destination Nodes
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_EAST)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_E" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_EAST,edge)

						elif j == (self.mCol - 1):
							#East Origin/Destination Nodes
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_WEST)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_W" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_WEST,edge)

						else:
							#Junction Nodes
							#North Adjacent Node
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_NORTH)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_N" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_NORTH,edge)

							#South Adjacent Node
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_SOUTH)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_S" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_SOUTH,edge)

							#West Adjacent Node
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_WEST)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_W" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_WEST,edge)

							#East Adjacent Node
							adjNodeIndex = node.getAdjNodeIndex(i,j,Node.ADJ_EDGES_EAST)
							toNode = self.mNodesArray[adjNodeIndex[0]][adjNodeIndex[1]]
							edge = Edge("edg_%i_%i_E" %(i, j), node, toNode,iEdgeType)
							node.setAdjEdge(Node.ADJ_EDGES_EAST,edge)

	def genRoutes(self, iNumRoutes):
		path = PathPlanning(self.mNodesArray)
		for i in range(iNumRoutes):	
			#Get Random orig and destination
			path.pickRandomOrigDest(self.mNodesOrigDestList)
			#Generate Random Route
			randEdges = path.randomPath()
			route = Route("rou_%i" %(i), randEdges)
			self.mRouteList.append(route)


	def genVehicles(self, iNumVehicles):
		path = PathPlanning(self.mNodesArray)
		vTypeList = list(Vehicle.MAP_VEHICLE_TYPE.keys())
		for i in range(iNumVehicles):
			#Generate Random Vehicle Type
			randType = random.choice(vTypeList)
			random.shuffle(vTypeList)
			randRoute = random.choice(self.mRouteList)
			randRouteId  = randRoute.getId()
			self.mVehicleList.append(Vehicle("veh_%i" %(i),randType, randRouteId, i))
	
	def getSpaceCenter(self, offsetY = None):
		spaceCenter = []
		for r in range(0, self.mRow - 1):
			for c in range(0, self.mCol - 1):
				x = c + 0.5
				if offsetY is None:
					y = r + 0.5
				else:
					y = offsetY - (r + 0.5)
				#print "x:%f y:%f" %(x,y)
				center = Coord2D(x * self.mLength, y * self.mLength)
				#print "len x:%f len y:%f" %(center.mX,center.mY)
				spaceCenter.append(center)
		return spaceCenter

	def genPloys(self, iVertex, iRadius):
		#Debug code:
		#pdb.set_trace()

		spaceCenter = self.getSpaceCenter(self.mRow - 1)
		polyShape = PolyGen()
		allPolyShape = polyShape.genAllPoly(spaceCenter, iVertex, iRadius)
		for i in range(0, len(allPolyShape)):
			pId = "poly_%d" %(i)
			color = Poly.POLY_COLOR_RED
			shapes = allPolyShape[i].getPoints()
			self.mPolyList.append(Poly(pId, color, shapes))

#####################################################################################################################
	def getSubSpaceCenter(self, row, col, spaceCenter, length):
		subSpaceCenter = []
		for r in range(0, row):
			y = 1.0/2.0 - (1.0/col) * r - 1.0/(2.0*col)
			for c in range(0, col):
				x = -(1.0/2.0) + (1.0/row) * c + 1.0/(2.0*row)
				subCenter = Coord2D(x*length + spaceCenter.mX, y*length + spaceCenter.mY)
				subSpaceCenter.append(subCenter)
		return subSpaceCenter

	def genPloy(self, iVertex, interval):
		radius = math.sqrt(2)*(self.mLength - interval * 2.0) / 2.0
		
		spaceCenter = self.getSpaceCenter(self.mRow - 1)
		polyShape = PolyGen()
		allPolyShape = polyShape.genAllPoly(spaceCenter, iVertex, radius)
		for i in range(0, len(allPolyShape)):
			pId = "poly_%d" %(i)
			color = Poly.POLY_COLOR_RED
			shapes = allPolyShape[i].getPoints()
			self.mPolyList.append(Poly(pId, color, shapes))

	def genPolyGroup(self, iVertex, numPoly, interval):
		if(numPoly == 0):
			return
		spaceCenter = self.getSpaceCenter(self.mRow - 1)
		polyShape = PolyGen()
		#radius = ((math.sqrt(2)*self.mLength) / numPoly) / interval
		radius = math.sqrt(2)*((self.mLength / numPoly) - interval * 2.0) / 2.0
		for sc in spaceCenter:	
			subSc = self.getSubSpaceCenter(numPoly, numPoly, sc, self.mLength)
			subPolys = polyShape.genAllPoly(subSc, iVertex, radius)
		
		for i in range(0, len(subPolys)):
			pId = "poly_%d" %(i)
			color = Poly.POLY_COLOR_RED
			shapes = subPolys[i].getPoints()
			self.mPolyList.append(Poly(pId, color, shapes))

#####################################################################################################################

	def getNodesArray(self):
		return self.mNodesArray

	def getVehicleList(self):
		return self.mVehicleList

	def getPolyList(self):
		return self.mPolyList

	def getEdgeType(self):
		return Edge.MAP_EDGE_TYPE

	def getVehicleType(self):
		return Vehicle.MAP_VEHICLE_TYPE

	def getRouteList(self):
		return self.mRouteList
