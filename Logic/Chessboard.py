rank = [1, 2, 3, 4, 5, 6, 7, 8]
file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
file_value = dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7)
chess_board = [[str(x) + str(y) for y in rank] for x in file]


def convert_file(f):
    if f is int:
        return file[f]
    return file_value.get(f)
