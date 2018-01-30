"""
Parent Class for all the pieces.

Variables:
    position
    type
    value (importance of a piece)
    color
    status:
        -1: dead
        0: neutral
        1: attack
        2: attacked
        3: 1 & 2
    defence value (pieces protecting self)
    attack value (pieces attacked by self)

Method:
    move

"""


class Pieces:
    # Example for balck bishop (starting position)
    position = "c8"
    piece_type = "B"
    value = 3
    color = "b"
    status = 0
    defence_value = 0
    attack_value = 0

    def __init__(self, position, piece_type, value, color):
        self.position = position
        self.piece_type = piece_type
        self.value = value
        self.color = color

    def getPosition(self):
        return self.position

    def setPosition(self, p):
        self.position = p

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def getStatus(self):
        return self.status

    def setStatus(self, s):
        self.status = s

    def getDefenceValue(self):
        return self.defence_value

    def setDefenceValue(self, defence_value):
        self.defence_value = defence_value

    def getAttackValue(self):
        return self.attack_value

    def getAttackValue(self, attack_value):
        self.attack_value = attack_value