from Logic.Chessboard import convert_file
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
    # Example for black bishop (starting position)
    position = "c8"
    type = "B"
    value = 3
    color = "b"
    status = 0
    defence_value = 0
    attack_value = 0

    def __init__(self, position, piece_type, value, color):
        self.position = position
        self.type = piece_type
        self.value = value
        self.color = color
