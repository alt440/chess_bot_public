from Black import *
from White import *
from Diagonal import *
from Line import *

"""
This method is used for determining which piece has access to the position. It looks into all
the diagonals and lines. Any other moves cannot be blocked and must be avoided. (Ex. Pawn and Knight)
"""


def piece_moves(index, piece_king):    # looking for the moves that we can make to block the check

    # we add the position of the piece because we can probably capture it (cond. 500 no protection)...

    if piece_king.COLOR == 1: # look for black pieces

        positions_tobe_blocked_toblockcheck = []

        if White.white_pieces[index].name is 'Queen':
            positions_tobe_blocked_toblockcheck = moves_diagonal(White.white_pieces[index], piece_king)
            if not positions_tobe_blocked_toblockcheck:
                positions_tobe_blocked_toblockcheck = moves_line(White.white_pieces[index], piece_king)

        elif White.white_pieces[index].name is 'Bishop':
            positions_tobe_blocked_toblockcheck = moves_diagonal(White.white_pieces[index], piece_king)

        elif White.white_pieces[index].name is 'Rook':
            positions_tobe_blocked_toblockcheck = moves_line(White.white_pieces[index], piece_king)

        elif White.white_pieces[index].name is 'Pawn':
            positions_tobe_blocked_toblockcheck.append(White.white_pieces[index].position)

        elif White.white_pieces[index].name is 'Knight':
            positions_tobe_blocked_toblockcheck = []

    elif piece_king.COLOR == 0:

        positions_tobe_blocked_toblockcheck = []

        if Black.black_pieces[index].name is 'Queen':
            positions_tobe_blocked_toblockcheck = moves_diagonal(Black.black_pieces[index], piece_king)
            if not positions_tobe_blocked_toblockcheck:
                positions_tobe_blocked_toblockcheck = moves_line(Black.black_pieces[index], piece_king)

        elif Black.black_pieces[index].name is 'Bishop':
            positions_tobe_blocked_toblockcheck = moves_diagonal(Black.black_pieces[index], piece_king)

        elif Black.black_pieces[index].name is 'Rook':
            positions_tobe_blocked_toblockcheck = moves_line(Black.black_pieces[index], piece_king)

        elif Black.black_pieces[index].name is 'Pawn':
            positions_tobe_blocked_toblockcheck.append(Black.black_pieces[index].position)

        elif Black.black_pieces[index].name is 'Knight':
            positions_tobe_blocked_toblockcheck = []

    return positions_tobe_blocked_toblockcheck


def moves_diagonal(piece, piece_king):
    positions_tobeBlocked_toBlockCheck = []
    if piece_king.position in diagonal_bottom_right(piece):
        positions_tobeBlocked_toBlockCheck = diagonal_bottom_right(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in diagonal_bottom_left(piece):
        positions_tobeBlocked_toBlockCheck = diagonal_bottom_left(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in diagonal_top_left(piece):
        positions_tobeBlocked_toBlockCheck = diagonal_top_left(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in diagonal_top_right(piece):
        positions_tobeBlocked_toBlockCheck = diagonal_top_right(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck


def moves_line(piece, piece_king):

    positions_tobeBlocked_toBlockCheck = []
    if piece_king.position in line_bottom(piece):
        positions_tobeBlocked_toBlockCheck = line_bottom(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in line_top(piece):
        positions_tobeBlocked_toBlockCheck = line_top(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in line_left(piece):
        positions_tobeBlocked_toBlockCheck = line_left(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
    elif piece_king.position in line_right(piece):
        positions_tobeBlocked_toBlockCheck = line_right(piece)
        positions_tobeBlocked_toBlockCheck.append(piece.position)
        return positions_tobeBlocked_toBlockCheck
