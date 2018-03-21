from Rules.Chessboard import convert_file
from Pieces.Chessboard import*

class Pawn(Pieces):
      def __init__(self, position, color):
          Pieces.__init__(self, position, color,"P")
#Firstly, taking in consideration all possible moves.
      def moves(self):
           moves = list()
           file_pos = int(convert_file(self.position[0]))
           rank_pos = int(self.position[1]) #raw

           if self.COLOR == 0 and rank_pos == 2: #white
               moves.append(convert_file(file_pos) + str(rank_pos + 2))

           elif rank_pos == 7 and self.COLOR == 1: #black
                moves.append(convert_file(file_pos)+str(rank_pos-2))

           if self.COLOR == 0:
               moves.append(convert_file(file_pos) + str(rank_pos + 1))

           elif self.COLOR == 1:
               moves.append(convert_file(file_pos) + str(rank_pos - 1))

           

           """
                      elif (FirstMove.neg() or self.COLOR == 0):
                if  (rank_pos +1 <= 8):
                    if rank_pos +1 > 8:
                    #Something will happen here
                    #creat a method
                    elif rank_pos + 1 <=8:
                        moves.append(convert_file(file_pos)+str(rank_pos+1))
           elif (FirstMove.neg() or self.COLOR == 1):
                if  (rank_pos -1 <= 0):
                    if rank_pos -1 > 0:
                    #Something will happen here
                    #creat a method
                    elif rank_pos - 1 <=0:
                        moves.append(convert_file(file_pos)+str(rank_pos-1))
           """

           return moves











