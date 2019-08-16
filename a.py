# Create the data.
from numpy import pi, sin, cos, mgrid
from gcodeParser import *
from supportParser import *
import sys, time, os
from mayavi import mlab
import numpy as np

mx = []
my = []
mz = []
sx = []
sy = []
sz = []

def loadModel(path):
	print "loading file %s ..."%repr(path)
	t1 = time.time()
	print
	print "Parsing '%s'..."%path
	print
	parser = GcodeParser()
	model = parser.parseFile(path)
	print
	print "Done! %s"%model
	print
	t2 = time.time()
	print "loaded file in %0.3f ms" % ((t2-t1)*1000.0, )
	t1 = time.time()
	for layer in model.layers:
		for seg in layer.segments:
			mx.append(seg.coords["X"])
			my.append(seg.coords["Y"])
			mz.append(seg.coords["Z"])
			
	t2 = time.time()
	print "end renderColors in %0.3f ms" % ((t2-t1)*1000.0, )

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	# get the real path to the script
	script_path = os.path.realpath(__file__)
	# get the containing folder
	script_dir = os.path.dirname(script_path)
	# default to hana
	path = os.path.join(script_dir, "a.gcode")

def loadSupport(path):
	print "loading file %s ..."%repr(path)
	t1 = time.time()
	print
	print "Parsing '%s'..."%path
	print
	parser = SupportParser()
	model = parser.parseFile(path)
	print
	print "Done! %s"%model
	print
	t2 = time.time()
	print "loaded file in %0.3f ms" % ((t2-t1)*1000.0, )
	t1 = time.time()
	for layer in model.layers:
		for seg in layer.segments:
			sx.append(seg.coords["X"])
			sy.append(seg.coords["Y"])
			sz.append(seg.coords["Z"])
			
	t2 = time.time()
	print "end renderColors in %0.3f ms" % ((t2-t1)*1000.0, )

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	# get the real path to the script
	script_path = os.path.realpath(__file__)
	# get the containing folder
	script_dir = os.path.dirname(script_path)
	# default to hana
	path = os.path.join(script_dir, "a.gcode")

loadModel(path)
loadSupport(path)

# default to the middle layer
#self.layerIdx = len(self.model.layers)-1



black = (0,0,0)
white = (1,1,1)
mlab.figure(bgcolor=white)
mlab.plot3d(mx, my, mz, color=(0.2, 0.2, 1), tube_radius=0.5)
mlab.plot3d(sx, sy, sz, color=(0.58, 0.58, 0.58), tube_radius=0.5)
#mlab.roll(-90)
#mlab.view(45, 45)
mlab.view(320, 70)
mlab.view(distance=20)
mlab.view(focalpoint=(90,0,40))
mlab.show()



'''
import numpy as np
from mayavi import mlab
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider


def slider_changed(val):
    s.mlab_source.scalars = np.asarray(x * (val + 1), 'd')

# mayavi 3d plot
x, y = np.mgrid[0:3:1,0:3:1]
s = mlab.surf(x, y, np.asarray(x*0.1, 'd'))

# a matplotlib slider
plt.figure()
ax = plt.subplot(1, 1, 1)
slider = Slider(ax, valmin=0., valmax=1., label='test')
slider.on_changed(slider_changed)

plt.show()
mlab.show()
'''