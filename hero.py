
class Hero:

    # pos, spawnPos su dictovi

    def __init__(self, id, name, userId, pos, life, gold, mineCount, spawnPos, crashed):
        self.id = id
        self.name = name
        self.userId = userId
        self.pos = pos # dict sa x, y
        self.life = life
        self.gold = gold
        self.mineCount = mineCount
        self.spawnPos = spawnPos # dict sa x, y
        self.crashed = crashed


class Direction:

    # Direction, String
    def __init__(self, previuousDirection, dir, x, y): # trenutna pozicija
        self.previousDirection = previuousDirection
        self.dir = dir
        self.x = x
        self.y = y


