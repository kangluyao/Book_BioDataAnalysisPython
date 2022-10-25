# 4.7 Strings
# assigns a species name to a variable
full_species_name = "Escherichia coli"  # valid syntax
full_species_name = Escherichia coli  # invalid syntax

# concatenate strings using the addition symbol
genus_name = "Escherichia"
species_name = "coli"
full_species_name = genus_name + " " + species_name
print(full_species_name)

# repeats the string n times
codon = "CTA"
multiple_codons = codon * 10
print(multiple_codons)

# extracts characters from a string as a new string and prints it
genus_abbrev = genus_name[0:5]
print(genus_abbrev)

segment = genus_name[2:6]
print(segment)

first_character = genus_name[0]
print(first_character)

# prints out all but the last two characters
print(genus_name[0:-2])
# prints out the last character
print(genus_name[-1])

print(float("1.5") + float("2.0"))
print(int("1") + int("4"))

# Exercise 10
aminoacid_sequence = "ARNDARCLFPTVTSO"
print(aminoacid_sequence[3:6])  # 0 is first character, the [] 左闭右开
print(aminoacid_sequence[1:-1])
print(aminoacid_sequence[-2])

# Exercise 11
x = "10" + 5  # invalid syntax
x = 10 + 5 + "20"  # invalid
x = float(5) + "10"  # invalid
x = float("5") + 10  # valid, 15
x = "1" + "2" + 3  # invalid
x = "10" + "5"  # invalid
x = 1 + 2 + 3  # valid
"x" = "10"  # invalid
"10" + "5" = x  # invalid
x = int("4.5") + 1  # invalid
x = int("4") + 1  # valid
x = "3 + 4  # invalid

# 4.7.2 Counting substring occurrences
