file_value = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)


class Pieces:
    """
    Abstract Class for all the Piece on the board
    :cvar VALUE: Value for the alpha pruning
    :cvar RADIUS: Range within which the piece can move/attack
    :cvar TYPE: Type of the piece (eg. Bishop = 'B')
    :ivar COLOR: 0 for white and 1 for black
    :ivar position: Location of a Piece on the board
    :ivar status: Is the Piece neutral::0, attacking::1 or attacked::2
    """

    VALUE = 0
    RADIUS = 0
    TYPE = ""#should type be a ivar instead? we have to know the type of the piece.

    def __init__(self, position, color, TYPE):#add TYPE parameter to add to chessboard dictionary?
        """
        Create a Piece.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        self.position = position
        self.COLOR = color
        self.status = 0
        self.TYPE = TYPE
        #ChessBoard.add_piece_location(position, piece+color)#is it ok? made add_piece_location static

    def moves(self):
        """"
        Template for children class
        Returns a list of possible moves as a list
        """
        pass
