import config
import pygame

from piece import *
# Import piece
# Initialize board with all pieces
# Display board

WIDTH, HEIGHT = config.windowSize

class Board:
  def __init__(self, squareSize = (WIDTH / 9), padding = (WIDTH / 18)):
    board = []
    
    self.squareSize = squareSize
    self.padding  = padding
    self.selected = None
    
    # See-through transparent square when move is available
    self.squareAvailable = pygame.Surface((squareSize, squareSize), pygame.SRCALPHA)
    pygame.draw.rect(self.squareAvailable, (255, 0, 0, 76), self.squareAvailable.get_rect())
    
    self.region = (padding, padding, WIDTH - squareSize, HEIGHT - squareSize)
    
    # Black
    Piece.isWhite = False
    
    board.append([
      Rook(0, 0),  Knight(1, 0), Bishop(2, 0), King(3, 0), 
      Queen(4, 0), Bishop(5, 0), Knight(6, 0), Rook(7, 0)
    ])
    
    board.append([])
    
    for i in range(8):
      board[1].append(Pawn(i, 1))
    
    # Empty fields
    for i in range(4):
      board.append([])
      for j in range(8):
        board[2 + i].append(None)
    
    # White
    Piece.isWhite = True
    
    board.append([])
    for i in range(8):
      board[6].append(Pawn(i, 6))
    
    board.append([
      Rook(0, 7),  Knight(1, 7), Bishop(2, 7), King(3, 7), 
      Queen(4, 7), Bishop(5, 7), Knight(6, 7), Rook(7, 7)
    ])
    
    self.board = board

  def update(self):
    pass
    
  # Draw board
  def draw(self):
    if (self.selected):
      self.drawAvailableMoves()
    
    i = 0
    for col in range(0, 8):
      for row in range(0, 8):
        posX = self.padding + (col * self.squareSize)
        posY = self.padding + (row * self.squareSize)
        
        if (i % 2 == 0):
          pygame.draw.rect(config.screen, (118, 150, 86), (posX, posY, self.squareSize, self.squareSize))
        else:
          pygame.draw.rect(config.screen, (218, 218, 190), (posX, posY, self.squareSize, self.squareSize))
        
        i += 1
      i -= 1

    # Draw pieces
    for row in self.board:
      for piece in row:
        if (piece):
          posX = self.padding + (piece.col * self.squareSize)
          posY = self.padding + (piece.row * self.squareSize)
          config.screen.blit(piece.image, (posX, posY + 2))
  
  def drawAvailableMoves(self, moves):
    for pos in moves:
      x = self.padding + (pos[0] * self.squareSize)
      y = self.padding + (pos[1] * self.squareSize)
      
      #pygame.draw.rect(config.screen, (255, 0, 0, 0.1), pygame.Rect(x, y, self.squareSize, self.squareSize))
      config.screen.blit(self.squareAvailable, (x, y))
  
  def isPositionFree(self, pos):
    col = pos[0]
    row = pos[1]
    
    return (self.board[row][col] == None)
    
  def getPiece(self, pos):
    col = pos[0]
    row = pos[1]
    
    # [row][col] since the array is [y][x]
    return self.board[row][col]
    
  def sanitizeMoves(self, piece, moves):
    i = 0
    while (i < len(moves)):
      # Check if out-of-bounds
      if (moves[i][0] < 0 or moves[i][0] > 7):
        moves.pop(i)
      elif (moves[i][1] < 0 or moves[i][1] > 7):
        moves.pop(i)
        
      # Check if position is free and if the it's a friendly piece
      elif (not self.isPositionFree(moves[i]) and piece.isFriendly(self.getPiece(moves[i]))):
        moves.pop(i)
      else:
        i += 1
        
    return moves

