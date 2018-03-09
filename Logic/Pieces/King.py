from Logic.Pieces.Pieces import Pieces
from Logic.Chessboard import convert_file


class King(Pieces):
    """
    Represent the pieces of type King.
    """

    def __init__(self, position, color):
        """
        Create a King Based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color)


    def moves(self, kingOpposite):
        """
        Returns the list of possible moves for the Knight.

        :return: List of possible moves
        :rtype list
        """

        moves = list()  # List of possible moves
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1])

        """
        Check for all the position where the King could go.
        """

        #if file_pos+1<=8:
            #need to know position of the other King to make this condition
            
        
        return moves

