from Logic.Pieces.Pieces import Pieces
from Logic.Pieces.Movement.Diagonal import diagonal_top_left, diagonal_bottom_right, diagonal_bottom_left, \
    diagonal_top_right



class Queen(Pieces):
    """
    Represent the pieces of type Queen.
    """
    VALUE = 90
    RADIUS = 8
    TYPE = "Q"

    def __init__(self, position, color):
        """
        Create a Queen Based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color)

    def moves(self):
        """
        Returns all possible moves for the Queen.

        :return: List of the possible moves
        :rtype list
        """
        return [y for x in [diagonal_top_right(self),
                            diagonal_top_left(self),
                            diagonal_bottom_left(self),
                            diagonal_bottom_right(self)]
                for y in x]