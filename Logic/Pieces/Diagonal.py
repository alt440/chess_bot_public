"""
Contains methods that return the possible move for a diagonal.

There is 4 diagonals, one for each quadrant of a cartesian plan
(top-right, top-left, bottom-left, bottom-right).
"""

from Chessboard import *


def diagonal_top_right(self):
    """
    Return the possible moves for the Top Right diagonal.

    :param Piece self: Piece to get move for
    :return list diagonal: List of the moves for the Top Right diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, self.RADIUS):
        if x + i <= 8:  # Verify if out of board
            new_pos = convert_file(x + i) + str(y + i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                diagonal.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return diagonal


def diagonal_top_left(self):
    """
    Return the possible moves for the Top Left diagonal.

    :param Piece self: Piece to get move for
    :return list diagonal: List of the moves for the Top Left diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(self.position[0])#convert_file method in chessboard.py
    y = int(self.position[1])

    for i in range(1, self.RADIUS):
        if y + i <= 8 and x - i > 0:  # Verify if out of board
            new_pos = convert_file(x - i) + str(y + i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                diagonal.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return diagonal


def diagonal_bottom_left(self):
    """
    Return the possible moves for the Bottom Left diagonal.

    :param Piece self: Piece to get move for
    :return list diagonal: List of the moves for the Bottom Left diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, self.RADIUS):
        if x - i > 0:  # Verify if out of board
            new_pos = convert_file(x - i) + str(y - i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                diagonal.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return diagonal


def diagonal_bottom_right(self):
    """
    Return the possible moves for the Bottom Right diagonal.

    :param Piece self: Piece to get move for
    :return list diagonal: List of the moves for the Bottom Right diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, self.RADIUS):
        if x + i <= 8 and y - i > 0:  # Verify if out of board
            new_pos = convert_file(x + i) + str(y - i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                diagonal.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return diagonal
