#!/usr/bin/python

import os
import random

relpath = "/New/Validation/O"
folder = os.path.join(os.getcwd(),relpath)
#print(folder)

imagefolder = os.listdir(folder)
# print(imagefolder)
imagefolder = random.sample(imagefolder, 1000)
for image in imagefolder:
	# print("****",image,"*****")
	f = os.path.join(folder, image)
	print(f)
	os.remove(f)