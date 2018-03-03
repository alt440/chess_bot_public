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
    TYPE = ""

    def __init__(self, position, color):
        self.position = position
        self.COLOR = color
        self.status = 0

    def moves(self):
        """"
        Template for children class
        Returns a list of possible moves as a list
        """
        pass
