from Bishop import *
from Knight import *
from Queen import *
from King import *
from Rook import *
from Pawn import *
#from Logic.Pieces.Pawn import * NOT THERE YET

class White():
    white_pieces=[]

    @staticmethod
    def start_new_game():
        rightWhiteBishop = Bishop("c1", 0)
        leftWhiteBishop = Bishop("f1", 0)
        rightWhiteRook = Rook("a1", 0)
        leftWhiteRook = Rook("h1", 0)
        rightWhiteKnight = Knight("b1", 0)
        leftWhiteKnight = Knight("g1", 0)
        whiteKing = King("e1", 0)
        whiteQueen = Queen("d1", 0)
        White.white_pieces = [whiteKing, whiteQueen, rightWhiteBishop, leftWhiteBishop, rightWhiteKnight, leftWhiteKnight,
                        rightWhiteRook, leftWhiteRook,
                        Pawn("a2", 0), Pawn("b2", 0), Pawn("c2", 0), Pawn("d2", 0), Pawn("e2", 0), Pawn("f2", 0),
                        Pawn("g2", 0), Pawn("h2", 0)]
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
