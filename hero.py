
class Hero:

    # pos, spawnPos su dictovi

    def __init__(self, id, name, pos, life, gold, mineCount, spawnPos, crashed):
        self.id = id
        self.name = name
        # self.userId = userId
        self.pos = pos # dict sa x, y
        self.life = life
        self.gold = gold
        self.mineCount = mineCount
        self.spawnPos = spawnPos # dict sa x, y
        self.crashed = crashed
        self.heroTile = "@1" if id == 1 else "@2";
        self.mineTile = "$1" if id == 1 else "$2";


class Field:
    # field name can be empty
    # Prepreka, HerojName, AparatZaKavu, RudnikNeutralan, Rudnik1, Rudnik2, Prazno
    def __init__(self, fieldName):
        self.fieldName = fieldName