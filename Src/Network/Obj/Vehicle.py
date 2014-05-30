#!/usr/bin/env python
"""
@file			Vehicle.py
@author		Hequn Zhang
@date			08-04-2013
@version	0.1

Definition of vehicles
"""
from VehicleType import VehicleType

class Vehicle:
	VEHICLE_TYPE_PRIVATE	= "passenger"
	VEHICLE_TYPE_TRANSPORT	= "transport"
	VEHICLE_TYPE_BUS	= "bus"
	VEHICLE_TYPE_EMERGENCY	= "emergency"

	VEHICLE_TYPE_PASSENGER_COLOR	= "1,1,0" #yellow
	VEHICLE_TYPE_TRANSPORT_COLOR	= "0,0,1" #blue
	VEHICLE_TYPE_BUS_COLOR				= "0,1,0" #green
	VEHICLE_TYPE_EMERGENCY_COLOR  = "1,0,0" #red

	MAP_VEHICLE_TYPE = {
	VEHICLE_TYPE_PRIVATE:VehicleType(VEHICLE_TYPE_PRIVATE, 2.6, 4.5, 0.5, VEHICLE_TYPE_PASSENGER_COLOR, 5, 2.5, 16.67, VEHICLE_TYPE_PRIVATE),
	VEHICLE_TYPE_TRANSPORT:VehicleType(VEHICLE_TYPE_TRANSPORT, 2.6, 4.5, 0.5 ,VEHICLE_TYPE_TRANSPORT_COLOR, 10, 3, 20, VEHICLE_TYPE_TRANSPORT),
	VEHICLE_TYPE_BUS:VehicleType(VEHICLE_TYPE_BUS, 2.6, 4.5, 0.5, VEHICLE_TYPE_BUS_COLOR, 10, 3, 20, VEHICLE_TYPE_BUS),
	VEHICLE_TYPE_EMERGENCY:VehicleType(VEHICLE_TYPE_EMERGENCY, 3.0, 5.5 , 0.1, VEHICLE_TYPE_EMERGENCY_COLOR, 7, 2.5, 30, "passenger/van")
	#ex. VEHICLE_TYPE_PLATOON:VehicleType(VEHICLE_TYPE_PLATOON, 1, 5.5 , 0.7, VEHICLE_TYPE_EMERGENCY_COLOR, 7, 2.5, 30, "passenger/van", VehicleType.CAR_FOLLOW_PLATOON)
	}
	
	def __init__(self, iId, iType, iRoute, iDepart, iColor = None, iDepartLane = None, iDepartPos = None, iDepartSpeed = None, iArrivalLane = None, iArrivalPos = None, iArrivalSpeed = None):
		self.mId = iId
		self.setVehicleType(iType) #Set vehicle type
		self.mRoute = iRoute	#Set Route
		self.mDepart = iDepart
		self.mColor = iColor
		self.mDepartLane = iDepartLane
		self.mDepartPos = iDepartPos
		self.mDepartSpeed = iDepartSpeed
		self.mArrivalLane = iArrivalLane
		self.mArrivalPos = iArrivalPos
		self.mArrivalSpeed = iArrivalSpeed

	def getId(self):
		return self.mId
	
	def getType(self):
		return self.mType

	def getRoute(self):
		return self.mRoute

	def getColor(self):
		return self.mColor

	def getDepart(self):
		return self.mDepart

	def getDepartLane(self):
		return self.mDepartLane
	def getRandomVehicleType(self):
		randKey = random.choice((list(Vehicle.MAP_VEHICLE_TYPE.keys())))
		return Vehicle.MAP_VEHICLE_TYPE[randKey]
	def getDepartPos(self):
		return self.mDepartPos

	def getDepartSpeed(self):
		return self.mDepartSpeed

	def getArrivalLane(self):
		return self.mArrivalLane

	def getArrivalPos(self):
		return self.mArrivalPos

	def getArrivalSpeed(self):
		return self.mArrivalSpeed

	def setVehicleType(self, iVehicleType):
		if Vehicle.MAP_VEHICLE_TYPE.has_key(iVehicleType):
			self.mType = Vehicle.MAP_VEHICLE_TYPE.get(iVehicleType)
		else:
			self.mType = Vehicle.MAP_VEHICLE_TYPE.get(Vehicle.VEHICLE_TYPE_PASSENGER)

