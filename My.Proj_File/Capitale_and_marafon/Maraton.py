


##################################

# name = 0

# while name != "":

from numpy import append

#### PRELUAREA DE LA TASTATURA A DATELOR #################
Maraton_score = []
for index in range(100):    
    name = str(input(f"Introdu numele[{index+1}] >>> "))
    score = str(input(f"introdu rezulatul[{index+1}] >>> "))
    print()
    if name == "" or score == "":
        break
    else:
        Maraton_score.append(f"|{index+1}| Name: {name} || Score: {score}")

#### PRELUAREA DE LA TASTATURA A DATELOR #################

#### PRINTAREA LA ECRAN ####################
print("\nAi introdus :", index , "sportivi!\n")

print(*Maraton_score, sep= "\n")
#### PRINTAREA LA ECRAN ####################

######### OPERAREA CU FAILUL ########################
file = open("Maraton.txt", "w")  # write
index = 1
for row in Maraton_score:
    if index <= 10:
        file.write(row + "\n")
    index +=1

file.close()
######### OPERAREA CU FAILUL ########################
     



