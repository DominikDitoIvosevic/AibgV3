from urllib.parse import urlencode
from urllib.request import Request, urlopen
from hero import Hero, Field
from queue import Queue
import time

import json

bfsCounterMax = 50
bfsCounter = bfsCounterMax

def parseHero (hero):
    id = hero['id'] #we know it is hero
    name = hero['name']
    # userId = hero['userId']
    pos = (hero['pos']['x'], hero['pos']['y'])
    life = hero['life']
    gold = hero['gold']
    mineCount = hero['mineCount']
    spawnPos = hero['spawnPos']
    chrased = hero['crashed']

    return id, name, pos, life, gold, mineCount, spawnPos, chrased


def callDirectionAlgorithm (fun, goodBoard, heroMy, heroTheir):
    return fun (goodBoard, heroMy, heroTheir)

def algorithm1 (goodBoard, heroMy, heroTheir):
    return None

def printb(board):
    [print("".join(b)) for b in board]

def parseBoard(boardSize, boardTiles):

    # dakle kada napunimo prvu listu, onda appendamo na ukupnu listu
    # tip klase koja... kaze kakvo je polje..
    # meh pa na kraju samo konveratemo u matricu...

    fields = []
    state = 0
    stateBefore = 0

    while (len(boardTiles) > 0):
        fields.append(boardTiles[0:2])
        boardTiles = boardTiles[2:]

    lenOfFields = len(fields)
    rows = lenOfFields//boardSize
    finalBoard = []

    # print (lenOfFields, boardSize)

    currStart = 0
    for i in range(0, rows):
        finalBoard.append(fields[currStart: currStart + boardSize])
        currStart += boardSize

    return finalBoard

def incPos(pos, direction):
    # print (pos)
    y, x= pos
    if (direction == 'North'):
        return (y-1, x)
    if (direction == 'South'):
        return (y+1, x)
    if (direction == 'East'):
        return (y, x+1)
    if (direction == 'West'):
        return (y, x-1)
    raise Exception()

###current request###

def bfsToClosesX(goodBoard, heroMy, heroTheir, whereTo, ignoreds):
    queue = Queue()
    # queue
    bfsCounter = bfsCounterMax

    visited = set()
    
    for direction in ['North', 'South', 'East', 'West']:
        nextPos = incPos(heroMy.pos, direction)
        ny, nx = nextPos

        if nx < 0 or ny < 0 or nx >= len(goodBoard) or ny >= len(goodBoard):
            continue

        currTile = goodBoard[ny][nx]
        if (currTile in whereTo):
            # printb (goodBoard)
            # print (direction)
            return (direction, 1)
            
        if currTile in ignoreds:
            continue

        queue.put((nextPos, [direction]))

    while not queue.empty():
        nexty, direction = queue.get()
        # print (direction)
        # print (0)
        visited.add(nexty)

        if bfsCounter <= 0:
            bfsCounter = bfsCounterMax
            if time.time() - start > 0.8:
                return ('North', 999)
        
        bfsCounter -= 1

        for dire in ['North', 'South', 'East', 'West']:
            nextnext = incPos(nexty, dire)
            if nextnext in visited:
                continue
                
            ny, nx = nextnext

            if nx < 0 or ny < 0 or nx >= len(goodBoard) or ny >= len(goodBoard):
                continue

            # print(nextnext)
            currTile = goodBoard[ny][nx]
            # print(currTile)
            if currTile in whereTo:
                # printb (goodBoard)
                direction.append(dire)
                # print (direction)
                return (direction[0], len(direction))
            
            if currTile in ignoreds:
                continue
            
            cloned = list(direction)
            cloned.append(dire)
            queue.put((nextnext, cloned))

def countTiles (goodBoard, tileTypes):
    return sum ([sum ([(1 if (tile in tileTypes) else 0) for tile in line]) for line in goodBoard])

def getPathToHeal(goodBoard, heroMy, heroTheir):
    return bfsToClosesX(goodBoard, heroMy, heroTheir, ['[]'], ['$2', '$-', '##', '$1', '@2'])[0]

def getPathToGranny(goodBoard, heroMy, heroTheir):
    return bfsToClosesX(goodBoard, heroMy, heroTheir, [heroTheir.heroTile], ['[]', '$2', '$-', '##', '$1'])[0]

def getPathToMine(goodBoard, heroMy, heroTheir):
    return bfsToClosesX(goodBoard, heroMy, heroTheir, [heroTheir.mineTile, '$-'], ['[]', '$-', '##', heroMy.mineTile])[0]

def getDistanceToHeal(goodBoard, heroMy, heroTheir):
    # print(heroTheir)
    # print(heroMy)
    return bfsToClosesX(goodBoard, heroMy, heroTheir, ['[]'], ['$2', '$-', '##', '$1', '@2'])[1]

def getDistanceToGranny(goodBoard, heroMy, heroTheir):
    return bfsToClosesX(goodBoard, heroMy, heroTheir, [heroTheir.heroTile], ['[]', '$2', '$-', '##', '$1'])[1]

def getDistanceToMine(goodBoard, heroMy, heroTheir):
    return bfsToClosesX(goodBoard, heroMy, heroTheir, [heroTheir.mineTile, '$-'], ['[]', '$-', '##', heroMy.mineTile])[1]

### init request ####

post_fields = {'key': 'h7hhobdd', 'turns':200}     # actually 6 turns, it returns 3*4 = 12
url = 'http://192.168.2.104:9000/api/arena'
request = Request(url, urlencode(post_fields).encode())
jsonData = json.loads(urlopen(request).read().decode())

### init request end ###

bol = False
start = time.time()

while True:
    old = start
    start = time.time()
    print (start-old)
    # at beggining fetched before while, will fetch at the end of loop

    game = jsonData['game']
    game_id = game['id']
    turn = game['turn']
    maxTurns = game['maxTurns']
    heroes = game['heroes']
    board = game['board']
    boardSize = board['size']
    boardTiles = board['tiles']
    finished = game['finished'] # find out type

    if finished:
        break

    hero = jsonData['hero']
    id, name, pos, life, gold, mineCount, spawnPos, crashed = parseHero(hero)
    heroMy = Hero (id, name, pos, life, gold, mineCount, spawnPos, crashed)
    heroTheir = None

    # iscitam ovog, to sam ja, i usporedim, na kraju imam njega i enemy heroa

    for concreteHero in heroes:
        # print(concreteHero)
        id, name, pos, life, gold, mineCount, spawnPos, crashed = parseHero(concreteHero)

        if id == heroMy.id:
            continue
        else:
            # print (concreteHero)
            heroTheir = Hero (id, name, pos, life, gold, mineCount, spawnPos, crashed)


    goodBoard = parseBoard(boardSize, boardTiles)

    # print ("numRows {}, numCols {}".format(len(goodBoard), len(goodBoard[0]) ))
    # print ("turn {}, maxturns {}".format(turn, maxTurns))


    # for now not using, but will parse when decide which one will be which

    token = jsonData['token']
    viewUrl = jsonData['viewUrl']
    playUrl = jsonData['playUrl'] # koristi se za zahtjev

    print ("viewUrl {}".format(viewUrl))

    def algorithm2 (goodBoard, heroMy, heroTheir):
        # print (str(heroMy.pos['x']) + " " + str(heroMy.pos['y']))
        # print (heroMy.life)
        if heroMy.life < 40:
            return getPathToHeal(goodBoard, heroMy, heroTheir)

        if heroTheir.mineCount - heroMy.mineCount > 4:
            if heroMy.life + 10 < heroTheir.life:
                return getPathToHeal(goodBoard, heroMy, heroTheir)
            return getPathToGranny(goodBoard, heroMy, heroTheir)

        if getDistanceToGranny(goodBoard, heroMy, heroTheir) < 5:
            # print (heroTheir)
            if heroMy.life < heroTheir.life:
                return getPathToHeal(goodBoard, heroMy, heroTheir)

        if countTiles(goodBoard, ['$-', heroTheir.mineTile]) < 3:
            if heroMy.life < 60:
                return getPathToHeal(goodBoard, heroMy, heroTheir)
            else:
                return getPathToGranny(goodBoard, heroMy, heroTheir)

        return getPathToMine(goodBoard, heroMy, heroTheir)



    ##complicated algo to determine direction###
    # print (heroTheir)
    dir = callDirectionAlgorithm (algorithm2, goodBoard, heroMy, heroTheir)

    ############################################

    # Stay, North, South, East, West

    post_fields = {'key': 'h7hhobdd', 'dir': dir}

    url = playUrl  # Set destination URL here
    request = Request(url, urlencode(post_fields).encode())
    jsonData = json.loads(urlopen(request).read().decode())

    ####current request end ###





