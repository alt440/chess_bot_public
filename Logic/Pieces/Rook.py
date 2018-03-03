from Logic.Pieces.Pieces import Pieces
from Logic.Pieces.Movement.Line import line_bottom, line_left, line_right, line_top

class Rook(Pieces):
    """
    Represent the pieces of type Rook.
    """
    Value = 50
    Radius = 8
    Type = "R"

    def __index__(self,position,color):
        """
        Create a Rook based on the Piece class

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self,position,color)

    def moves(self):
        """
        Returns all possible moves for the Queen.

        :return: List of the possible moves
        :rtype list
        """
        return [y for x in [line_right(self),
                            line_top(self),
                            line_left(self),
                            line_bottom(self)]
                for y in x]