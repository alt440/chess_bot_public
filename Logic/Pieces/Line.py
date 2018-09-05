"""
Contains methods that return the possible move for in a line.

There is 4 lines, one for each axis and direction on a cartesian plan
(right, top, left, bottom).
"""

"""
The "blocked" methods look for protected pieces
The "attack" methods look for which opposite pieces we can attack
"""

from Chessboard import *


def line_right(self):
    """
    Returns the possible moves for the Right line.

    :param Piece self: Piece to get move for
    :return: list line: List of the moves for the Right line
    :rtype list
    """
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x + i <= 8:  # Verify if out of board
            new_pos = convert_file(x + i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                line.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return line


def line_right_blocked(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x + i <= 8:  # Verify if out of board
            new_pos = convert_file(x + i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == 1:
                break
            if pos_status == -1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_right_attack(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x + i <= 8:  # Verify if out of board
            new_pos = convert_file(x + i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == -1:
                break
            if pos_status == 1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_top(self):
    """
    Returns the possible moves for the Top line.

    :param Piece self: Piece to get move for
    :return: list line: List of the moves for the Top line
    :rtype list
    """
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y + i <= 8:  # Verify if out of board
            new_pos = convert_file(x) + str(y + i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                line.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return line


def line_top_blocked(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y + i <= 8:  # Verify if out of board
            new_pos = convert_file(x) + str(y + i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == 1:
                break
            if pos_status == -1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_top_attack(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y + i <= 8:  # Verify if out of board
            new_pos = convert_file(x) + str(y + i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == -1:
                break
            if pos_status == 1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_left(self):
    """
    Returns the possible moves for the Left line.

    :param Piece self: Piece to get move for
    :return: list line: List of the moves for the Left line
    :rtype list
    """
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x - i > 0:  # Verify if out of board
            new_pos = convert_file(x - i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                line.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return line


def line_left_blocked(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x - i > 0:  # Verify if out of board
            new_pos = convert_file(x - i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == 1:
                break
            if pos_status == -1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_left_attack(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if x - i > 0:  # Verify if out of board
            new_pos = convert_file(x - i) + str(y)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == -1:
                break
            if pos_status == 1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_bottom(self):
    """
    Returns the possible moves for the Bottom line.

    :param Piece self: Piece to get move for
    :return: list line: List of the moves for the Bottom line
    :rtype list
    """
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y - i > 0:  # Verify if out of board
            new_pos = convert_file(x) + str(y - i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status >= 0:
                line.append(new_pos)
            if pos_status != 0:
                break
        else:
            break
    return line


def line_bottom_blocked(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y - i > 0:  # Verify if out of board
            new_pos = convert_file(x) + str(y - i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == 1:
                break
            if pos_status == -1:
                line.append(new_pos)
                break
        else:
            break
    return line


def line_bottom_attack(self):
    line = []
    x = convert_file(self.position[0])
    y = int(self.position[1])

    for i in range(1, 8):
        if y - i > 0:  # Verify if out of board
            new_pos = convert_file(x) + str(y - i)
            pos_status = position_status(self, new_pos)
            # Verify if the piece can go there
            if pos_status == -1:
                break
            if pos_status == 1:
                line.append(new_pos)
                break
        else:
            break
    return line