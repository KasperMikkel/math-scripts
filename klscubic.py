#!/usr/bin/env python
from __future__ import print_function
import sys,socket
import math
import cmath
from math import sqrt
from decimal import *
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
getcontext().prec = 28
f = Decimal(((3*c/a)-(b**2/a**2))/3)
g = Decimal(((2*b**3/a**3)-(9*b*c/a**2)+(27*d/a))/27)
h = Decimal((g**2/4)+(f**3/27))
print("f = {0}".format(f))
print("g = {0}".format(g))
print("h = {0}".format(h))

if h > 0:
    print("There is only 1 real root.")
elif f == 0 and \
     g == 0 and \
     h == 0:
        print("All 3 roots are real and equal.")
else :
    print("All 3 roots are real")
    q = Decimal(((g**2/4)-h))
    if q > 0:
        i = Decimal(math.pow(q, float(1)/2))
    elif q < 0:
        i = Decimal(-math.pow(abs(q), float(1)/2))
    else:
        print("Error line 48")

    j = Decimal(**(1./3))
    k = math.acos(-((1/(2*g))/2*(1/(2*i))))
    print("i = {0}".format(i))
    print("j = {0}".format(j))
    print("k = {0}".format(k))
    
