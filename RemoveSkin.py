filestub = "HandSkin"
filename = filestub + '.gcode'
file = open(filename, 'r')
lines = file.readlines()

file.seek(0)
n = 0
line = file.readline()
while 1:
  if line == ';TYPE:SKIN\n':
    skinstart = n
  elif line == 'G1 Z40 ;Raise Z\n':
    skinend = n - 1
  elif line == '':
    break
  n += 1
  line = file.readline()
file.close()

file = open(filename, 'w')
n = 0
for line in lines:
  if n < skinstart or n > skinend:
    file.write(line)
  n += 1

file.close()