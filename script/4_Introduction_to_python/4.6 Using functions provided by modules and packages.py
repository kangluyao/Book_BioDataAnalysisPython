# 4.6 Using functions provided by modules and packages
# import module or package into python session
import math  # common mathematical functions
E = math.exp(0.5)  # To call a function from a specific module we use the module and function names, separated by a dot.
print(E)

import numpy  # more sophisticated mathematical functions
r = numpy.random.uniform(0, 100)
print(r)
# load the parts of a package that we actually need
from numpy import linalg, random
r = random.uniform(0, 100)
print(r)

# Exercise 8
N0 = 10**6
r = 0.2
N5 = N0 * math.exp(r * 5)
N20 = N0 * math.exp(r * 20)
print(N5, N20)

# Exercise 9
import math
x1 = 127.483226
y1 = 51.866239
x2 = 103.487167
y2 = 19.685403
A = ((math.cos(y2) * math.sin(abs(x1 - x2)))**2 + (math.cos(y1) * math.sin(y2) - math.sin(y1) * math.cos(y2) * math.cos(abs(x1 - x2)))**2)**0.5
B = math.sin(y1) * math.sin(y2) + math.cos(y1) * math.cos(y2) * math.cos(abs(x1 - x2))
R = 6371
D = R * math.atan2(A, B)
print(A, B, D)
