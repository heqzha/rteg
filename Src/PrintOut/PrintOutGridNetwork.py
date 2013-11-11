#!/usr/bin/env python
"""
@file			PrintOutGridNetwork.py
@author		Hequn Zhang
@date			10-04-2013
@version	v0.1

Print out xml files which include .nod.xml .edg.xml .typ.xml .rou.xml poly.xml
"""
import os, sys
import pdb
from PrintOutFile import PrintOutFile

class PrintOutGridNetwork:	
	PATH_CURRENT = os.getcwd()
	PATH_RES = PATH_CURRENT + "/Data/"
	TAG_NODES			= "nodes"
	TAG_NODE			=	"node"
	TAG_EDGES			=	"edges"
	TAG_EDGE			=	"edge"
	TAG_ROUTES		=	"routes"
	TAG_VTYPE			=	"vType"	#vehicle type
	TAG_ROUTE			=	"route"
	TAG_VEHICLE		=	"vehicle"
	TAG_CONNECTIONS	=	"connections"
	TAG_CONNECTION	=	"connection"
	TAG_ELDETECTOR	=	"elDetector"
	TAG_TYPES				=	"types"
	TAG_TYPE				=	"type"
	TAG_SHAPES				=	"shapes"
	TAG_POLY				=	"poly"

	FILE_TYPE_NOD = "nod"
	FILE_TYPE_EDG = "edg"
	FILE_TYPE_ROU = "rou"
	FILE_TYPE_CON = "con"
	FILE_TYPE_DET = "det"
	FILE_TYPE_TYP = "typ"
	FILE_TYPE_POLY = "poly"

	FILE_SUFFIX_XML = "xml"
	FILE_SUFFIX_NETCCFG = "netccfg"
	FILE_SUFFIX_SUMOCFG = "sumocfg"

	XML_HEAD = """<?xml version="1.0" encoding="UTF-8"?>
	<%s xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="Data/%s/%s.%s.xml">
	"""
	XML_END = "</%s>"

	def __init__(self, iNetwork,iType, iSuffix, iTag):
		#Debug Code
		#pdb.set_trace()	
		self.mNetwork = iNetwork
		self.mType = iType
		self.mSuffix = iSuffix
		self.mPrintOutHandle = PrintOutFile(PrintOutGridNetwork.PATH_RES,iNetwork, iType, iSuffix)
		self.mXmlHead = PrintOutGridNetwork.XML_HEAD % (iTag, iNetwork, iNetwork, iType)
		self.mXmlEnd = PrintOutGridNetwork.XML_END % (iTag)

	def printOutNodXml(self, iNodeList):
		self.mPrintOutHandle.printOut(self.mXmlHead)
		for nodeListRow in iNodeList:
			for n in nodeListRow:
				if n is not None:
					if(n.getId() is not None and n.getX() is not None and n.getY() is not None and n.getType is not None):
						outStr = '		<%s id="%s" x="%f" y="%f" type="%s"		/>' %(PrintOutGridNetwork.TAG_NODE, n.getId(), n.getX(), n.getY(), n.getType())
						self.mPrintOutHandle.printOut(outStr)
		self.mPrintOutHandle.printOut(self.mXmlEnd)
		self.mPrintOutHandle.printOutEnd()
	
	def printOutEdgXml(self, iNodeList):
		self.mPrintOutHandle.printOut(self.mXmlHead)
		for nodeListRow in iNodeList:
			for n in nodeListRow:
				if n is not None:
					adjEdges = n.getAllAdjEdges()
					for i in adjEdges:
						edge = adjEdges.get(i)
						outStr = None
						if(edge.getId() is not None and edge.getFrom() is not None and edge.getTo() is not None):
							outStr = "		<%s" %(PrintOutGridNetwork.TAG_EDGE)
							outStr += ' id="%s"' %(edge.getId())
							outStr += ' from="%s"' %(edge.getFrom().getId())
							outStr += ' to="%s"' %(edge.getTo().getId())
							if(edge.getEdgeType() is not None):
								outStr += ' type="%s"' %(edge.getEdgeType().getId())
						
						if(outStr is not None):
							outStr += "		/>"
							self.mPrintOutHandle.printOut(outStr)					
		self.mPrintOutHandle.printOut(self.mXmlEnd)
		self.mPrintOutHandle.printOutEnd()
	
	def printOutTypXml(self, iEdgeTypeList):
		self.mPrintOutHandle.printOut(self.mXmlHead)
		for i in iEdgeTypeList:
			edgeType = iEdgeTypeList.get(i)
			outStr = None
			if (edgeType.getId() is not None and edgeType.getNumLanes() is not None and edgeType.getPriority() is not None and edgeType.getSpeed() is not None):
				outStr = '		<%s id="%s" numLanes="%i" width="%f" priority="%i" speed="%f"' %(PrintOutGridNetwork.TAG_TYPE, edgeType.getId(), edgeType.getWidth(), edgeType.getNumLanes(), edgeType.getPriority(), edgeType.getSpeed())
				if (edgeType.getAllow() is not None):
					outStr += ' allow="%s"' %(edgeType.getAllow())
				
				if (edgeType.getDisallow() is not None):
					outStr += ' disallow="%s"' %(edgeType.getDisallow())

				if (edgeType.getDiscard() is not None):
					outStr += ' discard="%s"' %(edgeType.getDiscard())

				if (edgeType.getOneway() is not None):
					outStr += ' oneway="%s"' %(edgeType.getOneway())

				outStr += "		/>"
				self.mPrintOutHandle.printOut(outStr)

		self.mPrintOutHandle.printOut(self.mXmlEnd)
		self.mPrintOutHandle.printOutEnd()

	def printOutRouXml(self,iVehicleList, iVehicleType, iRouteList):
		self.mPrintOutHandle.printOut(self.mXmlHead)
		#Vehicle Type (with car-following model)
		for i in iVehicleType:
			vType = iVehicleType.get(i)
			if (vType.getId() is not None):
				outStr = '		<%s' %(PrintOutGridNetwork.TAG_VTYPE)
				outStr += ' id = "%s"' %(vType.getId())
				if(vType.getCarFollow() is not None):
					if(vType.getColor() is not None and vType.getLength() is not None and vType.getMaxSpeed() is not None and vType.getGuiShape() is not None):
						outStr += ' color = "%s"'			%(vType.getColor())
						outStr += ' length = "%f"'		%(vType.getLength())
						outStr += ' maxSpeed = "%f"'	%(vType.getMaxSpeed())
						outStr += ' guiShape = "%s"'	%(vType.getGuiShape())
					outStr += "		>"
					self.mPrintOutHandle.printOut(outStr)

					carFollow = vType.getCarFollow()
					outStr = '				<%s' %(carFollow.getId())
					#car-following models
					if (carFollow.getAccel() is not None and carFollow.getDecel() is not None and carFollow.getMinGap is not None):
						outStr += ' accel = "%f"' %(carFollow.getAccel())
						outStr += ' decel = "%f"' %(carFollow.getDecel())
						outStr += ' minGap = "%f"' %(carFollow.getMinGap())
					if (carFollow.getSigma() is not None):
						outStr += ' sigma = "%f"' %(carFollow.getSigma())
					if (carFollow.getTau() is not None):
						outStr += ' tau = "%f"' %(carFollow.getTau())
					if (carFollow.getTimeHeadWay is not None):
						outStr += ' timeHeadWay = "%f"' %(carFollow.getTimeHeadWay())
					if (carFollow.getK() is not None):
						outStr += ' k = "%f"' %(carFollow.getK())
					if (carFollow.getPhl() is not None):
						outStr += ' phl = "%f"' %(carFollow.getPhl())
					outStr += '		/>'
					self.mPrintOutHandle.printOut(outStr)

					outStr = "		</%s>" %(PrintOutGridNetwork.TAG_VTYPE)
				else:
					#No car-following models
					if (vType.getAccel() is not None and vType.getDecel() is not None and vType.getMinGap is not None):
						outStr += ' accel = "%f"' 		%(vType.getAccel())
						outStr += '	decel = "%f"' 		%(vType.getDecel())
						outStr += ' minGap = "%f"'		%(vType.getMinGap())
					if (vType.getSigma() is not None):
						outStr += ' sigma = "%f"' 		%(vType.getSigma())
					if (vType.getTau() is not None):
						outStr += ' tau = "%f"' 			%(vType.getTau())
					if (vType.getColor() is not None):
						outStr += ' color = "%s"'			%(vType.getColor())
					if (vType.getLength() is not None):
						outStr += ' length = "%f"'		%(vType.getLength())
					if (vType.getMaxSpeed() is not None):
						outStr += ' maxSpeed = "%f"'	%(vType.getMaxSpeed())
					if (vType.getGuiShape() is not None):
						outStr += ' guiShape = "%s"'	%(vType.getGuiShape())
					outStr += "		/>"
					self.mPrintOutHandle.printOut(outStr)
		#Routes
		for r in iRouteList:
			outStr = None			
			if(r.getId() is not None and r.getEdges() is not None):
				outStr = '		<%s' %(PrintOutGridNetwork.TAG_ROUTE)
				outStr += '	id = "%s"' %(r.getId())
				outStr +=  ' edges ="'
				for edge in r.getEdges():
					outStr += '%s ' %(edge.getId())
				outStr += '"'
				if (r.getColor() is not None):
					outStr += ' color = "%s"' %(r.getColor())
				outStr += '	/>'
				self.mPrintOutHandle.printOut(outStr)

		#Vehicles
		for v in iVehicleList:
			outStr = None
			if (v.getId() is not None and v.getType() is not None and v.getRoute() is not None and v.getDepart() is not None):
				#Vehicle
				outStr = '		<%s' %(PrintOutGridNetwork.TAG_VEHICLE)
				outStr += ' id = "%s"' %(v.getId())
				outStr += ' type = "%s"' %(v.getType().getId())
				outStr += ' route = "%s"' %(v.getRoute())
				outStr += ' depart = "%f"' %(v.getDepart())
			#Debug Code
			#pdb.set_trace()	
			if (v.getColor() is not None):
				outStr += ' color = "%s"' %(v.getColor())
			if (v.getDepartLane() is not None):
				outStr += ' departLane = "%s"' %(v.getDepartLane())
			if (v.getDepartPos() is not None):
				outStr += ' departPos = "%s"' %(v.getDepartPos())
			if (v.getDepartSpeed() is not None):
				outStr += ' departSpeed = "%s"' %(v.getDepartSpeed())
			if (v.getArrivalLane() is not None):
				outStr += ' arrivalLane = "%s"' %(v.getArrivalLane())
			if (v.getArrivalPos() is not None):
				outStr += ' arrivalPos = "%s"' %(v.getArrivalPos())
			if (v.getArrivalSpeed() is not None):
				outStr += ' arrivalSpeed = "%s"' %(v.getArrivalSpeed())
			outStr += ' />'
			self.mPrintOutHandle.printOut(outStr)
		self.mPrintOutHandle.printOut(self.mXmlEnd)
		self.mPrintOutHandle.printOutEnd()

	def printOutPolyXml(self, iPolyList):
		self.mPrintOutHandle.printOut(self.mXmlHead)

		for poly in iPolyList:
			outStr = ""
			if (poly.getId() is not None and poly.getColor() is not None and len(poly.getShape()) > 0):
				outStr = '		<%s' %(PrintOutGridNetwork.TAG_POLY)
				outStr += ' id="%s"' %(poly.getId())
				outStr += ' color="%s"' %(poly.getColor())
				outStr += ' shape="'
				for p in poly.getShape():
					outStr += "%f,%f " %(p.mX, p.mY)
				outStr = outStr[:len(outStr)-1]
				outStr += '" '
			else:
				continue
			if(poly.getFill() is not None):
				outStr += ' fill="%d"' %(poly.getFill())

			if(poly.getLayer() is not None):
				outStr += ' layer="%d"' %(poly.getLayer())

			if(poly.getType() is not None):
				outStr += ' type="%s"' %(poly.getType())

			if(poly.getImgFile() is not None):
				outStr += ' imgFile="%s"' %(poly.getImgFile())

			outStr += '		/>'
			self.mPrintOutHandle.printOut(outStr)

		self.mPrintOutHandle.printOut(self.mXmlEnd)
		self.mPrintOutHandle.printOutEnd()

