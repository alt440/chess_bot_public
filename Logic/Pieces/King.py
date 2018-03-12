from Logic.Pieces.Pieces import Pieces
from Logic.Chessboard import *

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
        Pieces.__init__(self, position, color,"K")


    def moves(self, kingOpposite):
        """
        Returns the list of possible moves for the Knight.

        :return: List of possible moves
        :rtype list
        """

        moves = list()  # List of possible moves
        file_pos = int(convert_file(self.position[0])) #letters: Columns
        rank_pos = int(self.position[1]) #rows

        """
        Check for all the position where the King could go.
        """

        if file_pos+1<=8:
            if rank_pos+1<=8:
                moves.append(convert_file(file_pos+1)+str(rank_pos+1))
            if rank_pos-1<=0:
                moves.append(convert_file(file_pos+1)+str(rank_pos-1))

            moves.append(convert_file(file_pos+1)+str(rank_pos))

        if file_pos-1>=0:
            if rank_pos+1<=8:
                moves.append(convert_file(file_pos-1)+str(rank_pos+1))
            if rank_pos-1<=0:
                moves.append(convert_file(file_pos-1)+str(rank_pos-1))

            moves.append(convert_file(file_pos-1)+str(rank_pos))

        if rank_pos+1<=8:

            moves.append(convert_file(file_pos)+str(rank_pos+1))

        if rank_pos-1>=0:

            moves.append(convert_file(file_pos)+str(rank_pos-1))

        return moves

