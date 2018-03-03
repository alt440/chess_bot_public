from Logic.Pieces.Pieces import *
from Logic.Pieces.Movement.Diagonal import *


class Queen(Pieces):
    def __init__(self, position, color):
        Pieces.__init__(self, position, color)

    VALUE = 90
    ATTACK_RADIUS = 8
    TYPE = "Q"

    def moves(self):
        return [diagonal_top_right(self), diagonal_top_left(self), diagonal_bottom_left(self),
                diagonal_bottom_right(self)]
