#import chessboard
#import pieces
from Logic.Chessboard import *
from Logic.Pieces.Bishop import *
from Logic.Pieces.Knight import *
from Logic.Pieces.Queen import *
from Logic.Pieces.King import *
from Logic.Pieces.Rook import *



movesBlack = ()
movesWhite = ()

"""
This is what the code should look like, even if it is not the right methods right now
"""
def getAllMoves(previous_position_moved_piece, color):

    if color == 0: # if white
        #only need to remove the previous position of the piece before the last move. Otherwise, the rest of the list stays the same
        if not movesWhite: # if list is empty, fill it out
            for i in range(len(white_pieces)):
                movesWhite.append(white_pieces[i].moves())
        else: #here remove only the previous position of the piece
            for i in range(len(white_pieces)):
                if previous_position_moved_piece[0] == movesWhite[i][0]: #not sure




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
        if x_position_king == array[i][0] && y_position_king == array[i][1]:
            return True

    return False

