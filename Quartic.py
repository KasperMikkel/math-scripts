#!/usr/bin/env python
from __future__ import print_function
import sys,socket
import math
import cmath
from math import sqrt

try: 
    if sys.argv[6] == '-p':
        import matplotlib.pyplot as plt
except:
    pass
try: # Take arguments and print them
    a_input = float(sys.argv[1])
    b_input = float(sys.argv[2])
    c_input = float(sys.argv[3])
    d_input = float(sys.argv[4])
    e_input = float(sys.argv[5])

except:
    a_input = float(raw_input("a_input = "))
    b_input = float(raw_input("b_input = "))
    c_input = float(raw_input("c_input = "))
    d_input = float(raw_input("d_input = "))
    e_input = float(raw_input("e_input = "))
print("a_input = %d" % a_input)
print("b_input = %d" % b_input)
print("c_input = %d" % c_input)
print("d_input = %d" % d_input)
print("e_input = %d" % e_input)
a = 1.0
b = b_input/a_input
c = c_input/a_input
d = d_input/a_input
e = e_input/a_input
print("a = {0}".format(a))
print("b = {0}".format(b))
print("c = {0}".format(c))
print("d = {0}".format(d))
print("e = {0}".format(e))

f = c-((3*b**2)/8)
g = d+(b**3/8)-(b*c/2)
h = e-((3*b**4)/256)+((b**2*c)/16)-(b*d/4)

print("f = {0}".format(f))
print("g = {0}".format(g))
print("h = {0}".format(h))
