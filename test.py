#!/usr/bin/env python
from __future__ import division
import math
import sys
try:
    A = float(sys.argv[1])
    B = float(sys.argv[2])
    C = float(sys.argv[3])
    D = float(sys.argv[4])
except:
    A = raw_input("A = ")
    B = float(raw_input("B = "))
    C = float(raw_input("C = "))
    D = float(raw_input("D = "))

print A + B + C + D
