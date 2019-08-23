#!/usr/bin/env python

from numpy import pi, sin, cos, mgrid
from gcodeParser import *
import sys, time, os
from mayavi import mlab
import numpy as np
from tvtk.api import tvtk
import logging
from PIL import Image


logger = logging.getLogger('gcodeParser')
logger.setLevel(level=logging.CRITICAL)
logger2 = logging.getLogger('tvtk')
logger2.setLevel(level=logging.CRITICAL)
logger3 = logging.getLogger('mayavi')
logger3.setLevel(level=logging.CRITICAL)

class GcodeRenderer:

	def __init__(self):
		self.imgwidth= 800
		self.imgheight = 600

		self.path=""
		self.support = ""
		self.moves = ""
		self.show = ""

		self.coords = {}
		self.coords['object'] = {}
		self.coords['moves'] = {}
		self.coords['support'] = {}
		self.coords['object']['x'] = []
		self.coords['object']['y'] = []
		self.coords['object']['z'] = []
		self.coords['moves']['x'] = []
		self.coords['moves']['y'] = []
		self.coords['moves']['z'] = []
		self.coords['support']['x'] = []
		self.coords['support']['y'] = []
		self.coords['support']['z'] = []

		self.bedsize = [210, 210]
		black = (0, 0, 0)
		white = (1, 1, 1)
		red = (1, 0, 0)
		lightgrey = (0.7529, 0.7529, 0.7529)
		blue = (0, 0.4980, 0.9960)
		mediumgrey = (0.7, 0.7, 0.7)
		darkgrey1 = (0.4509, 0.4509, 0.4509)
		darkgrey2 = (0.5490, 0.5490, 0.5490)

		self.supportcolor = lightgrey
		self.extrudecolor = blue
		self.bedcolor = mediumgrey
		self.movecolor = red


	def run(self, path, support, moves, bed, show):
		self.path = path
		self.support = support
		self.moves = moves
		self.createScene()
		if bed == "true":
			self.createBed()
		
		self.loadModel(self.path)
		self.plotModel()
		self.plotSupport()

		if show == "true":
			self.showScene()
		else:
			self.save()


	def loadModel(self, path):
		#print "loading file %s ..."%repr(path)
		parser = GcodeParser()
		model = parser.parseFile(path)

		for layer in model['object'].layers:
			for seg in layer.segments:
				#if seg.extrude > 0 and seg.distance > 0:
					#if seg.extrude/seg.distance > 1:
				if seg.style == "extrude":
					#if(seg.extrudate > 0.5):
					#print(seg.extrude/seg.distance)
					self.coords['object']['x'].append(seg.coords["X"])
					self.coords['object']['y'].append(seg.coords["Y"])
					self.coords['object']['z'].append(seg.coords["Z"])
				
				if self.moves == "true":
					if seg.style == "fly":
						self.coords['moves']['x'].append(seg.coords["X"])
						self.coords['moves']['y'].append(seg.coords["Y"])
						self.coords['moves']['z'].append(seg.coords["Z"])
		if self.support == "true":
			for layer in model['support'].layers:
				for seg in layer.segments:
					self.coords['support']['x'].append(seg.coords["X"])
					self.coords['support']['y'].append(seg.coords["Y"])
					self.coords['support']['z'].append(seg.coords["Z"])

	def createScene(self):
		fig1 = mlab.figure(bgcolor=(1,1,1),size=(self.imgwidth,self.imgheight))
		fig1.scene.parallel_projection = False
		fig1.scene.render_window.point_smoothing = False
		fig1.scene.render_window.line_smoothing = False
		fig1.scene.render_window.polygon_smoothing = False
		fig1.scene.render_window.multi_samples = 8
		fig1.scene.show_axes = False

	def createBed(self):
		x1, y1, z1 = (0, 210, 0.1)  # | => pt1
		x2, y2, z2 = (210, 210, 0.1)  # | => pt2
		x3, y3, z3 = (0, 0, 0.1)  # | => pt3
		x4, y4, z4 = (210, 0, 0.1)  # | => pt4

		bed = mlab.mesh([[x1, x2], [x3, x4]], [[y1, y2], [y3, y4]], [[z1, z2], [z3, z4]], color=self.bedcolor)

		img = tvtk.JPEGReader(file_name=sys.path[0]+"/bed_texture.jpg")
		texture = tvtk.Texture(input_connection=img.output_port, interpolate=1, repeat=0)
		bed.actor.actor.texture = texture
		bed.actor.tcoord_generator_mode = 'plane'


	def plotModel(self):
		mlab.plot3d(self.coords['object']['x'], self.coords['object']['y'], self.coords['object']['z'], color=self.extrudecolor, line_width=2.0, representation='wireframe')
		if len(self.coords['moves']['x']) > 0:
			mlab.plot3d(self.coords['moves']['x'], self.coords['moves']['y'], self.coords['moves']['z'], color=self.movecolor, line_width=2.0, representation='wireframe')

	def plotSupport(self):
		if len(self.coords['support']['x']) > 0:
			mlab.plot3d(self.coords['support']['x'], self.coords['support']['y'], self.coords['support']['z'], color=self.supportcolor, tube_radius=0.5)

	def showScene(self):
				#mlab.view(azimuth=45, elevation=70, focalpoint=[0, 0, 0], distance=62.0, figure=fig)
		#																	tube_radius=0.2, tube_sides=4

		#mlab.roll(-90)
		#mlab.view(45, 45)
		mlab.view(320, 70)
		mlab.view(distance=20)
		mlab.view(focalpoint=(self.bedsize[0]/2,self.bedsize[1]/2,20))
		mlab.show()

	def save(self):
		mlab.view(320, 70)
		mlab.view(distance=20)
		mlab.view(focalpoint=(self.bedsize[0]/2,self.bedsize[1]/2,20))
		img_path = self.path.replace("gcode", "png")
		mlab.savefig(img_path, size=(800,600))
		mlab.close(all=True)
		basewidth = 800
		img = Image.open(img_path)
		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save(img_path) 


if __name__ == '__main__':
	path = "test.gcode"
	support = "true"
	moves = "false"
	bed = "true"
	show = "false"


	if "batch" in sys.argv[1] and "=" not in sys.argv[2]:
		path = sys.argv[2]

		files = []
		# r=root, d=directories, f = files
		for r, d, f in os.walk(path):
			for file in f:
				if '.gcode' in file:
					files.append(os.path.join(r, file))
		for f in files:
			print(f)
			path = f
			renderer = GcodeRenderer()
			renderer.run(path, support, moves, bed, show)

	elif "=" not in sys.argv[1]:
		path = sys.argv[1]
	
		for arg in sys.argv:
			if "support=" in arg:
				support = arg.replace("support=", "")
			if "moves=" in arg:
				moves = arg.replace("moves=", "")
			if "bed=" in arg:
				bed = arg.replace("bed=", "")
			if "show=" in arg:
				show = arg.replace("show=", "")

		renderer = GcodeRenderer()
		renderer.run(path, support, moves, bed, show)
	else:
		print("wrong usage");

	
