from Pieces import *
from Line import *
from Chessboard import *

class Rook(Pieces):
    """
    Represent the pieces of type Rook.
    """
    Value = 50
    Radius = 8
    Type = "R"
    name = 'Rook'

    def __init__(self,position,color):
        """
        Create a Rook based on the Piece class

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self,position,color,"R")
        add_piece_location(position, self)

    def moves_attack(self):
        return [y for x in [line_right_attack(self),
                            line_top_attack(self),
                            line_left_attack(self),
                            line_bottom_attack(self)]
                for y in x]

    def moves_blocked(self):
        return [y for x in [line_right_blocked(self),
                           line_top_blocked(self),
                           line_left_blocked(self),
                           line_bottom_blocked(self)]
                for y in x]

    def moves(self):
        """
        Returns all possible moves for the Rook.

        :return: List of the possible moves
        :rtype list
        """
        return [y for x in [line_right(self),
                            line_top(self),
                            line_left(self),
                            line_bottom(self)]
                for y in x]
