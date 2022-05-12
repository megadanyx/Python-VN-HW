from map import *
from ui import *

while True:
    clear()
    printMap(gameMap)
    key = controls()

    if key == "x":
        break
    gameMap[rr][rc] = 0 # erse the robot
   
    if key == "d" and rc != 9 :
        if gameMap[rr][rc+1] != 1:
            rc +=1         # increment coord
        
    if key == "a" and rc != 0:
        if gameMap[rr][rc-1] != 1:
            rc -=1    
    if key == "s" and rr != 9 : 
        if gameMap[rr+1][rc] != 1:
            rr +=1
    
    if key == "w" and rr != 0:
        if gameMap[rr-1][rc] != 1:
            rr -=1
    gameMap[rr][rc] = 2 # put the robot


