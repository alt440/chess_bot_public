from Pieces import *
from Chessboard import *


class Knight(Pieces):
    """
    Represent the pieces of type Knight.
    """
    name = 'Knight'

    def __init__(self, position, color):
        """
        Create a Knight Based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color,"N")
        add_piece_location(position, self)

    def moves(self):
        """
        Returns the list of possible moves for the Knight.

        :return: List of possible moves
        :rtype list
        """

        moves = list()  # List of possible moves
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1])



        """
        Check for all the position where the Knight could go. is_space_available check in Chessboard
        """
        if rank_pos + 2 <= 8:
            if file_pos + 1 <= 8 and is_space_available(file_pos+1, rank_pos+2, self.COLOR):
                file_letter = convert_file(file_pos + 1)
                moves.append(file_letter + str(rank_pos + 2))
            if file_pos - 1 > 0 and is_space_available(file_pos - 1, rank_pos + 2, self.COLOR):
                file_letter = convert_file(file_pos - 1)
                moves.append(file_letter + str(rank_pos + 2))

        if rank_pos - 2 > 0:
            if file_pos + 1 <= 8 and is_space_available(file_pos + 1, rank_pos - 2, self.COLOR):
                file_letter = convert_file(file_pos + 1)
                moves.append(file_letter + str(rank_pos - 2))
            if file_pos - 1 > 0 and is_space_available(file_pos - 1, rank_pos - 2, self.COLOR):
                file_letter = convert_file(file_pos - 1)
                moves.append(file_letter + str(rank_pos - 2))

        if file_pos + 2 <= 8:
            if rank_pos + 1 <= 8 and is_space_available(file_pos + 2, rank_pos + 1, self.COLOR):
                file_letter = convert_file(file_pos + 2)
                moves.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0 and is_space_available(file_pos + 2, rank_pos - 1, self.COLOR):
                file_letter = convert_file(file_pos + 2)
                moves.append(file_letter + str(rank_pos - 1))

        if file_pos - 2 > 0:
            if rank_pos + 1 <= 8 and is_space_available(file_pos - 2, rank_pos + 1, self.COLOR):
                file_letter = convert_file(file_pos - 2)
                moves.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0 and is_space_available(file_pos - 2, rank_pos - 1, self.COLOR):
                file_letter = convert_file(file_pos - 2)
                moves.append(file_letter + str(rank_pos - 1))

        return moves
