
from unicodedata import name


file = open("Capitale.txt", "r") # r- read

Capitala = file.read()
CapitalaName = Capitala.split(" ")
file.close()
first_str = len(CapitalaName)
print(len(first_str)
