#import chessboard
#import pieces
from Chessboard import *
from AI import *

"""
Order of arrays:
0: KING
1: QUEEN
2: BISHOP
3: BISHOP
4: KNIGHT
5: KNIGHT
6: ROOK
7: ROOK
8: PAWN A
9: PAWN B
10: PAWN C
11: PAWN D
12: PAWN E
13: PAWN F
14: PAWN G
15: PAWN H
These are the first indexes of the 2d arrays. The length of the 2nd dimension depends on how many moves are available.
"""

movesBlack = []
movesWhite = []

def addMovesForPieces(array_pieces, king_opposite_or_null, user_color):
    """
    color: Color of the Piece: white::0, black::1
    :param array_pieces: the array of pieces (black or white)
    :param king_opposite_or_null: if a king is passed as a parameter, add the opposite king. Otherwise, put this as null.
    :param user_color: to print the info important to the user
    :return:
    """

    #transfer used moves to previousMoves arrays

    if array_pieces[0].COLOR == 1:
        del movesBlack[:]
        if user_color == 1:
            for i in range(len(array_pieces)):
                if not array_pieces[i].name == 'King':
                    print(array_pieces[i].position + ' ' + array_pieces[i].name)
                    print(array_pieces[i].moves())
                    movesBlack.append(array_pieces[i].moves())
                else:
                    print(array_pieces[i].position + ' ' + array_pieces[i].name)
                    print(array_pieces[i].moves(king_opposite_or_null))
                    movesBlack.append(array_pieces[i].moves(king_opposite_or_null))
        else:
            for i in range(len(array_pieces)):
                if not array_pieces[i].name == 'King':
                    movesBlack.append(array_pieces[i].moves())
                else:
                    movesBlack.append(array_pieces[i].moves(king_opposite_or_null))

    elif array_pieces[0].COLOR == 0:
        del movesWhite[:]
        if user_color == 0:
            for i in range(len(array_pieces)):
                if not array_pieces[i].name == 'King':
                    print(array_pieces[i].position + ' ' + array_pieces[i].name)
                    print(array_pieces[i].moves())
                    movesWhite.append(array_pieces[i].moves())
                else:
                    print(array_pieces[i].position + ' ' + array_pieces[i].name)
                    print(array_pieces[i].moves(king_opposite_or_null))
                    movesWhite.append(array_pieces[i].moves(king_opposite_or_null))
        else:
            for i in range(len(array_pieces)):
                if not array_pieces[i].name == 'King':
                    movesWhite.append(array_pieces[i].moves())
                else:
                    movesWhite.append(array_pieces[i].moves(king_opposite_or_null))
            AI.classify_moves(movesBlack, movesWhite, 0)



"""
This is what the code should look like, even if it is not the right methods right now
"""
def getAllMoves(previous_position_moved_piece, color):
    """
    if color == 0: # if white
        #only need to remove the previous position of the piece before the last move. Otherwise, the rest of the list stays the same
        if not movesWhite: # if list is empty, fill it out
            for i in range(len(white_pieces)):
                movesWhite.append(white_pieces[i].moves())
        else: #here remove only the previous position of the piece
            for i in range(len(white_pieces)):
                if previous_position_moved_piece[0] == movesWhite[i][0]: #not sure
    """
    return 0

def is_check(opposite_king, new_position, old_position, piece_moved):
    """
    This is the class where we collect the moves, thus I thought it appropriate to look at the last move and find
    if it puts the other king in chess.
    Last move contains the new position, old position, and the piece moved
    :param opposite_king:
    :return:
    """

    #getting the possible moves of the piece from its new position
    array = piece_moved.moves()

    x_position_king =convert_file(self.position[0])
    y_position_king = int(self.position[1])

    for i in range(len(array)):
        if x_position_king == array[i][0] and y_position_king == array[i][1]:
            return True

    return False

