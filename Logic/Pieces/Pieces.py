from Logic.Chessboard import convert_file

"""
Parent Class for all the pieces.

Variables:
    position
    type
    value (importance of a piece)
    color
    status:
        -1: dead
        0: neutral
        1: attack
        2: attacked
        3: 1 & 2
    defence value (pieces protecting self)
    attack value (pieces attacked by self)

Method:
    move

"""
file_value = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)


class Pieces:
    # Example for black bishop (starting position)
    position = "c8"
    type = "B"
    value = 3
    color = "b"
    status = 0
    defence_value = 0
    attack_value = 0

    def __init__(self, position, piece_type, value, color):
        self.position = position
        self.type = piece_type
        self.value = value
        self.color = color

    '''
    Remove r and override it in children class instead.
    '''
    # Top Right
    def dig_top_right(self, r):
        line = []
        x = convert_file(self.position[0])
        y = int(self.position[1])

        for i in range(1, r):
            if x + i <= 8:
                line.append(convert_file(x + i) + str(y + i))
            else:
                break
        return line

    # Top Left
    def dig_top_left(self, r):
        line = []
        x = convert_file(self.position[0])
        y = int(self.position[1])

        for i in range(1, r):
            if y + i <= 8 and x - i > 0:
                line.append(convert_file(x - i) + str(y + i))
            else:
                break
        return line

    # Bottom Left
    def dig_bottom_left(self, r):
        line = []
        x = convert_file(self.position[0])
        y = int(self.position[1])

        for i in range(1, r):
            if x - i > 0:
                line.append(convert_file(x - i) + str(y - i))
            else:
                break
        return line

    # Bottom Right
    def dig_bottom_right(self, r):
        line = []
        x = convert_file(self.position[0])
        y = int(self.position[1])

        for i in range(1, r):
            if x + i <= 8 and y - i > 0:
                line.append(convert_file(x + i) + str(y - i))
            else:
                break
        return line


