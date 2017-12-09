from urllib.parse import urlencode
from urllib.request import Request, urlopen
from hero import Hero, Field

import json

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
    fun (goodBoard, heroMy, heroTheir)

def algorithm1 (goodBoard, heroMy, heroTheir):
    return None


def parseBoard(boardSize, boardTiles):

    # dakle kada napunimo prvu listu, onda appendamo na ukupnu listu
    # tip klase koja... kaze kakvo je polje..
    # meh pa na kraju samo konveratemo u matricu...

    fields = []
    state = 0
    stateBefore = 0



    for character in boardTiles:


        if character == '#':
            if state == 0:
                state = 1
            elif state == 1:
                state = 0
                fields.append(Field('Prepreka'))
        elif character == '@':
            stateBefore = 1
        elif character == '$':
            stateBefore = 2
        elif character == ']':
            fields.append(Field('AparatZaKavu'))
        elif character == '-':
            fields.append(Field('RudnikNeutralan'))
        elif character == '1':
            if stateBefore == 1:
                fields.append(Field("Heroj1"))
            elif stateBefore == 2:
                fields.append(Field("Rudnik1"))
            stateBefore = 0
        elif character == '2':
            if stateBefore == 1:
                fields.append(Field("Heroj2"))
            elif stateBefore == 2:
                fields.append(Field("Rudnik2"))
            stateBefore = 0
        elif character == ' ':
            fields.append(Field('Empty'))

    lenOfFields = len(fields)
    rows = lenOfFields//boardSize
    finalBoard = []

    currStart = 0
    for i in range(0, rows):
        finalBoard.append(fields[currStart: currStart + boardSize])
        currStart += boardSize


    return finalBoard


### init request ####

post_fields = {'key': 'eyx3wvrg', 'turns':3}     # actually 6 turns, it returns 3*4 = 12
url = 'http://192.168.3.251:9000/api/training'
request = Request(url, urlencode(post_fields).encode())
jsonData = json.loads(urlopen(request).read().decode())

### init request end ###

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



    ###current request###




    ##complicated algo to determine direction###

    dir = callDirectionAlgorithm (algorithm1, goodBoard, heroMy, heroTheir)

    ############################################

    post_fields = {'key': 'eyx3wvrg', 'dir': 'Stay'}

    url = playUrl  # Set destination URL here
    request = Request(url, urlencode(post_fields).encode())
    jsonData = json.loads(urlopen(request).read().decode())

    ####current request end ###








