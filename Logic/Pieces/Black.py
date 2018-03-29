from Bishop import *
from Knight import *
from Queen import *
from King import *
from Rook import *
from Pawn import * #NOT THERE YET


class Black():
    black_pieces = []

    @staticmethod
    def start_new_game():

        rightBlackBishop = Bishop("c8", 1)
        leftBlackBishop = Bishop("f8", 1)
        rightBlackRook = Rook("a8", 1)
        leftBlackRook = Rook("h8", 1)
        rightBlackKnight = Knight("b8", 1)
        leftBlackKnight = Knight("g8", 1)
        blackKing = King("e8", 1)
        blackQueen = Queen("d8", 1)
        Black.black_pieces = [blackKing, blackQueen, rightBlackBishop, leftBlackBishop, rightBlackKnight, leftBlackKnight,
                        rightBlackRook, leftBlackRook,
                        Pawn("a7", 1), Pawn("b7", 1), Pawn("c7", 1), Pawn("d7", 1), Pawn("e7", 1), Pawn("f7", 1),
                        Pawn("g7", 1), Pawn("h7", 1)]  # NEED TO ADD PAWNS

#all the pawns
#put them in an array. their index will serve as to the column they originate from.
#DO NOT FORGET: Index starts at 0, column starts at 1 --> decalage

#make a general array for all the pieces
#1st index (0): King
#2nd index (1): Queen
#3rd index (2): Bishop
#(3): Bishop
#(4): Knight
#(5): Knight
#(6): Rook
#(7): Rook
#(8): Pawn
#+Pawn*7 for the next 7 indexes
