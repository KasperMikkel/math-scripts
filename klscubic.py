#!/usr/bin/env python

from __future__ import print_function
import sys,socket
import math
from math import sqrt

try: 
    if sys.argv[5] == '-p':
        import matplotlib.pyplot as plt
except:
    pass
try: # Take arguments and print them
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	d = float(sys.argv[4])
	print("a = %d" % a)
	print("b = %d" % b)
	print("c = %d" % c)
	print("d = %d" % d)    
except:
	a = float(raw_input("a = "))
	b = float(raw_input("b = "))
	c = float(raw_input("c = "))
	d = float(raw_input("d = "))

