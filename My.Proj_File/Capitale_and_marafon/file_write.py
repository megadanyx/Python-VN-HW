


##  Bazele operarii cu fisierile.
##  file.read()
##  file.write()
##  file.close()
##

City = input("Enter a city name >>>")

### Save it to a file ###

file = open("Capitale.txt", "w")  # write
file.write(City)
file.close()

file = open("Capitale.txt", "r") # read
capitala = file.read()

print(capitala)
file.close()
