#!/usr/bin/env python
"""
@file				CarFollowingModel.py
@author			Hequn Zhang
@date				09-04-2013
@version		0.1

Definition of car-following model
"""

class CarFollowingModel:
	def __init__(self, iId, iAccel, iDecel, iSigma, iTau, iTimeHeadWay, iMinGap, iK, iPhl):
		self.mId = iId
		self.mAccel = iAccel
		self.mDecel = iDecel
		self.mSigma = iSigma
		self.mTau = iTau
		self.mTimeHeadWay = iTimeHeadWay
		self.mMinGap = iMinGap
		self.mK = iK
		self.mPhl = iPhl

	def getId(self):
		return self.mId

	def getAccel(self):
		return self.mAccel

	def getDecel(self):
		return self.mDecel

	def getSigma(self):
		return self.mSigma

	def getTau(self):
		return self.mTau

	def getTimeHeadWay(self):
		return self.mTimeHeadWay

	def getMinGap(self):
		return self.mMinGap

	def getK(self):
		return self.mK

	def getPhl(self):
		return self.mPhl


