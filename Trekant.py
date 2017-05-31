#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
AB = float(raw_input('Enter AB: '))
BC = float(raw_input('Enter BC: '))
AC = float(raw_input('Enter AC: '))
#A_x = float(raw_input('Enter A.x: '))
#A_y = float(raw_input('Enter A.y: '))
#B_x = float(raw_input('Enter B.x: '))
#B_y = float(raw_input('Enter B.y: '))
A_x = 0.0
A_y = 0.0
B_x = AB
B_y = 0.0
#print AB + BC + AC + A_x + A_y + B_x + B_y

C_x = (AB**2-BC**2+AC**2)/(2*AB)
try:
    C_y = math.sqrt(BC**2-(B_x-C_x)**2)-B_y
except:
    print 'Ya idiot this shit is not a fucking triangle'
    exit()
print 'C.x = %f' % C_x
print 'C.Y = %f' % C_y
plt.plot([A_x,B_x,C_x,A_x], [A_y,B_y,C_y,A_y])
plt.show()
