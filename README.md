
# Chess_bot

The chess bot was attempted, but not completed. There was a limited amount of time to execute it.

Many files are only describing each pieces' possible moves. There is also the Diagonal and the Line classes that were created
because of the recurring possibilities of moves from the Bishop, the Rook, and the Queen.

The AI file is more complex, but enough comment was added so that anyone can read the code effectively.

The AI is divided into four parts:
1- Check if the king of the AI is in check and counter that with a move
2- Check if the king of the AI could be in check during the next move and counter that with a move
3- Attack if there is the possibility of capturing another piece seems advantageous
4- Defend where it seems best
5- (not added but must be done) Random move in case all else fails

The Executioner class is where the game is being launched.
When asked to put in a move, only put the initial and the final location of the piece you want to move. The program will not 
check for the validity of the move.

Note: There is an error when capturing other pieces, I did not have enough time to look into it.
