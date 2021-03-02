import piece

test = piece.Pawn("black", 1, 0)

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

def getPossibleMoves(pos):
  row = pos[0]
  col = pos[1]
  
  moves = []
  
  # N
  if (chessboard[row][col] == "N"):
    # Up
    moves.append((row - 2, col - 1))
    moves.append((row - 2, col + 1))
    
    # Down
    moves.append((row + 2, col - 1))
    moves.append((row + 2, col + 1))
    
    # Left
    moves.append((row - 1, col - 2))
    moves.append((row - 1, col + 2))
    
    # Right
    moves.append((row + 1, col - 2))
    moves.append((row + 1, col + 2))

test.getPossibleMoves()
