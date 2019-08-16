#!/usr/bin/env python3.4

# ######################################
# 
# pip install --upgrade matplotlib
# 
# ######################################

import re, os, sys
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n = 0.0
coords = []
x = []
y = []
z = []
fig = plt.figure(figsize=(5,5))
ax = plt.axes(projection='3d')
ax.set_axis_off()

#ax.view_init(60, 35)
ax.set_aspect('equal')

file = open('d.gcode','r')
gcode = file.readlines()
print("reading gcode...")

imgname='img.png'

numlayers = 0
numlayers_Ze = 0
numlayers_G0 = 0
zn = 0.0
for line in gcode:
	regex = r"height.*[0-9]*\.[0-9]*"
	matches = re.finditer(regex, line, re.IGNORECASE | re.MULTILINE)
	for matchNum, match in enumerate(matches, start=1):
		#print(match.group())
		layerheight = re.findall(r'[0-9]*\.[0-9]$', match.group())[0]
		#print(layer)
		#print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

	if re.findall(r'Z = ', line):
		numlayers_Ze = numlayers_Ze + 1
	if re.findall(r'G0 .* Z[0-9]', line):
		numlayers_G0 = numlayers_G0 + 1


	if re.match(r'; layer [0-9]*, Z = [0-9]', line):
		zm = re.findall(r'Z = [0-9]*[.][0-9]*', line)
		#print(zm[0])
		zn = float(zm[0].replace("Z = ", ""))/10

	if re.match(r'^G1', line):
		coord = re.findall(r'[XY][0-9]*[.][0-9]*', line)
		if coord:
			if len(coord) > 1:
				n = n + 0.1
				x.append(float((coord[0].replace("X", "")))/10)
				y.append(float((coord[1].replace("Y", "")))/10)
				z.append(zn)

'''
X = np.array(x)
Y = np.array(y)
Z = np.array(z)

sizeX = (X.max()-X.min())/10
sizeY = (Y.max()-Y.min())/10
print("Xlen: "+str(sizeX))
print("Ylen: "+str(sizeY))



if numlayers_Ze < 1:
	numlayers = numlayers_G0
else:
	numlayers = numlayers_Ze

print("layer height: "+layerheight)
print("number of numlayers: "+str(numlayers))
itemheight = float(numlayers)*float(layerheight)/10
print("bauteil in cm:"+str(itemheight))
'''
import matplotlib.patheffects as pe

print("creating image...")
#ax.scatter3D(x, y, z, c=z, s=1, cmap='rainbow');
ax.plot(x, y, z, lw=1, path_effects=[pe.Stroke(linewidth=2, foreground='g'), pe.Normal()])
#ax.scatter(x, y, z)
#ax.plot(x, y, z, color='r');

#import matplotlib.patheffects as pe
#ax.plot(x, y, z, color='r', lw=2, path_effects=[pe.Stroke(linewidth=5, foreground='g'), pe.Normal()])


plt.show()
print("saving image...")
#fig.savefig(imgname, dpi=150)

print("finished...")




