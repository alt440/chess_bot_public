import random
from Chessboard import *
from White import *
from Black import *

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

print("Whites")
for i in range(1,len(White.white_pieces)):
    print(White.white_pieces[i])
    print(White.white_pieces[i].moves())

print("Blacks")
for i in range(1,len(Black.black_pieces)):
    print(Black.black_pieces[i])
    print(Black.black_pieces[i].moves())

"""
Asks the user to enter his moves until checkmate (him or the other player)
"""
checkmate = False

while checkmate != True:
    x = input("Enter your next move")
    print(x)

    """
    Check in the list of moves which one is most efficient for the AI
    --Return the AI move below
    """

