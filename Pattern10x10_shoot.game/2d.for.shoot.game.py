from os import system
from time import sleep
from random import randint

rx = 6
### bullet coord ###
bx = -1
by = 0
### bullet coord ###

### boomb coord ###
tx = 5
ty = 5
### boomb coord ###

option = ""
score = 0

########### Draw Pattern 10x10 ######xx
print()
while option != "x":
    system("cls")
    for y in range(1,11):
        for x in range(1,11):
            if x == rx and y == 10:
                print("R", end = " ")
            elif x == bx and y == by:
                print("^", end = " ")
            elif x == tx and y == ty:      
                print("X", end = " ")
            else:    
                print(".", end = " ")
        print()
    sleep (0.1)    
    print("                           " , score, end = "\n")   
########### Draw Pattern 10x10 ################
############## Target ##########################    
###    if ty != 10:
###        sleep(1)
###       ty +=1 
###        if ty == 10 and tx == rx:
###            print("Game Over")   
###            break     
###       if ty == 10:
###           ty = randint(1 ,7)
###            tx = randint(1 , 10)
###        continue 
############## Target ###########################    

############## Bullet###########################    
    if by != 0:
        by -=1
          
        if bx == tx and by == ty :
            ty = randint(1 , 7)
            tx = randint(1 , 10)
            score += 1
            by = 0
        continue  
############## Bullet###########################    

########### Control Game #######################
    option = input(">>>>>")
    if option == "a":
        if rx != 1:
            rx -=1
    if option == "d":
        if rx != 10:
            rx +=1    
    if option == " ": 
        bx = rx
        by = 10-1
         
        
########### Control Game #######################