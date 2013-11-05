#!/usr/bin/env python
"""
@file			EdgeType.py
@author		Hequn Zhang
@date			25-03-2013
@version	0.1

Definition of edge type
"""


class EdgeType:
	DEFAULT_DISCARD = "False" 
	DEFAULT_ONEWAY = "False"

	def __init__(self, iId, iNumLanes, iWidth,iPriority, iSpeed, iAllow = None, iDisallow = None, iDiscard = None, iOneway = None):
		self.mId = iId
		self.mNumLanes = iNumLanes
		self.mWidth = iWidth
		self.mPriority = iPriority
		self.mSpeed = iSpeed
		self.mAllow = iAllow
		self.mDisallow = iDisallow
		self.mDiscard = iDiscard
		self.mOneway = iOneway

	def getId(self):
		return self.mId

	def getWidth(self):
		return self.mWidth

	def getNumLanes(self):
		return self.mNumLanes

	def getPriority(self):
		return self.mPriority

	def getSpeed(self):
		return self.mSpeed

	def getAllow(self):
		return self.mAllow

	def getDisallow(self):
		return self.mDisallow

	def getDiscard(self):
		return self.mDiscard

	def getOneway(self):
		return self.mOneway
