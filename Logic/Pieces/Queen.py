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
        possible_move.extend(chess_board[file_pos])

        # Horizontal
        possible_move.extend([chess_board[x][rank_pos-1] for x in range(len(rank))])

        # Diagonal
        

        # possible_move.append()
        print("r: ", rank_pos, " f: ", file_pos)
        # possible_move = set(possible_move)
        print(set(possible_move))
