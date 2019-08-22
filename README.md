# gcode2png


python script for 3d rendering gcode files with mayavi

## Prerequisites:
	pip install numpy, mayavi, tvtk

## Usage:

# Single file generation
python ./gcode2png test.gcode moves=[true/false] support=[true/false] show=[true/false] bed=[true/false]

moves: show movements in red; default=false


support: show support layers in grey; default=true


bed: show printbed; default=true


show: true = show rendered image; false = save rendered image as png file


# batch generation

python ./gcode2png batch /Users/yourname/3dfiles/ moves=[true/false] support=[true/false] show=[true/false] bed=[true/false]


## Thanks to:
gcodeParser.py forked and modifed from: https://github.com/jonathanwin/yagv