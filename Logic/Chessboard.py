rank = [1, 2, 3, 4, 5, 6, 7, 8]
file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
file_value = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
chess_board = [[str(x) + str(y) for y in rank] for x in file]

# How a return position could work
def getRank():
    return rank

def getFile():
    return file

def getPostion():
    return [getFile(), getRank()]

# With this position can check the status of every positioj on the board
def isOccupied(rank, file):
    return (getRank() == rank and getFile() == file)


def printChess():
    print(chess_board)

def convert_file(f):
    if isinstance(f, int):
        return file[f-1]
    return file_value.get(f)

