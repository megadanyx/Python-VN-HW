gameMap = [
    [5, 4, 0],
    [1, 4, 3],
    [4, 3, 2],
]

## ALGO --> savae the map
# serialization manual

def LoadTOfiel(map):
    file = open("map.txt", "w")
    for ri in range(3):
        for co in range(3):
            file.write(str(map[ri][co]))
    file.close()
#LoadTOfiel(gameMap)


# Algo load map from file
def DonwloadFromFile(map):
    file = open("map.txt", "r")
    for ri in range(3):
        for co in range(3):
            map[ri][co] = int(file.read(1))       
    file.close()
#DonwloadFromFile(gameMap)

# show to display
def PrintMap(map):
    for ri in range(3):
        for co in range(3):
            print(map[ri][co], end= " ")
        print()
#PrintMap(gameMap)


#LoadTOfiel(gameMap)
#DonwloadFromFile(gameMap)
PrintMap(gameMap)