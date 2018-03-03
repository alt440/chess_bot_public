"""
Used to represent the chessboard.

Only for mapping Pieces to their position,
does not contain any information about the current game.
"""

rank = [1, 2, 3, 4, 5, 6, 7, 8]  # Rank number
file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # File letter
file_value = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)  # Map the file letter to number

# Create all the chessboard position in format ("File"+"Rank")
chess_board = [[str(x) + str(y) for y in rank] for x in file]


def convert_file(f):
    """
    Converts a file from letter to number or from number to letter.

    :param f: file to convert
    :return: Integer if f is letter, Char if f is Integer.
    """
    if isinstance(f, int):
        return file[f - 1]
    return file_value.get(f)
