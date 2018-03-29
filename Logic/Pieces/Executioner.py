import random
from Chessboard import *
from White import *
from Black import *
from MovesCollector import *

"""
Use the game initializer method to initialize the game
"""
print("Game has been initialized")
"""
Choose at random who is white and black
"""
user_color = -1
initial_color = random.random()
if initial_color >= 0.5:
    user_color = 1  # color is black
elif initial_color < 0.5:
    user_color = 0  # color is white
print(user_color)
print("Welcome to the simulator")

White.start_new_game()
Black.start_new_game()

"""
Used to test if the right moves were allowed
"""
if user_color == 0:
    print("Whites")
    print(White.white_pieces[0].position + ' ' + White.white_pieces[0].name)
    addMovesForPiece(White.white_pieces[0], Black.black_pieces[0])
    print(White.white_pieces[0].moves(Black.black_pieces[0]))

    for i in range(1,len(White.white_pieces)):
        print(White.white_pieces[i].position + ' ' + White.white_pieces[i].name)
        print(White.white_pieces[i].moves())
        addMovesForPiece(White.white_pieces[i], None)
    print(movesWhite)

if user_color == 1:
    print("Blacks")
    print(Black.black_pieces[0].position + ' ' + Black.black_pieces[0].name)
    addMovesForPiece(Black.black_pieces[0], White.white_pieces[0])
    print(Black.black_pieces[0].moves(White.white_pieces[0]))

    for i in range(1,len(Black.black_pieces)):
        print(Black.black_pieces[i].position + ' ' + Black.black_pieces[i].name)
        print(Black.black_pieces[i].moves())
        addMovesForPiece(Black.black_pieces[i], None)
    print(movesBlack)

print("Choose a move to make. First indicate the initial position of the object and mention the new position.")
"""
Asks the user to enter his moves until checkmate (him or the other player)
"""
checkmate = False

while checkmate is not True:
    x = input("Enter your initial and next move ")
    x = x.strip()

    concerned_piece = None

    initial_position = x[:2]
    print(initial_position)
    position_piece = 'h7'
    print(position_piece in initial_position)
    position_piece = "h7"
    print(position_piece in initial_position)

    if user_color == 0:
        for i in range(len(White.white_pieces)):
            #print(White.white_pieces[i].position)
            if initial_position in White.white_pieces[i].position:
                print("TRUE")
                concerned_piece = White.white_pieces[i]
                break

    elif user_color == 1:
        for i in range(len(Black.black_pieces)):
            #print(Black.black_pieces[i].position)
            if initial_position in Black.black_pieces[i].position:
                print("TRUE")
                concerned_piece = Black.black_pieces[i]
                break

    print(concerned_piece)
    make_move(concerned_piece, x[2:4])

    if user_color == 0:
        print("Whites")
        print(White.white_pieces[0].position + ' ' + White.white_pieces[0].name)
        print(White.white_pieces[0].moves(Black.black_pieces[0]))
        for i in range(1, len(White.white_pieces)):
            print(White.white_pieces[i].position + ' ' + White.white_pieces[i].name)
            print(White.white_pieces[i].moves())
    elif user_color == 1:
        print("Blacks")
        print(Black.black_pieces[0].position + ' ' + Black.black_pieces[0].name)
        print(Black.black_pieces[0].moves(White.white_pieces[0]))
        for i in range(1, len(Black.black_pieces)):
            print(Black.black_pieces[i].position + ' ' + Black.black_pieces[i].name)
            print(Black.black_pieces[i].moves())

    """
    Check in the list of moves which one is most efficient for the AI
    --Return the AI move below
    """




