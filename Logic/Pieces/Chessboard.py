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

# Store the the location for every piece in the format {location : piece}
piece_location = dict()

"""
We could store the locations of the pieces more easily by making a 2D array
with the location being the position inside the array
"""
piece_location_chessboard_view = [[None for y in range(8)] for x in range(8)]


def convert_file(f):
    """
    Converts a file from letter to number or from number to letter.

    :param f: file to convert
    :return: Integer if f is letter, Char if f is Integer.
    """
    if isinstance(f, int):
        return file[f - 1]
    return file_value.get(f)


def position_status(self, position):
    """
    Returns if their is already a piece on the case.

    :param Piece self: Piece to verify for
    :param position: Position to be compared to
    :return: -1 if is occupied by a piece of the same color,
            0 if their is no piece,
            1 if their is a piece of the opposite color
    """

    if position in piece_location.keys():
        if piece_location[position].COLOR == self.COLOR:
            return -1
        else:
            return 1
    else:
        return 0

def add_piece_location(position, piece):
    """
    Add the position to the dictionary of piece_location
    """
    piece_location[position] = piece
    piece_location_chessboard_view[int(convert_file(position[0]))-1][int(position[1])-1] = piece

    #need to convert the position to 2 indexes for putting it into
    #the piece_location_chessboard_view 2d array
    """
    CODE STRUCTURE FOR THE REST OF THIS METHOD
    1. Divide the position into vertical and horizontal position
    2. Insert at the position the piece name into the piece_location_chessboard_view array
    """

"""
Checks if the space is available on the chessboard. The space is available to a piece if it is not of the same
color or if it is empty
"""
def is_space_available(file_pos, rank_pos, color):
    is_space_available_bool = piece_location_chessboard_view[file_pos-1][rank_pos-1] is None or \
                              not (piece_location_chessboard_view[file_pos-1][rank_pos-1].COLOR == color)
    return is_space_available_bool

"""
Makes the move considering the move is already legit.
Problem with piece: can sometimes be None??
array_moves_from_opposite_color is the array of black or white pieces. do not confuse.
"""
def make_move(piece, next_position, array_moves_from_opposite_color):
    print(piece.position+''+next_position)
    del piece_location[piece.position]
    piece_location_chessboard_view[int(convert_file(piece.position[0])) - 1][int(piece.position[1]) - 1] = None

    """
        We must also consider the removal of the other piece at that position once it has been captured
    """
    if not piece_location_chessboard_view[int(convert_file(next_position[0]))-1][int(next_position[1])-1] is None:
        array_moves_from_opposite_color.remove(piece_location_chessboard_view[int(convert_file(next_position[0]))-1][int(next_position[1])-1])

    """
        Replace the position by the actual piece that goes there (the one we are moving)
    """
    piece.position = next_position
    piece_location[next_position] = piece
    piece_location_chessboard_view[int(convert_file(next_position[0]))-1][int(next_position[1])-1] = piece



