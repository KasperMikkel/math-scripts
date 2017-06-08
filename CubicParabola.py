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

#Discriminant
Disc0 = b**2 - 3*a*c
Disc1 =	2*b**3 - 9*a*b*c +27*a**2*d
Disc = (Disc1 - 4 * Disc0**3) / -27*a**2 
print("Disc = %d" % Disc)
Cp = ((Disc1 + (Disc1**2 - 4*Disc0**3)**(1/2))/2)**(1/3)
Cm = ((Disc1 - (Disc1**2 - 4*Disc0**3)**(1/2))/2)**(1/3)

#/CubicParabola.py 1 3 -6 -8 should be -4 -1 2 

u = -0,5 + 0,866025404j

for n in range(1,4):
	print("Answer {0} is {1}".format( n, ((b + u**n*Cm + (Disc0/u**n*Cm))/3*a)))
