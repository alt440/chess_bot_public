from Chessboard import *
from Pieces import *

class Pawn(Pieces):

    name = 'Pawn'

    def __init__(self, position, color):
        Pieces.__init__(self, position, color,"P")
        add_piece_location(position, self)

    @staticmethod
    def possibility_of_capturing(file_pos, rank_pos, color):
        return piece_location_chessboard_view[file_pos - 1][rank_pos - 1] is not None \
            and not (piece_location_chessboard_view[file_pos - 1][rank_pos - 1].COLOR == color)

    def is_space_occupied(file_pos, rank_pos):
        return piece_location_chessboard_view[file_pos - 1][rank_pos - 1] is not None


    #Firstly, taking in consideration all possible moves.
    def moves(self):
        moves = list()
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1]) #raw

        if self.COLOR == 0 and rank_pos == 2 and not Pawn.is_space_occupied(file_pos, rank_pos + 2): #white
            moves.append(convert_file(file_pos) + str(rank_pos + 2))

        elif rank_pos == 7 and self.COLOR == 1 and not Pawn.is_space_occupied(file_pos, rank_pos - 2): #black
            moves.append(convert_file(file_pos)+str(rank_pos-2))

        if self.COLOR == 0 and rank_pos+1 <= 8 and not Pawn.is_space_occupied(file_pos, rank_pos + 1):
            moves.append(convert_file(file_pos) + str(rank_pos + 1))

        elif self.COLOR == 1 and rank_pos-1 > 0 and not Pawn.is_space_occupied(file_pos, rank_pos - 1):
            moves.append(convert_file(file_pos) + str(rank_pos - 1))


        """
        Looking at the diagonals of the pawn allow it to eat another piece
        """
        if self.COLOR == 0:
            if file_pos-1 > 0 and rank_pos + 1 <= 8 and Pawn.possibility_of_capturing(file_pos - 1, rank_pos + 1, self.COLOR):
                moves.append(convert_file(file_pos - 1) + str(rank_pos + 1))
            if file_pos+1 <= 8 and rank_pos + 1 <= 8 and Pawn.possibility_of_capturing(file_pos + 1, rank_pos + 1, self.COLOR):
                moves.append(convert_file(file_pos + 1) + str(rank_pos + 1))

        elif self.COLOR == 1:
            if file_pos-1 > 0 and rank_pos - 1 > 0 and Pawn.possibility_of_capturing(file_pos - 1, rank_pos - 1, self.COLOR):
                moves.append(convert_file(file_pos - 1) + str(rank_pos - 1))
            if file_pos+1 <= 8 and rank_pos - 1 > 0 and Pawn.possibility_of_capturing(file_pos + 1, rank_pos - 1, self.COLOR):
                moves.append(convert_file(file_pos + 1) + str(rank_pos - 1))

        return moves









