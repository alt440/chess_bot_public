from MovesCollector import *
from White import *
from Black import *
from Chessboard import *

class AI():
    """
movesAI will contain second level moves. That is, moves that would be available after one move has been made.
It will try every type of move from the original array, and evaluate them with a system of points. The most points
a move has, the most convenient it is to make that move.
    """
    movesAI = []
    moves_points = []

    max_value = 0

    @staticmethod
    def classify_moves(black_pieces_moves, white_pieces_moves, colorAI):
        """
    color: Color of the Piece: white::0, black::1
    :return:
        """

        """
    We will need to analyze every move from our color. Then, for each possible
    move we need to know which pieces it protects, and which pieces can attack it
    from the opposite team. We must also know which pieces it can attack because they are undefended.
    
    We must be able to predict the player's move by predicting all his next possible moves.
    That will be done later.
        """

        """
    To know if a piece is protected when going somewhere on the board, we will look at the occurence
    of the position in the array of moves, because if pieces can get there, they can protect other pieces.
    However, that is not the case for Pawns, which is why there is a method "check_diagonals" in the Pawn 
    class. We will use that method to replace every possible moves of the pawns and put that instead.
    
    Exception : We want the King unprotected. We simply want it to be covered, so for the King these rules
    do not apply.
        """

        """
    The points given for protection will be inversely set. Meaning, if a queen protects a pawn, less points 
    would be attributed than if a rook protects a pawn. Thus, the pawn being the protection will give the 
    most points.
    This goes opposite when attacking. When attacking, the highest points go for attacking the queen or putting
    the King in check, instead of capturing a pawn.
        """
        #contains spaces that can be protected with next move. Same concept as movesCollector (indexes same)
        protection_array = []
        #we put the sum of inversely points given to pieces at each position in the protection array
        protection_array_values = [[0 for y in range(8)] for x in range(8)]

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


        if colorAI == 0:
            #White
            for i in range(len(white_pieces_moves)):
                #look at the position and inspect surroundings
                if i > 7:
                    protection_array.append(White.white_pieces[i].checking_diagonals())
                else:
                    protection_array.append(white_pieces_moves[i])

            #array populated. doing points
            AI.max_value = 0
            for i in range(len(protection_array)):
                #remove the index that is the piece's possible moves for protection (decrease by 1 the occurence of the position, only for other than pawn) For now, no
                if i == 0:
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 1, AI.max_value)

                elif i == 1:
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 2, AI.max_value)

                elif i >= 2 and i <= 5:
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 5, AI.max_value)

                elif i== 6 or i == 7:
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 3, AI.max_value)

                elif i > 7:
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 9, AI.max_value)

            #so one of the pieces going at these positions will get protected

            #to quit the loop when the move has been made, because we do not need to search for another move anymore
            skip = False

            for i in range(8):
                print(protection_array_values[i])

            while AI.max_value >= 0 and not skip:
                for i in range(8):
                    for j in range(8):
                        if protection_array_values[i][j] == AI.max_value and not skip:
                            position = str(convert_file(i+1))+str(j+1)
                            print(position)
                            print(str(protection_array_values[i][j])+' '+str(AI.max_value)+' values compared')
                            print("OK")
                            """
                            if position in white_pieces_moves:
                                print("OK")
                                #find the origin, then break from this whole loop
                                #start from end of loop with pawns, as they are preferred.
                            """
                            k = 15
                            while k >= 0 and not skip:
                                for l in range(len(white_pieces_moves[k])):
                                    if white_pieces_moves[k][l] == position:
                                        #take piece and make move
                                        print("Piece "+White.white_pieces[k].name+" moves to "+position)
                                        make_move(White.white_pieces[k], position, Black.black_pieces)
                                        skip = True
                                        break
                                k-=1


                    if i == 7 and j == 7 and not skip:
                        while AI.max_value not in protection_array_values and AI.max_value >= 0:
                            AI.max_value -= 1 #decrease until another possible value in the array is encountered.

        return 0

    @staticmethod
    def add_piece_value_to_protection_array_values(i, protection_array, protection_array_values, value_added, max_value):
        for j in range(len(protection_array[i])):
            row = int(convert_file(protection_array[i][j][0]))-1
            column = int(protection_array[i][j][1])-1
            protection_array_values[row][column] += value_added
            if protection_array_values[row][column] > AI.max_value:
                AI.max_value = protection_array_values[row][column]
        return 0


"""
#should include the looking ahead of 2 moves
def AImove(color):
    # get the right list of moves from the color indicated

    #say it is this list
    listOfMoves = MovesCollector.list

    listPoints_position_piece = () #should find a way to indicate the points attributed to the move, the position it lands on and the piece moved in the array
    for i in range(1,len(listOfMoves)):
        if notProtected && attacked:
            -infinity

        elif notProtected but attacks: # if it attacks the other player
            positive near 0

        elif Protected && attacked:
            if nbPiecesProtect> nbPiecesAttack:
                positive near 0
            else:
                negative near 0
"""
