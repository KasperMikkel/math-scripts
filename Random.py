#!/usr/bin/env python
from __future__ import print_function
import random
import sys

try:
    min = float(sys.argv[1])
    max = float(sys.argv[2])
except:
    min = float(raw_input("Min = "))
    max = float(raw_input("Max = "))

print(random.randint(min,max))

