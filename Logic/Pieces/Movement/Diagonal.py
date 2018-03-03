"""
Contains methods that return the possible move for a diagonal.

There is 4 diagonals, one for each quadrant of a cartesian plan
(top-right, top-left, bottom-left, bottom-right).
"""

from Logic.Chessboard import convert_file


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
        if x + i <= 8:
            diagonal.append(convert_file(x + i) + str(y + i))
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
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, self.RADIUS):
        if y + i <= 8 and x - i > 0:
            diagonal.append(convert_file(x - i) + str(y + i))
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
        if x - i > 0:
            diagonal.append(convert_file(x - i) + str(y - i))
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
        if x + i <= 8 and y - i > 0:
            diagonal.append(convert_file(x + i) + str(y - i))
        else:
            break
    return diagonal