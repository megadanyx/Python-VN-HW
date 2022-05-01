#List
# 0 - free
# 1 - reserved
# 2 - bought

from os import system
from time import sleep
from random import randint

seats = [ 0, 0, 1, 2, 0, 0, 0, 0 ]
option = -1
place = 0
# Lean free places
while option != 4:
    system("cls")
    
    free_places = len(seats)

    for pi in range(len(seats)):
        if seats[pi] != 0:
            free_places -= 1
    # Lean free places
    ############ PLOT #####################
    print()
    for pi in range(len(seats)):
        print("", pi+1,"", end = " ")
    print()

    for pi in range(len(seats)):
        if seats[pi] == 1:
            print("|-|", end =" ")
        elif seats[pi] == 2:
            print("|+|", end =" ")
        else:
            print("| |", end =" ")
    print("\n")
    print("Free places: ", free_places)
    ############ PLOT #####################

    ############ Menu #####################
    print("MENU")
    print("1. Book")
    print("2. Buy")
    print("3. Cancel")
    print("4. Exit")         
    ############ Menu #####################
    option = int(input(">>>  "))
    ############ Condition 1.##############
    if option <= 4 and option >= 1:
                
        if option == 1:
            place = int(input("Whith place: "))
            place -= 1 
            if place <= 7 and place >= 0:    
                if seats[place] == 0:
                    seats[place] = 1
                    print(f"You booked a seat {place+1} !") 
                    sleep(1)   
                else: 
                    print("This place is not free!")
                    sleep(2)    
            else :
                print("This place dont'n exist!")         
                sleep(2)
        ############ Condition 1.#############
        
        ############ Condition 2.#############
        if option == 2:
            place = int(input("Whith place: "))
            place -= 1 
            if place <= 7 and place >= 0:    
                if seats[place] == 0:
                    seats[place] = 2
                    print(f"You bought a place {place+1} !")
                    sleep(1)  
                else: 
                    print("This place is not free!")
                    sleep(2)    
            else :
                print("This place dont'n exist!")         
                sleep(2)
        ############ Condition 2.#############
        if option == 3:
            place = int(input("Whith place cancel : "))
            place -= 1 
            if place <= 7 and place >= 0:
                if seats[place] !=0:
                    seats[place] = 0
                    print("The place has been canceled!")
                    sleep(2)
                else:
                    print("This place can't be canceled! he's free!")   
                    sleep(2)
    else:
        print("This solution does not exist!")
        sleep(2)
        continue