from Pieces import *
from Diagonal import *
from Chessboard import *


class Bishop(Pieces):
    """
    Represent the pieces of type Bishop.
    """
    VALUE = 30
    RADIUS = 8
    TYPE = "B"
    name = 'Bishop'

    def __init__(self, position, color):
        """
        Create a Bishop based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color,"B")
        add_piece_location(position, self)

    def moves_attack(self):
        return [y for x in [diagonal_top_right_attack(self),
                            diagonal_top_left_attack(self),
                            diagonal_bottom_left_attack(self),
                            diagonal_bottom_right_attack(self)]
                for y in x]

    def moves_blocked(self):
        return [y for x in [diagonal_top_right_blocked(self),
                            diagonal_top_left_blocked(self),
                            diagonal_bottom_left_blocked(self),
                            diagonal_bottom_right_blocked(self)]
                for y in x]

    def moves(self):
        """
        Returns all possible moves for the Bishop.

        :return: List of the possible moves
        :rtype list
        Methods from Logic.Pieces.Movement.Diagonal
        """
        return [y for x in [diagonal_top_right(self),
                            diagonal_top_left(self),
                            diagonal_bottom_left(self),
                            diagonal_bottom_right(self)]
                for y in x]
