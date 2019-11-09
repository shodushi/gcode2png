# gcode2png


python script for 3d rendering gcode files with mayavi

all images are created with width of 800px and somewhat ~600px height

## Installation:
	sudo pip install six==1.12.0 bokeh matplotlib numpy mayavi Pillow wxPython

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
