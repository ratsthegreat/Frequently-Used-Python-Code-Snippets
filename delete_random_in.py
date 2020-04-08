#!/usr/bin/python

import os
import random

folder = os.path.join(os.getcwd(),"/New/Validation")
#print(folder)

files = os.listdir(folder)  # Get filenames in current folder
# print(files)
for file in files:
	imagefolder = os.path.join(folder,file)
	imagefolder = os.listdir(imagefolder)
	# print(imagefolder)
	imagefolder = random.sample(imagefolder, 3)
	for image in imagefolder:
		# print("****",image,"*****")
		f = os.path.join(folder,file, image)
		print(f)
		os.remove(f)