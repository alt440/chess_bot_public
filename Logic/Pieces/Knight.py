from Logic.Pieces.Pieces import *
from Logic.Chessboard import *


class Knight(Pieces):
    # It would probably make more sense to create a default constructor for position, value and piece_type
    # How would you determine which position (since every player has two pieces)
    def __init__(self, color):
        if color == "white":
            Pieces.__init__(self, "b1", "knight", 3, color)
        else:
            Pieces.__init__(self, "b8", "knight", 3, color)

    def __str__(self):
        return ("You are in class Knight my I am at position {} and {}".format(self.getPosition(), self.getColor()))

    def move(self):
        # Setup
        possible_move = list()
        file_pos = int(convert_file(self.position[0]))
        rank_pos = int(self.position[1])

        if rank_pos + 2 <= 8:
            if file_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 1)
                possible_move.append(file_letter + str(rank_pos + 2))
            if file_pos - 1 > 0:
                file_letter = convert_file(file_pos - 1)
                possible_move.append(file_letter + str(rank_pos + 2))

        if rank_pos - 2 > 0:
            if file_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 1)
                possible_move.append(file_letter + str(rank_pos - 2))
            if file_pos - 1 > 0:
                file_letter = convert_file(file_pos - 1)
                possible_move.append(file_letter + str(rank_pos - 2))

        if file_pos + 2 <= 8:
            if rank_pos + 1 <= 8:
                file_letter = convert_file(file_pos + 2)
                possible_move.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0:
                file_letter = convert_file(file_pos + 2)
                possible_move.append(file_letter + str(rank_pos - 1))

        if file_pos - 2 > 0:
            if rank_pos + 1 <= 8:
                file_letter = convert_file(file_pos - 2)
                possible_move.append(file_letter + str(rank_pos + 1))
            if rank_pos - 1 > 0:
                file_letter = convert_file(file_pos - 2)
                possible_move.append(file_letter + str(rank_pos - 1))

        print(possible_move)