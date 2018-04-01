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
        # contains spaces that can be protected with next move. Same concept as movesCollector (indexes same)
        protection_array = []
        # we put the sum of inversely points given to pieces at each position in the protection array
        protection_array_values = [[0 for y in range(8)] for x in range(8)]

        # contains the spaces where we can reach for enemy pieces
        attack_array = [[0 for y in range(8)] for x in range(8)]
        # we put the sum of points given to pieces at each position in the attack_array
        attack_array_values = [[0 for y in range(8)] for x in range(8)]

        # contains information as to how much pieces are protected. Only information will be the number
        # of pieces that protect some piece. It will help determining if attacking is worth it.
        protection_all_pieces = [[0 for y in range(8)] for x in range(8)]
        # do the same for our pieces


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

        """
            The AI can attack and defend with the best possible moves. However, it does not know how to reply to attacks
            to the king, (avoiding checkmate) and when attacked, it must find a way to protect its pieces if left alone
            and/or counterattack or put another piece in the way that would make the AI lose less valuable assets.
        
        """


        if colorAI == 0:
            # White
            for i in range(len(white_pieces_moves)):
                # look at the position and inspect surroundings
                if White.white_pieces[i].name is 'Pawn':
                    protection_array.append(White.white_pieces[i].checking_diagonals())
                else:
                    protection_array.append(white_pieces_moves[i])

            # array populated. doing points
            AI.max_value = 0
            for i in range(len(protection_array)):
                # remove the index that is the piece's possible moves for protection (decrease by 1 the occurence of the
                # position, only for other than pawn) For now, no
                if White.white_pieces[i].name is 'King':
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 1)

                elif White.white_pieces[i].name is 'Queen':
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 2)

                elif White.white_pieces[i].name is 'Bishop' or White.white_pieces[i].name is 'Knight':
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 5)

                elif White.white_pieces[i].name is 'Rook':
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 3)

                elif White.white_pieces[i].name is 'Pawn':
                    AI.add_piece_value_to_protection_array_values(i, protection_array,
                                                                  protection_array_values, 9)

            # Checkpoint: Protection array and protection array values completed.

            # filling the protection_enemy_pieces array
            for i in range(len(Black.black_pieces)):
                protected_enemy_pieces = Black.black_pieces[i].moves_blocked()
                for j in range(len(protected_enemy_pieces)):
                    row = int(convert_file(protected_enemy_pieces[j][0]))-1
                    column = int(protected_enemy_pieces[j][1])-1  # do -1 bc starts at 1
                    protection_all_pieces[row][column] += 1

            # filling the protection_ally_pieces array
            for i in range(len(White.white_pieces)):
                protected_ally_pieces = White.white_pieces[i].moves_blocked()
                for j in range(len(protected_ally_pieces)):
                    row = int(convert_file(protected_ally_pieces[j][0]))-1
                    column = int(protected_ally_pieces[j][1])-1  # do -1 bc starts at 1
                    protection_all_pieces[row][column] -= 1

            # checking for unprotected pieces: will have the value 500 and -500
            for i in range(len(White.white_pieces)):
                position = White.white_pieces[i].position
                row = int(convert_file(position[0])) - 1
                column = int(position[1]) - 1  # do -1 bc starts at 1
                if protection_all_pieces[row][column] == 0:
                    protection_all_pieces[row][column] -= 500

            for i in range(len(Black.black_pieces)):
                position = Black.black_pieces[i].position
                row = int(convert_file(position[0])) - 1
                column = int(position[1]) - 1  # do -1 bc starts at 1
                if protection_all_pieces[row][column] == 0:
                    protection_all_pieces[row][column] += 500

            print("ENEMY PROTECTION (USER PROTECTION)")
            for i in range(8):
                print(protection_all_pieces[i])

            print("END")

            # Checkpoint: Make the attack table
            # I need all the possible attack moves. Integer put on the position the piece is attacking (depending on
            # number of pieces that will protect it when it moves to attack the piece)
            # to find out if pieces can protect, number at position > 1.
            attack_array_pieces_all = []
            for i in range(len(White.white_pieces)):
                attack_array_pieces = (White.white_pieces[i].moves_attack())
                attack_array_pieces_all.append(White.white_pieces[i].moves_attack())
                for j in range(len(attack_array_pieces)):
                    row = int(convert_file(attack_array_pieces[j][0])) - 1
                    column = int(attack_array_pieces[j][1]) - 1  # do -1 bc starts at 1
                    print(str(attack_array_pieces[j][0])+str(column+1)+' position at which we move with '+White.white_pieces[i].name+' at '+White.white_pieces[i].position)
                    attack_array[row][column] += 1

            print("ATTACK ARRAY")
            for i in range(8):
                print(attack_array[i])
            print("END")

            # attack or protect??
            # first look at attack. can it attack and win?
            has_move = False
            for i in range(8):
                for j in range(8):
                    if attack_array[i][j] != 0 and not has_move:
                        # check the protection on the other side.
                        if attack_array[i][j] > protection_all_pieces[i][j] or protection_all_pieces[i][j] == 500:
                            # find the piece that can attack and make the move
                            # if pieces, find the one with the lesser value to place there
                            row = convert_file(i+1)
                            column = j+1
                            position = row+str(column)
                            pieces_that_can_attack = []
                            for k in range(len(White.white_pieces)):
                                for l in range(len(attack_array_pieces_all[k])):
                                    print(attack_array_pieces_all[k][l]+' and '+position+' are the two compared strings')
                                    if attack_array_pieces_all[k][l][0] is position[0] and attack_array_pieces_all[k][l][1] is position[1]:
                                        pieces_that_can_attack.append(White.white_pieces[k])
                                        print(White.white_pieces[k].name)

                            # find piece with lesser value
                            min = 150
                            piece = None
                            for i in range(len(pieces_that_can_attack)):
                                if pieces_that_can_attack[i].VALUE < min:
                                    min = pieces_that_can_attack[i].VALUE
                                    piece = pieces_that_can_attack[i]

                            # make the move and exit
                            if piece is not None:
                                print('AI attacks to '+position+' with piece at '+piece.position)
                                print(piece.position+position)
                                make_move(piece, position, Black.black_pieces)
                                has_move = True


            # to quit the loop when the move has been made, because we do not need to search for another move anymore
            skip = has_move

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
                            # as this value will decrease because pieces are being eaten, then we put size of array
                            k = len(White.white_pieces)-1
                            while k >= 0 and not skip:
                                # print (str(k)+' index for error')
                                if white_pieces_moves[k] is not None:
                                    for l in range(len(white_pieces_moves[k])):
                                        if white_pieces_moves[k][l] == position:
                                            # take piece and make move
                                            print("Piece "+White.white_pieces[k].name+" moves to "+position)
                                            print(White.white_pieces[k].position+position)
                                            make_move(White.white_pieces[k], position, Black.black_pieces)
                                            skip = True
                                            break
                                    k -= 1

                    if i == 7 and j == 7 and not skip:
                        while AI.max_value not in protection_array_values and AI.max_value >= 0:
                            AI.max_value -= 1 # decrease until another possible value in the array is encountered.

        return 0

    @staticmethod
    def add_piece_value_to_protection_array_values(i, protection_array, protection_array_values, value_added):
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
