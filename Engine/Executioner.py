import random


"""
Use the game initializer method to initialize the game
"""
print("Game has been initialized")
"""
Choose at random who is white and black
"""
user_color = ""
initial_color = random.random()
if initial_color >= 0.5:
    user_color = "B"  # color is black
elif initial_color < 0.5:
    user_color = "W"  # color is white

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

