from urllib.parse import urlencode
from urllib.request import Request, urlopen
from hero import Hero, Field
from queue import Queue

import json

def parseHero (hero):
    id = hero['id'] #we know it is hero
    name = hero['name']
    userId = hero['userId']
    pos = (hero['pos']['x'], hero['pos']['y'])
    life = hero['life']
    gold = hero['gold']
    mineCount = hero['mineCount']
    spawnPos = hero['spawnPos']
    chrased = hero['crashed']

    return id, name, userId, pos, life, gold, mineCount, spawnPos, chrased


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

    print (lenOfFields, boardSize)

    currStart = 0
    for i in range(0, rows):
        finalBoard.append(fields[currStart: currStart + boardSize])
        currStart += boardSize


    return finalBoard


### init request ####

post_fields = {'key': 'eyx3wvrg', 'turns':200}     # actually 6 turns, it returns 3*4 = 12
url = 'http://192.168.3.251:9000/api/training'
request = Request(url, urlencode(post_fields).encode())
jsonData = json.loads(urlopen(request).read().decode())

### init request end ###

bol = False

while True:

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
    id, name, userId, pos, life, gold, mineCount, spawnPos, crashed = parseHero(hero)
    heroMy = Hero (id, name, userId, pos, life, gold, mineCount, spawnPos, crashed)
    heroTheir = None

    # iscitam ovog, to sam ja, i usporedim, na kraju imam njega i enemy heroa

    for concreteHero in heroes:
        id, name, userId, pos, life, gold, mineCount, spawnPos, crashed = parseHero(hero)

        if id == heroMy.id:
            continue
        else:
            heroTheir = Hero (id, name, userId, pos, life, gold, mineCount, spawnPos, crashed)


    goodBoard = parseBoard(boardSize, boardTiles)

    print ("numRows {}, numCols {}".format(len(goodBoard), len(goodBoard[0]) ))
    print ("turn {}, maxturns {}".format(turn, maxTurns))


    # for now not using, but will parse when decide which one will be which

    token = jsonData['token']
    viewUrl = jsonData['viewUrl']
    playUrl = jsonData['playUrl'] # koristi se za zahtjev


    print ("viewUrl {}".format(viewUrl))

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

        visited = set()
        
        for direction in ['North', 'South', 'East', 'West']:
            nextPos = incPos(heroMy.pos, direction)
            ny, nx = nextPos

            if nx < 0 or ny < 0 or nx >= len(goodBoard) or ny > len(goodBoard):
                continue
            
            currTile = goodBoard[ny][nx]
            if (currTile in whereTo):
                printb (goodBoard)
                print (direction)
                return direction
                
            if currTile in ignoreds:
                continue

            queue.put((nextPos, [direction]))
            visited.add(nextPos)

        while not queue.empty():
            nexty, direction = queue.get()
            # print (direction)
            # print (0)
            visited.add(nexty)

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
                    printb (goodBoard)
                    direction.append(dire)
                    print (direction)
                    return direction[0]
                
                if currTile in ignoreds:
                    continue
                
                cloned = list(direction)
                cloned.append(dire)
                queue.put((nextnext, cloned))

    def countTiles (goodBoard, tileTypes):
        return sum ([sum ([(1 if (tile in tileTypes) else 0) for tile in line]) for line in goodBoard])

    def algorithm2 (goodBoard, heroMy, heroTheir):
        # print (str(heroMy.pos['x']) + " " + str(heroMy.pos['y']))
        print (heroMy.life)
        if heroMy.life < 30:
            return bfsToClosesX(goodBoard, heroMy, heroTheir, ['[]'], ['$2', '$-', '##', '$1'])

        if countTiles(goodBoard, ['$-', '$2']) <= 1:
            if heroMy.life < 60:
                bfsToClosesX(goodBoard, heroMy, heroTheir, ['[]'], ['$2', '$-', '##', '$1'])
            else:
                bfsToClosesX(goodBoard, heroMy, heroTheir, ['@2'], ['[]', '$2', '$-', '##', '$1'])

        return bfsToClosesX(goodBoard, heroMy, heroTheir, ['$2', '$-'], ['##', '$1', '[]'])



    ##complicated algo to determine direction###

    dir = callDirectionAlgorithm (algorithm2, goodBoard, heroMy, heroTheir)

    ############################################

    # Stay, North, South, East, West

    # if bol:
    #     dir = 'North'
    #     bol = not bol
    # else:
    #     dir = 'South'
    #     bol = not bol

    post_fields = {'key': 'eyx3wvrg', 'dir': dir}

    url = playUrl  # Set destination URL here
    request = Request(url, urlencode(post_fields).encode())
    jsonData = json.loads(urlopen(request).read().decode())

    ####current request end ###





