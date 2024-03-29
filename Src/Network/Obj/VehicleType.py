#!/usr/bin/env python

"""
@file			VehicleType.py
@author		Hequn Zhang
@date			25-03-2013
@version	0.1

Definition of vehicle type
"""
from CarFollowingModel import	CarFollowingModel

class VehicleType:
	DEFAULT_TAU = 1
	DEFAULT_LENGTH = 5
	DEFAULT_MINGAP = 2.5
	DEFAULT_MAXSPEED = 70.0
	DEFAULT_SPEEDFACTOR = 1.0
	DEFAULT_SPEEDDEV = 0.0
	DEFAULT_COLOR = "1,1,0"
	DEFAULT_VCLASS = "unknown"
	DEFAULT_EMISSIONCLASS = "P_7_7"
	DEFAULT_GUISHAPE = "unknown" 
	DEFAULT_WIDTH = 2
	DEFAULT_IMGFILE = ""

	List_VClass = [
	"private",
	"public_transport",
	"public_emergency",
	"public_authority",
	"public_army",
	"vip",
	"ignoring",
	"passenger",
	"hov",
	"taxi",
	"bus",
	"delivery",
	"transport",
	"lightrail",
	"cityrail",
	"rail_slow",
	"rail_fast",
	"motorcycle",
	"bicycle",
	"pedestrian"
	]

	List_EmissionClass = [
	"pedestrian",
	"bicycle",
	"motorcycle",
	"passenger",
	"passenger/sedan",
	"passenger/hatchback",
	"passenger/wagon",
	"passenger/van",
	"delivery",
	"transport",
	"transport/semitrailer",
	"transport/trailer",
	"bus",
	"bus/city",
	"bus/flexible",
	"bus/overland",
	"rail",
	"rail/light",
	"rail/city",
	"rail/slow",
	"rail/fast",
	"rail/cargo",
	"evehicle"
	]
	#Car Following Models	
	CAR_FOLLOW_KRAUSS = "carFollowing-Krauss"
	CAR_FOLLOW_KRAUSSORIG1 = "carFollowing-KraussOrig1"
	CAR_FOLLOW_PWAGNER2009 = "carFollowing-PWagner2009"
	CAR_FOLLOW_IDM = "carFollowing-IDM"
	#ex. CAR_FOLLOW_PLATOON = "carFollowing-Platoon" 

	MAP_CAR_FOLLOW_MODEL = {
	CAR_FOLLOW_KRAUSS:CarFollowingModel(CAR_FOLLOW_KRAUSS, 0.8, 4.5, 0.5, 1, None, 3, None, None),
	CAR_FOLLOW_KRAUSSORIG1:CarFollowingModel(CAR_FOLLOW_KRAUSSORIG1, 0.8, 4.5, 0.5, 1, None, 3, None, None),
	CAR_FOLLOW_PWAGNER2009:CarFollowingModel(CAR_FOLLOW_PWAGNER2009, 0.8, 4.5, 0.5, 1, None, 3, None, None),
	CAR_FOLLOW_IDM:CarFollowingModel(CAR_FOLLOW_IDM, 0.8, 4.5, None, None, 1, 3, None, None)
	#ex. CAR_FOLLOW_PLATOON
	}

	def __init__(self, iId, iAccel, iDecel, iSigma = 0.5, iColor = None, iLength = None, iMinGap = None, iMaxSpeed = None, iGuiShape = None, iCarFollow = None, iTau = None, iSpeedFactor = 1.0, iSpeedDev = 0.1, iVClass = None, iEmissionClass = None, iWidth = None, iImgFile = None):
		self.mId = iId
		self.mCarFollow = self.setCarFollow(iCarFollow)
		
		self.mAccel = iAccel
		self.mDecel = iDecel
		self.mSigma = iSigma
		self.mTau = iTau
		self.mMinGap = iMinGap			
		
		self.mColor = iColor
		self.mLength = iLength
		self.mMaxSpeed = iMaxSpeed
		self.mGuiShape = iGuiShape

		self.mSpeedFactor = iSpeedFactor
		self.mSpeedDev = iSpeedDev
		self.mVClass = iVClass
		self.mEmissionClass = iEmissionClass
		self.mWidth = iWidth
		self.mImgFile = iImgFile

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

	def getLength(self):
		return self.mLength

	def getMinGap(self):
		return self.mMinGap

	def getMaxSpeed(self):
		return self.mMaxSpeed

	def getGuiShape(self):
		return self.mGuiShape

	def getCarFollow(self):
		return self.mCarFollow

	def getSpeedFactor(self):
		return self.mSpeedFactor

	def getSpeedDev(self):
		return self.mSpeedDev

	def getColor(self):
		return self.mColor

	def getVClass(self):
		return self.mVClass

	def getEmissionClass(self):
		return self.mEmissionClass

	def getWidth(self):
		return self.mWidth

	def getImgFile(self):
		return self.ImgFile
	
	def setCarFollow(self, iCarFollow):
		if iCarFollow is None:
			return None
		else:
			if VehicleType.MAP_CAR_FOLLOW_MODEL.has_key(iCarFollow):
				return VehicleType.MAP_CAR_FOLLOW_MODEL[iCarFollow]
			else:
				return None
