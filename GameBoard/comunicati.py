
import inspect

from serial import *

print(inspect.getfile(Serial))

print(dir(Serial))
ser = Serial.Serial('COM9', 9600, timeout=0,parity=Serial.PARITY_EVEN, rtscts=1)
#s = ser.read(100)       # read up to one hundred bytes
#print(s)