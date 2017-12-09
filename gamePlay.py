from urllib.parse import urlencode
from urllib.request import Request, urlopen
from hero import Hero, Direction
import queue
import json


totalPath = []


def parseHero (hero):
    id = hero['id'] #we know it is hero
    name = hero['name']
    userId = hero['userId']
    pos = hero['pos']
    life = hero['life']
    gold = hero['gold']
    mineCount = hero['mineCount']
    spawnPos = hero['spawnPos']
    chrased = hero['crashed']

    return id, name, userId, pos, life, gold, mineCount, spawnPos, chrased


def callDirectionAlgorithm (fun, goodBoard, heroMy, heroTheir):
    return fun (goodBoard, heroMy, heroTheir)


def yieldDirection(currDirection):

    while currDirection.previousDirection is not None:
        totalPath.append(currDirection.dir)
        currDirection = currDirection.previousDirection

    totalPath.append(currDirection.dir)

    return  currDirection.dir


def yieldDirectionToCoffe(currDirection):

    coffeDirection = []
    while currDirection.previousDirection is not None:
        coffeDirection.append(currDirection.dir)
        currDirection = currDirection.previousDirection

    coffeDirection.append(currDirection.dir)

    return currDirection.dir

def calcManhatan(x1, y1, x2, y2):
    return

def goHealYourself(goodBoard, heroMy, heroTheir):
    ### just find closest shite ###

   # pathsToHeal = []
   # cordsOfHeal = []

    qveve = queue.Queue()

    maxX = len(goodBoard)
    maxY = len(goodBoard[0])

    directons = ['North', 'South', 'East', 'West']
    directionRoute = {'North':(-1, 0), 'South': (1, 0), 'East': (0, 1), 'West':(0, -1)}

    currX, currY = heroMy.pos['x'], heroMy.pos['y']

    #print("trenutno polje {} {}".format(currX, currY))

    prevDirection = None

    visited = set()
    visited.add((currX, currY))


    while True:


        for dir in directons:

            dx, dy = directionRoute[dir]

            finX = currX + dx
            finY = currY + dy


            if finX >= maxX or finY >= maxY or finX < 0 or finY < 0:
                continue

            if goodBoard[finX][finY] == 'Prepreka':
                continue

            if goodBoard[currX][currY] == 'RudnikNeutralan' or goodBoard[currX][currY] == 'Rudnik1' or goodBoard[currX][currY] == 'Rudnik2':
                continue
            # nasli smo, treba prekinut i to, i rekonsturirat




            if (finX, finY) in visited:
                continue

          #  print("opcije {} {}".format(finX, finY))
            direction = Direction(prevDirection, dir, finX, finY)
            qveve.put(direction)


        if qveve.qsize() == 0:
            break

        currDirection = qveve.get()

        currX, currY = currDirection.x, currDirection.y
        visited.add((currX, currY))

        prevDirection = currDirection

       # print ("pretrazujemo {} {}".format(currX, currY))z
        if goodBoard[currX][currY] == 'AparatZaKavu':
            # nasli smo, treba prekinut i to, i rekonsturirat
            return yieldDirectionToCoffe(currDirection)

    #pathsToHeal.sort(key = len)

    #  manhatan1 = calcManhatan( heroMy[pos]['x'], heroMy[pos]['y'], heroTheir[pos]['x'], heroTheir[pos]['y'] )

    # meh , bumo onaj s najtupljim (najvecim kutem, i to je to)












# bfs
def algorithm1 (goodBoard, heroMy, heroTheir):

    if heroMy.life < 30:
         return goHealYourself(goodBoard, heroMy, heroTheir)


    ### just find closest shite ###

    qveve = queue.Queue()

    maxX = len(goodBoard)
    maxY = len(goodBoard[0])

    directons = ['North', 'South', 'East', 'West']
    directionRoute = {'North':(-1, 0), 'South': (1, 0), 'East': (0, 1), 'West':(0, -1)}

    currX, currY = heroMy.pos['x'], heroMy.pos['y']

    #print("trenutno polje {} {}".format(currX, currY))

    prevDirection = None

    visited = set()
    visited.add((currX, currY))


    while True:


        for dir in directons:

            dx, dy = directionRoute[dir]

            finX = currX + dx
            finY = currY + dy


            if finX >= maxX or finY >= maxY or finX < 0 or finY < 0:
                continue

            if goodBoard[finX][finY] == 'Prepreka' or goodBoard[finX][finY] == 'AparatZaKavu':
                continue

            if goodBoard[finX][finY] == 'Rudnik1':
                if heroMy.id == 1:  # it is already mine
                    continue

            if goodBoard[finX][finY] == 'Rudnik2':
                if heroMy.id == 2:  # it is already mine
                    continue


            if (finX, finY) in visited:
                continue

          #  print("opcije {} {}".format(finX, finY))
            direction = Direction(prevDirection, dir, finX, finY)
            qveve.put(direction)


        if qveve.qsize() == 0:
            totalPath.append('Stay')
            return 'Stay' #curr meta

        currDirection = qveve.get()

        currX, currY = currDirection.x, currDirection.y
        visited.add((currX, currY))

        prevDirection = currDirection

       # print ("pretrazujemo {} {}".format(currX, currY))

        if goodBoard[currX][currY] == 'RudnikNeutralan' or goodBoard[currX][currY] == 'Rudnik1' or goodBoard[currX][currY] == 'Rudnik2':
            # nasli smo, treba prekinut i to, i rekonsturirat
            return yieldDirection(currDirection)









def parseBoard(boardSize, boardTiles):

    # dakle kada napunimo prvu listu, onda appendamo na ukupnu listu
    # tip klase koja... kaze kakvo je polje..
    # meh pa na kraju samo konveratemo u matricu...

    fields = []

    while (len(boardTiles) > 0):

        if boardTiles[0:2] == '  ':
            fields.append('Prazno')
        if boardTiles[0:2] == '##':
            fields.append('Prepreka')
        elif boardTiles[0:2] == '@1':
            fields.append('Heroj1')
        elif boardTiles[0:2] == '@2':
            fields.append('Heroj2')
        elif boardTiles[0:2] == '[]':
            fields.append('AparatZaKavu')
        elif boardTiles[0:2] == '$-':
            fields.append('RudnikNeutralan')
        elif boardTiles[0:2] == '$1':
            fields.append('Rudnik1')
        elif boardTiles[0:2] == '$2':
            fields.append('Rudnik2')

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


### init request ####

post_fields = {'key': 'eyx3wvrg', 'turns':25}     # actually 6 turns, it returns 3*4 = 12
url = 'http://192.168.3.251:9000/api/training'
request = Request(url, urlencode(post_fields).encode())
jsonData = json.loads(urlopen(request).read().decode())

### init request end ###

bol = False
fstIter = True
goodBoard = None
viewUrl = None

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

    goodBoard = parseBoard(boardSize, boardTiles)


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



  #  print ("numRows {}, numCols {}".format(len(goodBoard), len(goodBoard[0]) ))
  #  print ("turn {}, maxturns {}".format(turn, maxTurns))


    # for now not using, but will parse when decide which one will be which

    token = jsonData['token']
    viewUrl = jsonData['viewUrl']
    playUrl = jsonData['playUrl'] # koristi se za zahtjev



   # print ("viewUrl {}".format(viewUrl))



    """
    dir = None
    if len(totalPath) > 0:
        dir = totalPath[-1]
        totalPath.pop()
    else:
        callDirectionAlgorithm (algorithm1, goodBoard, heroMy, heroTheir)
        dir = totalPath[-1]
        totalPath.pop()
    
    """

   #
    dir = callDirectionAlgorithm (algorithm1, goodBoard, heroMy, heroTheir)

   # print(dir)
    ############################################

    # Stay, North, South, East, West

    post_fields = {'key': 'eyx3wvrg', 'dir': dir}

    url = playUrl  # Set destination URL here
    request = Request(url, urlencode(post_fields).encode())
    jsonData = json.loads(urlopen(request).read().decode())

    ####current request end ###

print(viewUrl)






