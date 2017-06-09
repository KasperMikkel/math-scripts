#!/usr/bin/env python
from __future__ import print_function
import sys,socket
import math
import cmath
from math import sqrt
#from decimal import *
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
#getcontext().prec = 28
f = ((3*c/a)-(b**2/a**2))/3
g = ((2*b**3/a**3)-(9*b*c/a**2)+(27*d/a))/27
h = (g**2/4)+(f**3/27)
print("f = {0}".format(f))
print("g = {0}".format(g))
print("h = {0}".format(h))

if h > 0:
    print("There is only 1 real root.")
    R = -(g/2)+(h)**(float(1)/2)
    S = (R)**(float(1)/3)
    T = -(g/2)-(h)**(float(1)/2)
    if T > 0:
        U = math.pow(T, float(1)/3)
    elif T < 0:
        U = -math.pow(abs(T), float(1)/3)
    else:
        print("Error only 1 real root.")
    #U = (T)**(float(1)/3)
    q = ((g**2/4)-h)
    if q > 0:
        i = math.pow(q, float(1)/2)
    elif q < 0:
        i = -math.pow(abs(q), float(1)/2)
    else:
        print("Error Only 1 real root")
    X_1 = (S+U)-(b/(3*a))
    X_2_3 = (-(S+U)/2)-(b/(3*a))
    i_X = ((S-U)*(3)**(float(1)/2))/2
    

    print("R = {0}".format(R))
    print("S = {0}".format(S))
    print("T = {0}".format(T))
    print("U = {0}".format(U))
    print("i = {0}".format(i))
    print("i_X = {0}".format(i_X))
    print("X1 = {0}".format(X_1))
    print("X2 = {0} + i*{1}".format(X_2_3, i_X))
    print("X3 = {0} - i*{1}".format(X_2_3, i_X))
elif f == 0 and \
     g == 0 and \
     h == 0:
        print("All 3 roots are real and equal.")
        f = (((3*c)/a)-(b**2/a**2))/3
        g = ((((2*b**3)/a**3)-((9*b*c))/a**2)+((27*d)/a))/27
        x = (d/a)**(float(1)/3)*-1
        print("f = {0}".format(f))
        print("g = {0}".format(g))
        print("X1 = X2 = X3 = {0}".format(x))
else :
    print("All 3 roots are real")
    q = ((g**2/4)-h)
    if q > 0:
        i = math.pow(q, float(1)/2)
    elif q < 0:
        i = -math.pow(abs(q), float(1)/2)
    else:
        print("Error All 3 roots")

    j = math.pow(i, float(1)/3)

    K = math.acos(-(g/(2*i)))
    L = j*-1
    M = math.cos(K/3)
    N = math.sqrt(3)*math.sin(K/3)
    P = (b/(3*a))*-1
    X_1 = (2*j)*math.cos(K/3)-(b/(3*a))
    X_2 = L*(M+N)+P
    X_3 = L*(M-N)+P
    print("i = {0}".format(i))
    print("j = {0}".format(j))
    print("K = {0}".format(K))
    print("L = {0}".format(L))
    print("M = {0}".format(M))
    print("N = {0}".format(N))
    print("P = {0}".format(P))
    print("X1 = {0}".format(X_1))
    print("X2 = {0}".format(X_2))
    print("X3 = {0}".format(X_3))