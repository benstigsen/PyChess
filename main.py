import piece

pawn = piece.Pawn("black", 1, 0)
knight = piece.Knight("black", 7, 6)

chessboard = [
  ["r", "n", "b", "q", "k", "b", "n", "r"],
  ["p", "p", "p", "p", "p", "p", "p", "p"],
  [".", ".", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", ".", ".", "."],
  [".", ".", ".", ".", ".", ".", ".", "."],
  ["P", "P", "P", "P", "P", "P", "P", "P"],
  ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

def isPositionFree(pos):
  row = pos[0]
  col = pos[1]
  
  return (chessboard[row][col] == ".")

def getName(pos):
  row = pos[0]
  col = pos[1]
  
  return chessboard[row][col]

#pawn.getPossibleMoves()
print(knight.getPossibleMoves())
