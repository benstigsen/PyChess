from board import Board
import piece

chessboard = Board()
chessboard.draw()

#pawn = piece.Pawn("black", 1, 0)
#knight = piece.Knight("black", 7, 6)


def isPositionFree(pos):
  row = pos[0]
  col = pos[1]
  
  return (chessboard[row][col] == ".")

def getName(pos):
  row = pos[0]
  col = pos[1]
  
  return chessboard[row][col]

#pawn.getPossibleMoves()
#print(knight.getPossibleMoves())
