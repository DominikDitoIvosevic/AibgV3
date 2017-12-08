
class Hero:

    # pos, spawnPos su dictovi

    def __init__(self, id, name, userId, pos, lastDIr, life, gold, mineCount, spawnPos, crashed):
        self.id = id
        self.name = name
        self.userId = userId
        self.pos = pos
        self.lastDir = lastDIr
        self.life = life
        self.gold = gold
        self.mineCount = mineCount
        self.spawnPos = spawnPos
        self.crashed = crashed


