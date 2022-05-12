# this module contains the map logic
# 0 = empty
# 1 = wall
# 2 = robot

rr = 1
rc = 8

gameMap = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], # 0 
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0], 
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 1, 1, 1, 0, 1, 0, 0, 1], 
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 1], 
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
   # 0  1                       9
]

gameMap[rr][rc] = 2

def p( c ):
    print(c + " ", end= "")

def printMap( m ):
    for ri in range(len(m)):
        for ci in range(len(m)):
            if m[ri][ci] == 0:
                p(".")
            elif m[ri][ci] == 1:
                p("#")
            elif m[ri][ci] == 2:
                p("R")
        
        print()


def Limit():
    gameMap[rr][rc] 