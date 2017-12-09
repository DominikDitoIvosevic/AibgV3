from urllib.parse import urlencode
from urllib.request import Request, urlopen
from hero import Hero, Direction
import queue
import json
import time


#totalPath = []


def parseHero (hero):
    id = hero['id'] #we know it is hero
    name = hero['name']
    # userId = hero['userId']
    pos = hero['pos']
    life = hero['life']
    gold = hero['gold']
    mineCount = hero['mineCount']
    spawnPos = hero['spawnPos']
    chrased = hero['crashed']

    return id, name, None, pos, life, gold, mineCount, spawnPos, chrased


def callDirectionAlgorithm (fun, goodBoard, heroMy, heroTheir):
    return fun (goodBoard, heroMy, heroTheir)


def yieldDirection(currDirection):

    while currDirection.previousDirection is not None:
        currDirection = currDirection.previousDirection


    return  currDirection.dir


def yieldDirectionToCoffe(currDirection):

    while currDirection.previousDirection is not None:
        currDirection = currDirection.previousDirection

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










iter = 0

healing = False

# bfs
def algorithm1 (goodBoard, heroMy, heroTheir):

    global healing
    if heroMy.life < 22:
        healing = True

    if healing and heroMy.life > 90:
        healing = False

    if healing: 
        return goHealYourself(goodBoard, heroMy, heroTheir)

    if heroMy.mineCount >= heroTheir.mineCount + 2:
        return goHealYourself(goodBoard, heroMy, heroTheir)

    # if (iter > 150):
    #     if heroMy.life < 50:
    #         return goHealYourself(goodBoard, heroMy, heroTheir)

    if heroMy.life > heroTheir.life:
        if heroMy.pos['x'] == heroTheir.pos['x'] and heroMy.pos['y'] == heroTheir.pos['y'] + 2:
            return 'East'
        if heroMy.pos['x'] == heroTheir.pos['x'] and heroMy.pos['y'] == heroTheir.pos['y'] - 2:
            return 'West'
        if heroMy.pos['x'] == heroTheir.pos['x'] + 2 and heroMy.pos['y'] == heroTheir.pos['y']:
            return 'South'
        if heroMy.pos['x'] == heroTheir.pos['x'] - 2 and heroMy.pos['y'] == heroTheir.pos['y']:
            return 'North'
            

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

    cnt = 0

    while (cnt < len(boardTiles)):

        if boardTiles[cnt:cnt+2] == '  ':
            fields.append('Prazno')
        if boardTiles[cnt:cnt+2] == '##':
            fields.append('Prepreka')
        elif boardTiles[cnt:cnt+2] == '@1':
            fields.append('Heroj1')
        elif boardTiles[cnt:cnt+2] == '@2':
            fields.append('Heroj2')
        elif boardTiles[cnt:cnt+2] == '[]':
            fields.append('AparatZaKavu')
        elif boardTiles[cnt:cnt+2] == '$-':
            fields.append('RudnikNeutralan')
        elif boardTiles[cnt:cnt+2] == '$1':
            fields.append('Rudnik1')
        elif boardTiles[cnt:cnt+2] == '$2':
            fields.append('Rudnik2')

        cnt += 2


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

post_fields = {'key': 'lkzatce7'}     # actually 6 turns, it returns 3*4 = 12
url = 'http://192.168.2.104:9000/api/arena'
request = Request(url, urlencode(post_fields).encode())
jsonData = json.loads(urlopen(request).read().decode())

### init request end ###

bol = False
fstIter = True
goodBoard = None
viewUrl = None

while True:
    iter +=1

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
        id, name, _, pos, life, gold, mineCount, spawnPos, crashed = parseHero(concreteHero)

        if id == heroMy.id:
            continue
        else:
            heroTheir = Hero (id, name, None, pos, life, gold, mineCount, spawnPos, crashed)



  #  print ("numRows {}, numCols {}".format(len(goodBoard), len(goodBoard[0]) ))
  #  print ("turn {}, maxturns {}".format(turn, maxTurns))


    # for now not using, but will parse when decide which one will be which

    token = jsonData['token']
    viewUrl = jsonData['viewUrl']
    try:
        once
    except NameError:
        print(viewUrl)
        once = True
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
    st = time.time()
    dir = callDirectionAlgorithm (algorithm1, goodBoard, heroMy, heroTheir)
    print (time.time() - st)
   # print(dir)
    ############################################

    # Stay, North, South, East, West

    post_fields = {'key': 'lkzatce7', 'dir': dir}

    url = playUrl  # Set destination URL here
    request = Request(url, urlencode(post_fields).encode())
    try:
        jsonData = json.loads(urlopen(request).read().decode())
    except:
        print(urlencode(post_fields).encode())

    ####current request end ###

print(viewUrl)






