from Pieces import *
from Chessboard import *

class King(Pieces):
    """
    Represent the pieces of type King.
    """
    name = 'King'

    def __init__(self, position, color):
        """
        Create a King Based on the Piece class.

        :param position: Position on the chessboard
        :param color: Color of hte Piece: white::0, black::1
        """
        Pieces.__init__(self, position, color,"K")
        add_piece_location(position, self)

    def moves(self, kingOpposite):
        """
        Returns the list of possible moves for the King.
        The King opposite parameter will be put with the tables of White and Black that easily refer to it.

        :return: List of possible moves
        :rtype list
        """

        moves = list()  # List of possible moves
        file_pos = int(convert_file(self.position[0])) #letters: Columns
        rank_pos = int(self.position[1]) #rows

        """
        opposite king position
        kingOpposite=None
        for i in piece_location:
            if piece_location[i].__name__ =='King' and not piece_location[i].COLOR == self.COLOR:
                kingOpposite=piece_location[i]
        """
        file_pos_opposite = int(convert_file(kingOpposite.position[0]))
        rank_pos_opposite = int(kingOpposite.position[1])

        """
        Check for all the position where the King could go.
        """
        if file_pos+1 <= 8:
            if rank_pos+1 <= 8:
                moves.append(convert_file(file_pos+1)+str(rank_pos+1))
            if rank_pos-1 >= 0:
                moves.append(convert_file(file_pos+1)+str(rank_pos-1))

            moves.append(convert_file(file_pos+1)+str(rank_pos))

        if file_pos-1 >= 0:
            if rank_pos+1 <= 8:
                moves.append(convert_file(file_pos-1)+str(rank_pos+1))
            if rank_pos-1 >= 0:
                moves.append(convert_file(file_pos-1)+str(rank_pos-1))

            moves.append(convert_file(file_pos-1)+str(rank_pos))

        if rank_pos+1 <= 8:

            moves.append(convert_file(file_pos)+str(rank_pos+1))

        if rank_pos-1 >= 0:

            moves.append(convert_file(file_pos)+str(rank_pos-1))

        """
        Check the positions that could be in sync with opposite king (not available moves)
        """
        moves_opposite = list()
        if file_pos_opposite+1 <= 8:
            if rank_pos_opposite+1 <= 8:
                moves_opposite.append(convert_file(file_pos_opposite+1)+str(rank_pos_opposite+1))
            if rank_pos_opposite-1 >= 0:
                moves_opposite.append(convert_file(file_pos_opposite+1)+str(rank_pos_opposite-1))

            moves_opposite.append(convert_file(file_pos_opposite+1)+str(rank_pos_opposite))

        if file_pos_opposite-1 >= 0:
            if rank_pos_opposite+1 <= 8:
                moves_opposite.append(convert_file(file_pos_opposite-1)+str(rank_pos_opposite+1))
            if rank_pos_opposite-1 >= 0:
                moves_opposite.append(convert_file(file_pos_opposite-1)+str(rank_pos_opposite-1))

            moves_opposite.append(convert_file(file_pos_opposite-1)+str(rank_pos_opposite))

        if rank_pos_opposite+1 <= 8:

            moves_opposite.append(convert_file(file_pos_opposite)+str(rank_pos_opposite+1))

        if rank_pos_opposite-1 >= 0:

            moves_opposite.append(convert_file(file_pos_opposite)+str(rank_pos_opposite-1))


        moves_answer = list()
        for x in range(len(moves)):
            for y in range(len(moves_opposite)):    #this code is not performant...
                if moves[x] == moves_opposite[y]:
                    break
                if y == len(moves_opposite)-1:
                    moves_answer.append(moves[x])

        return moves_answer



