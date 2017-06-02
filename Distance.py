#!/usr/bin/env python
from math import sqrt
import sys

try:
    A_x = float(sys.argv[1])
    A_y = float(sys.argv[2])
    B_x = float(sys.argv[3])
    B_y = float(sys.argv[4])
except:
    A_x = float(raw_input("A_x = "))
    A_y = float(raw_input("A_y = "))
    B_x = float(raw_input("B_x = "))
    B_y = float(raw_input("B_y = "))

d = sqrt((A_x - B_x)**2 + (A_y - B_y)**2)

print("The distance is {0}".format(d))
