


#########################################
file_1 = open("1.txt", "r")
stringchar_1  = file_1.read()
file_1.close()
file_2 = open("2.txt", "r")
stringchar_2  = file_2.read()
file_2.close()

if len(stringchar_1) == len(stringchar_2):
    
    print("Numarul de caractere este ega!")

else:
    
    print("Numarul de caractere nu este ega!")
