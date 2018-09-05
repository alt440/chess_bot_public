from Pieces import *
from Diagonal import *
from Line import *
from Chessboard import *


class Queen(Pieces):
    """
    Represent the pieces of type Queen.
    """
    VALUE = 90
    RADIUS = 8
    TYPE = "Q"
    name = 'Queen'

    def __init__(self, position, color):
        """
        Create a Queen based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color, "Q")
        add_piece_location(position, self)

    def moves_attack(self):
        return [y for x in [diagonal_top_right_attack(self),
                            diagonal_top_left_attack(self),
                            diagonal_bottom_left_attack(self),
                            diagonal_bottom_right_attack(self),
                            line_right_attack(self),
                            line_top_attack(self),
                            line_left_attack(self),
                            line_bottom_attack(self)]
                for y in x]

    def moves_blocked(self):
        return [y for x in [diagonal_top_right_blocked(self),
                            diagonal_top_left_blocked(self),
                            diagonal_bottom_left_blocked(self),
                            diagonal_bottom_right_blocked(self),
                            line_right_blocked(self),
                            line_top_blocked(self),
                            line_left_blocked(self),
                            line_bottom_blocked(self)]
                for y in x]

    def moves(self):
        """
        Returns all possible moves for the Queen.

        :return: List of the possible moves
        :rtype list
        """
        return [y for x in [diagonal_top_right(self),
                            diagonal_top_left(self),
                            diagonal_bottom_left(self),
                            diagonal_bottom_right(self),
                            line_right(self),
                            line_top(self),
                            line_left(self),
                            line_bottom(self)]
                for y in x]
