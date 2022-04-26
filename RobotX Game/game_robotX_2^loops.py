
from os import system
import random

###### Map Size ########
mapsizex = 20
mapsizey = 5
###### Map Size ########

###### coordonate robot ########
roboX = 5
roboY = 5
###### coordonate robot ########

###### coordonate bomb ########
       
bombX = random.randrange(1, mapsizex)     
bombY = random.randrange(1, mapsizey)

###### coordonate bomb ########

###### coordonate life ########
heartY = random.randrange(1, mapsizey)
heartX = random.randrange(1, mapsizex)

###### coordonate life ########

###### coordonate powerbank ########
powerbankX = random.randrange(1, mapsizey)
powerbankY = random.randrange(1, mapsizey)
###### coordonate powerbank ########
detone_bombX = 0
detone_bombY = 0

RobotHP = 100
RobotBR = 100

clear = "cls"
option = ""
# game loop (ciclu infinit)
while True :
    ################# 1.Draw Map ###################

    system(clear)
    # print("\n")
    for c in range(1,mapsizey + 1):
        print("\n", end = " ")
        for i in range(1,mapsizex + 1):
            if i == roboX and c == roboY :
                print("😎" , end = " ")
            elif detone_bombX == i and detone_bombY == c:
                print("x" , end = " ")
            elif i == bombX and c == bombY:   
                print("💣" , end = " ")
            elif i == heartX and c == heartY:
                print("❤" , end = " ")
            elif i == powerbankX and c == powerbankY:
                print("⚡" , end = " ")
             
            else :
                print("-" , end = " ")    

    print("\n\n HP :", RobotHP)
    print("\n Power:", RobotBR, "%")

    print("\n")

    ################# 1. Draw Map ###################

    ################# 2. Read Input ##################
    option = input(">>>")
            
    ################# 2. Read Input ##################
                 
    ################# 3. Decide ######################
  
    if option == "a" and roboX > 1:
        roboX -=1
        RobotBR -=1
    if option == "d" and roboX < mapsizex:
        roboX +=1
        RobotBR -=1
    
    if option == "s" and roboY < mapsizey:
        roboY +=1
        RobotBR -=1
    if option == "w" and roboY > 1:
        roboY -=1
        RobotBR -=1
    
    # check if bomb
    if roboX == bombX and roboY == bombY:
        detone_bombX =  bombX
        detone_bombY =  bombY
        RobotHP -= 10
        bombX = random.randrange(1, mapsizex)     
        bombY = random.randrange(1, mapsizey)
    elif  RobotHP == 0 :
        print("Game Over! ")
        print("Thank you for playing!")
        break    
    # check if heart
    if  roboX == heartX and roboY == heartY:
        heartY = random.randrange(1, mapsizey)
        heartX = random.randrange(1, mapsizex)
        if RobotHP < 100 :
            RobotHP += 10
    # check power 
       
    if roboX == powerbankX and roboY == powerbankY:   
        powerbankY = random.randrange(1, mapsizey)
        powerbankX = random.randrange(1, mapsizex)
        if RobotBR <= 100 and RobotBR > 90 :
            RobotBR += 2
        elif RobotBR < 90:
            RobotBR += 8 
    elif RobotBR < 1 :
        print("Game Over! (Power is 0) ")
        print("Thank you for playing!")
        break



    if option == "x":
        system(clear)
        print("Thank you for playing!")
        break

    ################# 3. Decide ######################