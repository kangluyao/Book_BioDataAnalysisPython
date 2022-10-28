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
locations = "N valley, S valley, S valley, SE peak, E ridge, SE peak, N valley"
Ndays = locations.count("S valley")
print(Ndays)
Ntransitions = locations.count("S valley, SE peak")
print(Ntransitions)

Ntransitions = locations.count("s Valley, se Peak") # invalid syntax, cause python are generally case-sensitive

# Exercise 12
## two methods download files from URL
### method1
pip install requests  # install package requests
import requests  # Import the requests library
URL = "https://pages.uoregon.edu/slouca/LoucaLab/SECTION_Publications/MODULE_Publications/CLASS_Books/UNIT_BioDataAnalysisPython/supporting_datasets/animal_species_names_1000.txt"
response = requests.get(URL)  # download the data behind the URL
open("animal_species_names_1000.txt", "wb").write(response.content)  # Open the response into a new file called animal_species_names_1000.txt

### method2
import wget
response = wget.download(URL, "data/animal_species_names_1000.txt")
fin = open(response, "rt")
species_names = fin.read()
fin.close()
NSycon = species_names.count("Sycon")
print(NSycon)  # 93

# 4.7.3 Replacing substrings
DNA = "TATCGGCATCTACTAATCCGACTTTCCCTTCACGAGCTAAGGCAACGGCTAAATTTACTGCAACAGTAGCGA"
## compute the complement of this sequence
### swap A <--> T
complement = DNA.replace("A", "a")  # temporarily replace A with a
complement = complement.replace("T", "A")  # replace T with A
complement = complement.replace("a", "T")  # replace a with T

### swap G <--> C
complement = complement.replace("G", "g")  # temporarily replace G with g
complement = complement.replace("C", "G")  # replace C with G
complement = complement.replace("g", "C")  # replace g with C
print(complement)

# Since replace returns the modified string, we can chain multiple replace calls to achieve the
#same outcome as above, but with fewer lines of code:
### swap A <--> T
complement = DNA.replace("A", "a").replace("T", "A").replace("a", "T")
### swap G <--> C
complement = complement.replace("G", "g").replace("C", "G").replace("g", "C")
print(complement)

# Exercise 13
complement = DNA.replace("A","T") # replace A with T
complement = complement.replace("T","A") # replace T with A
complement = complement.replace("G","C") # replace G with C
complement = complement.replace("C","G") # replace C with G

# 4.7.4 String formatting (C-style)
name = "Ecoli_K12"
L = 4639221
A = 0.24527
TX = "Genome of %s has length %d, adenine fraction %f"%(name, L, A)
print(TX)

print("Adenine fraction %.1f%%"%(100*A))  # %% indicates percent

# the “newline” character, represented by a \n
print("Genome of %s: \n length: %d \n Adenine fraction: %.1f%%"%(name, L, A*100))

# Exercise 14
Nbeetles = 105
average_weight = 1.6487135
country_of_origin = "Kenya"
print("Across %d examined beetles from %s, the average weight was %.3f g."%(Nbeetles, country_of_origin, average_weight))

# Exercise 15
mass = 596599.7
metabolic_rate = 48.65
print("Pinus massoniana: \n ")
