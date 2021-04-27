filestub = "radars"

manualscale = 0
width = 72.025
height = 92.127

xstart = 27
ystart = 98


filename = filestub + '.xyz'


xmin = 10000
xmax = -10000
ymin = 10000
ymax = -10000
line = 1
file = open(filename, 'r+')
#for i in range(10):
#  line = file.readline()

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

output = ';FLAVOR:Marlin\nM105\nM109 S0\nM82 ;absolute extrusion mode\nG92 E0 ;Reset Extruder\nM92 E1 ;Steps per ' \
         'mm\nG92 E0\nM107\nG1 F300 Z12\nG1 F1200\n\n'

line = file.readline()
while 1:
  # line = line.replace(',', ' Y')
  # output += "G1 X" + line
  comma = line.find(',')

  if manualscale:
    output += "G1 X" + str(xscale*(float(line[0:4])-xmin)+xstart) + " Y" + str(
      yscale*(float(line[comma + 1:comma + 5])-ymin)+ystart) + "\n"
  else:
    output += "G1 X" + str(float(line[0:4])-xmin+xstart) + " Y" + str(
      float(line[comma + 1:comma + 5])-ymin+ystart) + "\n"

  line = file.readline()
  output += 'G1 Z2\n'
  while line != '' and line != '\n':
    # line = line.replace(',', ' Y')
    comma = line.find(',')

    if manualscale:
      output += "G1 X" + str(xscale * (float(line[0:4]) - xmin) + xstart) + " Y" + str(
        yscale * (float(line[comma + 1:comma + 5]) - ymin) + ystart) + "\n"
    else:
      output += "G1 X" + str(float(line[0:4]) - xmin + xstart) + " Y" + str(
        float(line[comma + 1:comma + 5]) -ymin+ystart) + "\n"

    line = file.readline()

  # output = output[:-4]
  line = file.readline()
  if line == '':
    output += '\nG1 Z30'
    break
  else:
    output += 'G1 F300 Z12\nG1 F1200\n'
    # line = file.readline()

file.close()
filename = filestub + '.gcode'
file = open(filename, 'w')
file.write(output)
file.close()