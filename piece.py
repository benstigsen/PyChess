import pygame
import config

images = [{}, {}]

class Piece:
  isWhite = False

  def __init__(self, name, row, col):
    if (Piece.isWhite):
      self.name = name.upper()
    else:
      self.name = name.lower()
      
    self.row = row
    self.col = col
    
    self.hasMoved = False
    self.isWhite = Piece.isWhite
    #print(self.name)
    
    # Load white and black pieces
    if (self.isWhite):
      if (name.lower() in images[0]):
        self.image = images[0][name.lower()]
      else:
        self.image = pygame.image.load(f"assets/img/{name.lower()}.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        self.image.fill((255, 255, 255, 0), None, pygame.BLEND_RGBA_ADD)
        
        images[0][name.lower()] = self.image
    else:
      if (name.lower() in images[1]):
        self.image = images[1][name.lower()]
      else:
        self.image = pygame.image.load(f"assets/img/{name.lower()}.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        images[1][name.lower()] = self.image
    
  def getPosition(self):
    return (self.row, self.col)

class King(Piece):
  def __init__(self, row, col):
    super().__init__("K", row, col)

  def getPossibleMoves(self):
    row = self.row
    col = self.col
    
    moves = []
    
    # Vertical
    moves.append((row + 1, col))
    moves.append((row - 1, col))
  
    # Horizontal
    moves.append((row, col + 1))
    moves.append((row, col - 1))
    
    # Diagonal
    moves.append((row + 1, col + 1))
    moves.append((row + 1, col - 1))
    moves.append((row - 1, col + 1))
    moves.append((row - 1, col - 1))
    
    return moves

# TO-DO: Get blocking pieces
class Queen(Piece):
  def __init__(self, row, col):
    super().__init__("Q", row, col)
    
  def getPossibleMoves(self):
    row = self.row
    col = self.col
    
    moves = []
    
    for i in range(1, 8):
      # Vertical
      moves.append((row - i, col))
      moves.append((row + i, col))
      
      # Horizontal
      moves.append((row, col + i))
      moves.append((row, col - i))
      
      # Diagonal
      moves.append((row + i, col + i))
      moves.append((row + i, col - i))
      moves.append((row - i, col + i))
      moves.append((row - i, col - i))
    
    return moves
    
class Rook(Piece):
  def __init__(self, row, col):
    super().__init__("R", row, col)

class Bishop(Piece):
  def __init__(self, row, col):
    super().__init__("B", row, col)

class Knight(Piece):
  def __init__(self, row, col):
    super().__init__("N", row, col)
      
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

    return moves
  
class Pawn(Piece):
  def __init__(self, row, col):
    super().__init__("P", row, col)
    
    # -1 for white, 1 for black
    if (self.isWhite):
      self.direction = -1
    else:
      self.direction = 1
    
  def getPossibleMoves(self):    
    moves = []
    
    # Change options depending on it having moved or not
    if (self.hasMoved):
      moves.append((self.row + self.direction, self.col))
    else:
      moves.append((self.row + (self.direction * 2), self.col))
      moves.append((self.row + self.direction, self.col))
    
    return moves
    
