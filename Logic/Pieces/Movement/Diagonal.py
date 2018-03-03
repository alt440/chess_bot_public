from Logic.Chessboard import convert_file
from Logic.Pieces import Pieces


def diagonal_top_right(self, p):
    """
    Return the possible moves for the Top Right diagonal.

    :param Piece p: Piece to get move for
    :return list diagonal: List of the moves for the Top Right diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(p.position[0])
    y = int(p.position[1])

    for i in range(1, p.RADIUS):
        if x + i <= 8:
            diagonal.append(convert_file(x + i) + str(y + i))
        else:
            break
    return diagonal


def diagonal_top_left(self, p):
    """
    Return the possible moves for the Top Left diagonal.

    :param Piece p: Piece to get move for
    :return list diagonal: List of the moves for the Top Left diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(p.position[0])
    y = int(p.position[1])

    for i in range(1, p.RADIUS):
        if y + i <= 8 and x - i > 0:
            diagonal.append(convert_file(x - i) + str(y + i))
        else:
            break
    return diagonal


def diagonal_bottom_left(self, p):
    """
    Return the possible moves for the Bottom Left diagonal.

    :param Piece p: Piece to get move for
    :return list diagonal: List of the moves for the Bottom Left diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(p.position[0])
    y = int(p.position[1])

    for i in range(1, p.RADIUS):
        if x - i > 0:
            diagonal.append(convert_file(x - i) + str(y - i))
        else:
            break
    return diagonal


def diagonal_bottom_right(self, p):
    """
    Return the possible moves for the Bottom Right diagonal.

    :param Piece p: Piece to get move for
    :return list diagonal: List of the moves for the Bottom Right diagonal
    :rtype list
    """
    diagonal = []
    x = convert_file(p.position[0])
    y = int(p.position[1])

    for i in range(1, p.RADIUS):
        if x + i <= 8 and y - i > 0:
            diagonal.append(convert_file(x + i) + str(y - i))
        else:
            break
    return diagonal
