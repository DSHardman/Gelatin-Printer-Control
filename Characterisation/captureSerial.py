#! /usr/bin/python3
'''
Binh Nguyen, Jan 2019
to use python 2 use /usr/bin/python2
requires pySerial to be installed
add date to the header, and time to the begining of each line
add sys argument to customize
USE: make executable by chmod +x scriptname.py and
> ./recordSerial.py test1000.txt (and Enter)
or python3 captureSerial.py "this is my optional message added the top of the file"
'''
import serial, time, os, sys

SNAP_TIME = 0.7  # time in second to for time.sleep
serial_port = '/dev/ttyUSB0'  #  listening port, type ls /dev/ttyUSB* in shell for available ports
baud_rate = 9600  #  In arduino, Serial.begin(baud_rate), e.g. 115200 or 9600

logFile = 'captured_data_from_serialPort.csv'
intervalLog = True
intervalLogTime = 60    # in seconds
lastTime = 0

if len(sys.argv) == 2:
    msg = sys.argv[1]
    msg += '\n'
else:
    msg = 'Data captured Python script from PMS7003>>USB>>RPi\n'

with open(logFile, 'a+') as f:
    head_ = f.readline()
    if not head_.startswith("Data captured"):
        f.write(msg)
        header = 'time,pm2.5\n'
        f.write(header)
    else:
        time_ = time.strftime('%x %X', time.localtime())
        sprtor = '{}, 0\n'.format(time_)
        f.write(sprtor)
    
keep_going = True
print("Press Ctrl+C stop the logging")

ser = serial.Serial(serial_port, baud_rate)

def logData(logFile):
    ser.reset_input_buffer() # important!!! clearing up old data in the buffer 
    line = ser.readline()
    line = line.decode("utf-8")  #  ser.readline returns a binary, convert to string
    time_ = time.strftime('%x %X', time.localtime())
    log = ','.join((time_, line))
    with open(logFile, 'a') as f:
        f.write(log)
        print("logged: {}".format(log))
    return None

try:
    while keep_going:
        if intervalLog and time.time() - lastTime >= intervalLogTime:
            logData(logFile)
            lastTime = time.time()
        elif not intervalLog:
            logData(logFile)
except KeyboardInterrupt:
    print(">> Ctrl+C pressed, stop logging to {} file".format(logFile))
    f.close()
    raise SystemExit