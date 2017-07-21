from __future__ import print_function

from shutil import copyfile

import os

class Clumpp():
	'Class for finding and preparing clumpp output from the output produced by clumpak'

	def __init__(self,wd,k):
		self.wd = wd
		self.k = k

		#Construct path to where files should reside
		tempdir = "K=" + self.k
		self.cdir = os.path.join(self.wd, tempdir, "MajorCluster", "CLUMPP.files")

		# check to see if directory exists
		self.dirExists(self.cdir)

		self.oldind = "ClumppIndFile.output"
		self.oldpop = "ClumppPopFile"

		#Get the files that contain clumpp output
		self.clumppoutind = os.path.join(self.cdir, self.oldind)
		self.clumppoutpop = os.path.join(self.cdir, self.oldpop)

		#Check if files exist
		self.fileExists(self.clumppoutind)
		self.fileExists(self.clumppoutpop)

		#find number of individuals and populations
		self.inds = self.linecount(self.clumppoutind)
		self.pops = self.linecount(self.clumppoutpop)

	def copyFiles(self):
		nd = self.makeDir()
		newind = os.path.join(nd, self.oldind)
		newpop = os.path.join(nd, self.oldpop)
		copyfile(self.clumppoutind, newind)
		copyfile(self.clumppoutpop, newpop)

	def makeDir(self):
		nd = os.path.join(self.wd, "best_results")
		if not os.path.exists(nd):
			os.makedirs(nd)
		return nd

	def linecount(self,fname):
		with open(fname) as f:
			for i, l in enumerate(f):
				pass
		return i+1

	def fileExists(self, filename):
		if( os.path.isfile(filename) != True ):
			print( filename, "does not exist" )
			print( "Exiting program..." )
			print( "" )
			raise SystemExit
		else:
			print(filename, "Exists")

	def dirExists(self,directory):
		if(os.path.isdir(directory) != True):
			print(repr(directory), "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
		else:
			print(directory, "Exists")
