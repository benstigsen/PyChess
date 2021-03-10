import pygame
import config

images = [{}, {}]

class Piece:
  isWhite = False

  def __init__(self, name, col, row):
    if (Piece.isWhite):
      self.name = name.upper()
    else:
      self.name = name.lower()
      
    self.col = col
    self.row = row
    
    self.isWhite = Piece.isWhite
    
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
    return (self.col, self.row)
    
  def isFriendly(self, other):
    return (self.isWhite == other.isWhite)

# Check if checked
class King(Piece):
  def __init__(self, col, row):
    super().__init__("K", col, row)

  def getPossibleMoves(self):
    row = self.row
    col = self.col
    
    moves = []
    
    # Vertical
    moves.append((col, row + 1))
    moves.append((col, row - 1))
  
    # Horizontal
    moves.append((col + 1, row))
    moves.append((col - 1, row))
    
    # Diagonal
    moves.append((col + 1, row + 1))
    moves.append((col - 1, row + 1))
    moves.append((col + 1, row - 1))
    moves.append((col - 1, row - 1))
    
    return (moves, False)

# TO-DO: Get blocking pieces
class Queen(Piece):
  def __init__(self, col, row):
    super().__init__("Q", col, row)
    
  def getPossibleMoves(self):
    col = self.col
    row = self.row
    
    moves = [[], [], [], [], [], [], [], []]
    
    for i in range(1, 8):
      # Vertical
      moves[0].append((col, row - i))
      moves[1].append((col, row + i))
      
      # Horizontal
      moves[2].append((col + i, row))
      moves[3].append((col - i, row))
      
      # Diagonal
      moves[4].append((col + i, row + i))
      moves[5].append((col - i, row + i))
      moves[6].append((col + i, row - i))
      moves[7].append((col - i, row - i))
    
    return (moves, True)
    
class Rook(Piece):
  def __init__(self, col, row):
    super().__init__("R", col, row)
    
  def getPossibleMoves(self):
    col = self.col
    row = self.row
    
    moves = [[], [], [], []]
    
    for i in range(1, 8):
      # Horizontal
      moves[0].append((col, row + i))
      moves[1].append((col, row - i))
      
      # Vertical
      moves[2].append((col + i, row))
      moves[3].append((col - i, row))
    
    return (moves, True)

class Bishop(Piece):
  def __init__(self, col, row):
    super().__init__("B", col, row)
    
  def getPossibleMoves(self):
    col = self.col
    row = self.row
  
    moves = [[], [], [], []]
    
    for i in range(1, 8):
      moves[0].append((col + i, row + i))
      moves[1].append((col + i, row - i))
      moves[2].append((col - i, row + i))
      moves[3].append((col - i, row - i))
    
    return (moves, True)

class Knight(Piece):
  def __init__(self, col, row):
    super().__init__("N", col, row)
      
  def getPossibleMoves(self):
    col = self.col
    row = self.row
  
    moves = []
  
    # Up
    moves.append((col - 1, row - 2))
    moves.append((col + 1, row - 2))
    
    # Down
    moves.append((col - 1, row + 2))
    moves.append((col + 1, row + 2))
    
    # Left
    moves.append((col - 2, row - 1))
    moves.append((col + 2, row - 1))
    
    # Right
    moves.append((col - 2, row + 1))
    moves.append((col + 2, row + 1))

    return (moves, False)
  
class Pawn(Piece):
  def __init__(self, col, row):
    super().__init__("P", col, row)
    
    self.hasMoved = False
    
    # -1 for white, 1 for black
    if (self.isWhite):
      self.direction = -1
    else:
      self.direction = 1
    
  def getPossibleMoves(self):    
    moves = [[], []]
    
    # Change options depending on it having moved or not
    if (self.hasMoved):
      moves[0].append((self.col, self.row + self.direction))
    else:
      moves[0].append((self.col, self.row + self.direction))
      moves[0].append((self.col, self.row + (self.direction * 2)))
    
    # Attack
    moves[1].append((self.col - 1, self.row + self.direction))
    moves[1].append((self.col + 1, self.row + self.direction))
    
    return (moves, True)
    
