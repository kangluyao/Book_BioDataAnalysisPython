# 4 Introduction to python
## 4.1 Variables
x = 3
y = 5.1 + 10.4
z = "hello"
number_of_genes = 3821  # longer names
species_name = "Mycobacterium lepraemurium"
treatment1 = "no antibiotics"
treatment2 = "with antibiotics"
##Spaces and other non-alphanumeric characters (except underscores) are not allowed in variable
##names

number_of_genes = 3821
average_gene_size = 1060
genome_size = number_of_genes * average_gene_size
print(genome_size)


# Exercise 1
x = 3
y = x * 5
x = y
z = x * 2
print(x, y, z)

# Exercise 2
## 1
number_of_cells = 2000
cell_volume = 0.001
total_volume = number_of_cells * cell_volume
print(total_volume)
## 2
number of cells = 2000  # variable name with whitespace
cell_volume = 0.001
total_volume = number_of_cells * cell_volume
## 3
2000 = number_of_cells  # cannot assign to literal
cell_volume = 0.001
total_volume = number_of_cells * cell_volume


# 4.4 Mathematical operations
x = 3
y = x + 4 # this assigns the value 3+4=7 to the variable y
z = y - 1 # this assigns the value 7-1=6 to the variable z
w = z / 4 # this assigns the value 6/4=1.5 to the variable w
q = w ** 3 # raise w to the power of 3 and assign the result to q
print(x, y, z, w, q)

# / performs true devision, // perform integer division.
A = 14 // 4 # this assigns the value 3 to A
B = 6.5 // 4 # this assigns the value 1 to B
C = 0.5 // 4 # this assigns the value 0 to C
print(A, B, C)

# % computes the remainder of integer division
r1 = 5 % 2 # this assigns the value 5 modulo 2 = 1 to the variable r1
r2 = 5 % 5 # this assigns the value 5 modulo 5 = 0 to the variable r2
print(r1, r2)

# add/subtract a value from an existing variable, or simply want to increase/
# decrease it by some factor
x1 = 3
x2 = 3
x3 = 3
x4 = 3
x1 += 4 # increment x by 4 and assign the result back to x1
x2 -= 2 # subtract 2 from x and assign the result back to x2
x3 *= 5 # multiply x by 5 and assign the result back to x3
x4 /= 10 # divide x by 10 and assign the result back to x4
print(x1, x2, x3, x4)

# combine several mathematical operations
x = 4 + 5 - 10
y = 10 ** 3
z = y*2 + x/3
print(x, y, z)

z = (y*2 + x)/3
print(z)

# complex mathematical expressions into multiple stages using parentheses or intermediate variables
f = x**(y + 3 * z**2)
print(f)
# or as follows:
exponent = y + 3 * z**2
f = x ** exponent
print(f)

# Integers vs. decimals (Floating point)
X = 3.0
N = 3
print(X, N)
# convert float to an integer
N = int(X)
print(X)
print(N)

# Exercise 4
F = 50
C = (F - 32) * 5 / 9
print(C)

# Exercise 5
x = 5
y = 2.1
z = 4.6
(x + y ** (2 * z + x)) / (100 * (x + y**3)) + x * z**4

# Exercise 6
year = 5
expected_adult_plants = 15 **(year-1)
print(expected_adult_plants)

# 4.5 Functions
print("Hello world")
help(print)
y = abs(x)

# Multiple arguments must be separated by commas.
smallest_number = min(10, 5, 98)
largest_number = max(10, 5, 98)
print("The smallest number is:",smallest_number)
print("The largest number is:",largest_numbe)

# nest multiple functions and mathematical expressions
print(abs(55-298))

fin = open("documents/some_text_file.txt", "rt")
contents = fin.read()
fin.close()

# Exercise 7:
elephant_masses = [114, 91, 98, 109, 91, 104, 125, 128, 93, 106, 134, 118]
smallest_calf = min(elephant_masses)
largest_calf = max(elephant_masses)
difference = abs(largest_calf - smallest_calf)
print("the mass of the smallest calf is", smallest_calf)
print("the mass of the largest calf is", largest_calf)
print("the mass difference between the smallest and largest calf is", difference)

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


