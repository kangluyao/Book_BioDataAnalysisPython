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
