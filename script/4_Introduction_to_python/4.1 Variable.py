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
