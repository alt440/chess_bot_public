from MovesCollector import *

"""
movesAI will contain second level moves. That is, moves that would be available after one move has been made.
It will try every type of move from the original array, and evaluate them with a system of points. The most points
a move has, the most convenient it is to make that move.
"""
movesAI = []
moves_points = []

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

    if colorAI == 0:
        #White
        for i in range(len(white_pieces_moves)):
            #look at the position and inspect surroundings



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
