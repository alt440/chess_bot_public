#import chessboard
#import pieces
from Chessboard import *
from Bishop import *
from Knight import *
from Queen import *
from King import *
from Rook import *

"""
Order of arrays:

"""

movesBlack = []
movesWhite = []

def addMovesForPiece(piece, king_opposite_or_null):
    """
    color: Color of the Piece: white::0, black::1
    :param piece: any piece
    :param king_opposite_or_null: if a king is passed as a parameter, add the opposite king. Otherwise, put this as null.
    :return:
    """

    if piece.COLOR == 1:
        if not piece.name == 'King':
            movesBlack.append(piece.moves())
        else:
            movesBlack.append(piece.moves(king_opposite_or_null))

    elif piece.COLOR == 0:
        if not piece.name == 'King':
            movesWhite.append(piece.moves())
        else:
            movesWhite.append(piece.moves(king_opposite_or_null))



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




def isPossibleMove(inputX):
    if inputX in list:
        return True
    else:
        return False


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

