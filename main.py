import shared
#import piece
from board import Board

shared.chessboard = Board()
shared.chessboard.draw()

#pawn = piece.Pawn("black", 1, 0)
#knight = piece.Knight("black", 7, 6)

def getName(pos):
  row = pos[0]
  col = pos[1]
  
  return chessboard[row][col]

print(shared.chessboard.board[7][6].getPossibleMoves())

#pawn.getPossibleMoves()
#print(knight.getPossibleMoves())
