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




path = '/Users/stefan/Seafile/3D-Druck/_octoprint'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.gcode' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)