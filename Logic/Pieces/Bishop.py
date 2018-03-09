from Logic.Pieces.Pieces import Pieces
from Logic.Pieces.Movement.Diagonal import diagonal_top_left, diagonal_bottom_right, diagonal_bottom_left, \
    diagonal_top_right


class Bishop(Pieces):
    """
    Represent the pieces of type Bishop.
    """
    VALUE = 30
    RADIUS = 8
    TYPE = "B"

    def __init__(self, position, color):
        """
        Create a Bishop based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color)

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
