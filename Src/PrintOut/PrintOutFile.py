#!/usr/bin/env python
"""
@file PrintOutFile.py
@autohr Hequn Zhang
@date		27-03-2013

The class for print out to file.
"""
import os,sys
import pdb

class PrintOutFile:
	def __init__(self, iResPath,iFileName, iFileType = None, iFileSuffix = None):
		self.mFile = ""
		if iFileName is not None:
			self.mFile += iFileName + "."
			self.mRes = iResPath + iFileName + "/"
			self.mFileHandle = None
			if iFileType is not None:
				self.mFile += iFileType + "."

			if iFileSuffix is not None:
				self.mFile += iFileSuffix

	def checkFile(self):
		if not os.path.isdir(os.path.normpath(self.mRes)):
			os.mkdir(self.mRes)
		if self.mFile is None:
			return False
			
		if os.path.isfile(os.path.normpath(self.mRes + self.mFile)):
			return True
		else:
			return False

	def genFile(self):
		self.checkFile()
		try:
			self.mFileHandle = open(os.path.normpath(self.mRes + self.mFile), mode = 'w')
			return True
		except IOError:
			print "Generate " + self.mFile + " failed!"
			return False
		
	def printOut(self, iStr):
		#Debug code:
		#pdb.set_trace()
		if self.mFileHandle is None:
			if not self.genFile():
				return False
		print >> self.mFileHandle, iStr
		
		return True

	def printOutEnd(self):
		if self.mFileHandle is not None:
			self.mFileHandle.close()
			self.mFileHandle = None
			sys.stdout.flush()


