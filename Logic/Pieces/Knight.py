from Logic.Pieces.Pieces import Pieces
from Logic.Chessboard import convert_file


class Knight(Pieces):
    def __init__(self, position, color):
        Pieces.__init__(self, position, color)

    def moves(self):
        # Setup
        moves = list()
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1])

        if rank_pos + 2 <= 8:
            if file_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 1)
                moves.append(file_letter + str(rank_pos + 2))
            if file_pos - 1 > 0:
                file_letter = convert_file(file_pos - 1)
                moves.append(file_letter + str(rank_pos + 2))

        if rank_pos - 2 > 0:
            if file_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 1)
                moves.append(file_letter + str(rank_pos - 2))
            if file_pos - 1 > 0:
                file_letter = convert_file(file_pos - 1)
                moves.append(file_letter + str(rank_pos - 2))

        if file_pos + 2 <= 8:
            if rank_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 2)
                moves.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0:
                file_letter = convert_file(file_pos + 2)
                moves.append(file_letter + str(rank_pos - 1))

        if file_pos - 2 > 0:
            if rank_pos + 1 <= 8:
                file_letter = convert_file(file_pos - 2)
                moves.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0:
                file_letter = convert_file(file_pos - 2)
                moves.append(file_letter + str(rank_pos - 1))

        return moves
