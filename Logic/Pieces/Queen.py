from Logic.Pieces.Pieces import Pieces
from Logic.Chessboard import *


class Queen(Pieces):
    def __init__(self, position, piece_type, value, color):
        Pieces.__init__(self, position, piece_type, value, color)

    def move(self):
        # Setup
        possible_move = list()
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1])

        # Vertical
        possible_move.extend(chess_board[file_pos - 1])

        # Horizontal
        possible_move.extend([chess_board[x][rank_pos - 1] for x in range(8)])

        # Diagonal
        for x in range(1, 9):
            delta_pos = rank_pos - x

            if 0 < file_pos - delta_pos <= 8
                file_letter = convert_file(file_pos - delta_pos)
                possible_move.append(file_letter + str(rank_pos - delta_pos))

            if 0 < file_pos + delta_pos <= 8:
                file_letter = convert_file(file_pos + delta_pos)
                possible_move.append(file_letter + str(rank_pos - delta_pos))

        return list(set(possible_move))
