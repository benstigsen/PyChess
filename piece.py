global board

class Piece:
  def __init__(self, name, row, col, white = False):
    if (white):
      self.name = name.upper()
    else:
      self.name = name.lower()
      
    self.row = row
    self.col = col
    
    self.isWhite = white
    
    self.has_moved = False
    
  def getPosition(self):
    return (self.row, self.col)
    
  def _sanitizeMoves(self, moves):
    i = 0
    while (i < len(moves)):
      # Check if out-of-bounds
      if (moves[i][0] < 0 or moves[i][0] > 7):
        moves.pop(i)
      elif (moves[i][1] < 0 or moves[i][1] > 7):
        moves.pop(i)
      # Check if position is free (and if it's a "friendly" piece
      #elif (not isPositionFree(moves[i])):
        #moves.pop(i)
      else:
        i += 1
        
    return moves
    
  def update(self):
    pass
    
  def draw(self):
    pass
    
  #def move(self):
    #self.row = 

class King(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("K", row, col, white)

class Queen(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("Q", row, col, white)
    
class Rook(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("R", row, col, white)

class Bishop(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("B", row, col, white)

class Knight(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("N", row, col, white)
      
  def getPossibleMoves(self):
    row = self.row
    col = self.col
  
    moves = []
  
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
    
    moves = self._sanitizeMoves(moves)
    
    return moves
  
class Pawn(Piece):
  def __init__(self, row, col, white = False):
    super().__init__("P", row, col, white)
    
    # -1 for white, 1 for black
    if (white):
      self.direction = -1
    else:
      self.direction = 1
    
  def getPossibleMoves(self):    
    moves = []
    
    # Change options depending on it having moved or not
    if (self.has_moved):
      moves.append((self.row + self.direction, self.col))
    else:
      moves.append((self.row + (self.direction * 2), self.col))
      moves.append((self.row + self.direction, self.col))
      
    moves = self._sanitizeMoves(moves)
    
    return moves
    
