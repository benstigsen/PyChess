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
    self.padding = padding
    
    self.region = pygame.Rect(
      padding, padding, WIDTH - squareSize, HEIGHT - squareSize
    )
    
    
    # Black
    Piece.isWhite = False
    
    board.append([
      Rook(0, 0),  Knight(0, 1), Bishop(0, 2), King(0, 3), 
      Queen(0, 4), Bishop(0, 5), Knight(0, 6), Rook(0, 7)
    ])
    
    board.append([])
    
    for i in range(8):
      board[1].append(Pawn(1, i))
    
    # Empty fields
    for i in range(4):
      board.append([])
      for j in range(8):
        board[2 + i].append(None)
    
    # White
    Piece.isWhite = True
    
    board.append([])
    for i in range(8):
      board[6].append(Pawn(6, i))
    
    board.append([
      Rook(7, 0),  Knight(7, 1), Bishop(7, 2), King(7, 3), 
      Queen(7, 4), Bishop(7, 5), Knight(7, 6), Rook(7, 7)
    ])
    
    self.board = board

  def update(self):
    pass
    
  def draw(self):
    # Draw board
    pygame.draw.rect(config.screen, (118, 150, 86), self.region)
    
    for x in range(0, 8, 2):
      for y in range(0, 8, 2):
        posX = self.padding + (x * self.squareSize)
        posY = self.padding + (y * self.squareSize)
        
        pygame.draw.rect(config.screen, (238, 238, 210), pygame.Rect(posX, posY, self.squareSize, self.squareSize))
        
    for x in range(1, 8, 2):
      for y in range(1, 8, 2):
        posX = self.padding + (x * self.squareSize)
        posY = self.padding + (y * self.squareSize)
        
        pygame.draw.rect(config.screen, (238, 238, 210), pygame.Rect(posX, posY, self.squareSize, self.squareSize))
  
  def isPositionFree(self, pos):
    row = pos[0]
    col = pos[1]
    
    return self.board[row][col] == None
    
  def getPiece(self, pos):
    row = pos[0]
    col = pos[1]
    
    return self.board[row][col]
    
  def sanitizeMoves(self, moves):
    i = 0
    while (i < len(moves)):
      # Check if out-of-bounds
      if (moves[i][0] < 0 or moves[i][0] > 7):
        moves.pop(i)
      elif (moves[i][1] < 0 or moves[i][1] > 7):
        moves.pop(i)
      # Check if position is free
      # TO-DO: Check if it's a friendly piece
      elif (not self.isPositionFree(moves[i])):
        moves.pop(i)
      else:
        i += 1
        
    return moves

