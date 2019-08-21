# gcode2png


python script for 3d rendering gcode files with mayavi

## Prerequisites:
	pip install numpy, mayavi, tvtk

## Usage:
python ./gcode2png test.gcode moves=[true/false] support=[true/false] show=[true/false] bed=[true/false]

moves: show movements in red; default=false


support: show support layers in grey; default=true


bed: show printbed; default=true


show: true = show rendered image; false = save rendered image as png file


## Thanks to:
gcodeParser.py forked and modifed from: https://github.com/jonathanwin/yagv