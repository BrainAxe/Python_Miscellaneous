#!/usr/bin/env python

__author__ = "BrainAxe"

import os
import sys 
import fnmatch


def searcher():

	fname = raw_input("Search For(case insensative): ").lower()
	pattern = fname + '*'
	#Enter search location here
	location = raw_input("Location: ")  
	
	print "\n"

	for root, dirs, files in os.walk(location):
		
		new_dirs = [item.lower() for item in dirs]
		new_files = [item2.lower() for item2 in files]	

		for d in fnmatch.filter(new_dirs,pattern):
			print d + '<dir>'
		for f in fnmatch.filter(new_files,pattern):
			print f 




if __name__ == '__main__':
	searcher()

