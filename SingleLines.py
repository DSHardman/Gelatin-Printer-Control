import numpy as np

filestub = "PneuNetM3"

manualscale = 1
addextrusion = 1

zoffset = 2

escale = 0.15
retractmm= 5

width = 18
height = 108

# xstart = 34
# ystart = 60

xstart = 10
ystart = 65


filename = filestub + '.xyz'


xmin = 10000
xmax = -10000
ymin = 10000
ymax = -10000
line = 1
file = open(filename, 'r+')

line = file.readline()
while 1:
  if line == '\n':
    line = file.readline()
    continue
  elif line == '':
    break
  comma = line.find(',')
  xmin = min(xmin, float(line[0:3]))
  xmax = max(xmax, float(line[0:3]))
  ymin = min(ymin, float(line[comma+1:comma+4]))
  ymax = max(ymax, float(line[comma+1:comma+4]))
  line = file.readline()

file.close()


xscale = width/(xmax-xmin)
yscale = height/(ymax-ymin)

file = open(filename, 'r+')

#for i in range(10):
#  line = file.readline()

output = ';FLAVOR:Marlin\nM105\nM109 S0\nM82 ;absolute extrusion mode\nG92 E-1 ;Reset Extruder\nM92 E10 ;Steps per ' \
         'mm\nG92 E0\nM107\nG1 F300 Z12\nG1 F1200\nG1 X25.00 Y42.00\nG1 F5000 E0\nG1 Z4\nG1 F300 X65 Y42 E6\nG1 F300' \
         'Z14\nG1 F1200\nG92 E0\n\n'


e = 0
line = file.readline()
while 1:
  comma = line.find(',')

  if manualscale:
    x = xscale * (float(line[0:4]) - xmin) + xstart
    y = yscale * (float(line[comma + 1:comma + 5]) - ymin) + ystart

  else:
    x = float(line[0:4]) - xmin + xstart
    y = float(line[comma + 1:comma + 5]) - ymin + ystart

  output += "G1 X" + str(x) + " Y" + str(y) + '\n'

  line = file.readline()

  if addextrusion:
    output += 'G1 F5000 E' + str(e) + '\n'

  output += 'G1 Z' + str(2+zoffset) + '\n'

  first = 1
  while line != '' and line != '\n':
    comma = line.find(',')

    xprev = x
    yprev = y
    if manualscale:
      x = xscale * (float(line[0:4]) - xmin) + xstart
      y = yscale * (float(line[comma + 1:comma + 5]) - ymin) + ystart
    else:
      x = float(line[0:4]) - xmin + xstart
      y = float(line[comma + 1:comma + 5]) - ymin + ystart

    if first:
      output += "G1 F300 X" + str(x) + " Y" + str(y)
      first = 0
    else:
      output += "G1 X" + str(x) + " Y" + str(y)

    if addextrusion:
      e += escale * np.sqrt((x - xprev) ** 2 + (y - yprev) ** 2)
      output += " E" + str(e) + "\n"
    else:
      output += "\n"

    line = file.readline()

  line = file.readline()
  if line == '':
    output += '\nG1 F5000 E' + str(e - retractmm) + '\nG1 Z30\nM18 E'
    break
  else:
    output += 'G1 F300 Z' + str(12+zoffset) + '\nG1 F1200\n'
    if addextrusion:
      output += 'G1 F5000 E' + str(e - retractmm) + '\n'

file.close()

filename = filestub + '.gcode'
file = open(filename, 'w')
file.write(output)
file.close()