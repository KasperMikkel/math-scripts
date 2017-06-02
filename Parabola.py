#!/usr/bin/env python

from __future__ import print_function
import sys, math
from math import sqrt

try: 
    if sys.argv[4] == '-p':
        import matplotlib.pyplot as plt
except:
    pass

try:
	a = float(sys.argv[1])
	b = float(sys.argv[2])
	c = float(sys.argv[3])
	print("a = %d" % a)
	print("b = %d" % b)
	print("c = %d" % c)
except:
	
	a = float(raw_input("a = "))
	b = float(raw_input("b = "))
	c = float(raw_input("c = "))

d = b**2 - 4*a*c

print("d = %d" % d)

if d > 0:
	dx1 = math.ceil(((-b + sqrt(d))/(2*a)) * 1000) / 1000
	dx2 = math.ceil(((-b - sqrt(d))/(2*a)) * 1000) / 1000
	print("The parabola intersects the x-axis at x = {0} and x = {1}".format(dx1, dx2))
elif d == 0:
	dx1 = math.ceil(((-b + sqrt(d))/(2*a)) * 1000) / 1000
	print("The parabola intersects the x-axis at x = {0}".format(dx1))

else :
	print("The parabola doesn't intersect with the x-axis")

Tx = -b/2*a
Ty = -d/4*a
print("(Tx,Ty) = ({0},{1})".format(Tx,Ty))

TTx = a*5**2 + b*5 + c

print("At x = 5.0, y = {0}".format(TTx))
try:
	if sys.argv[4] == '-p':
		f_a=[]
		f_b=[]
		for x in range(-7,8,1):
			y = (a*x**2 + b*x + c)
			f_a.append(x)
			f_b.append(y)

		fig= plt.figure()
		axes=fig.add_subplot(111)
		axes.plot(f_a,f_b)
		plt.grid()
		plt.show()
except:
	exit()
