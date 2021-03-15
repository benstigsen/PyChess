import config
import pygame

from piece import *

WIDTH, HEIGHT = config.windowSize

class Board:
  def __init__(self, squareSize = (WIDTH / 9), padding = (WIDTH / 18)):
    board = []
    
    self.squareSize     = squareSize
    self.padding        = padding
    self.selectedPiece  = None
    self.availableMoves = []
    self.isWhitesTurn   = True
    
    # See-through transparent square when move is available
    self.squareAvailable = pygame.Surface((squareSize, squareSize), pygame.SRCALPHA)
    pygame.draw.rect(self.squareAvailable, (255, 0, 0, 76), self.squareAvailable.get_rect())
    
    self.region = (padding, padding, WIDTH - squareSize, HEIGHT - squareSize)
    
    # Black
    Piece.isWhite = False
    
    board.append([
      Rook(0, 0),  Knight(1, 0), Bishop(2, 0), Queen(3, 0),
      King(4, 0), Bishop(5, 0), Knight(6, 0), Rook(7, 0)
    ])
    
    # Pawns
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
    
    # Pawns
    board.append([])
    for i in range(8):
      board[6].append(Pawn(i, 6))
    
    board.append([
      Rook(0, 7),  Knight(1, 7), Bishop(2, 7), Queen(3, 7),
      King(4, 7), Bishop(5, 7), Knight(6, 7), Rook(7, 7)
    ])
    
    self.board = board
    
  # Draw chessboard
  def drawChessboard(self):
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
  
  # Draw available moves from an array/list of moves
  def drawAvailableMoves(self, moves):
    for pos in moves:
      x = self.padding + (pos[0] * self.squareSize)
      y = self.padding + (pos[1] * self.squareSize)

      config.screen.blit(self.squareAvailable, (x, y))
  
  # Draw chess pieces on the board
  def drawChessPieces(self):
    # Draw pieces
    for row in self.board:
      for piece in row:
        if (piece):
          posX = self.padding + (piece.col * self.squareSize)
          posY = self.padding + (piece.row * self.squareSize)
          config.screen.blit(piece.image, (posX, posY + 2))
  
  # Check if a specific position is free
  def isPositionFree(self, pos):
    col = pos[0]
    row = pos[1]
    
    return (self.board[row][col] == None)
  
  # Get piece from position
  def getPiece(self, pos):
    col = pos[0]
    row = pos[1]
    
    return (self.board[row][col])
  
  # Move a <piece> to <dest>
  def movePiece(self, piece, dest):
    # Pawn (special case)
    if (piece.name.lower() == "p"):
      piece.hasMoved = True
  
    col1 = piece.col
    row1 = piece.row
    
    col2 = dest[0]
    row2 = dest[1]
    
    piece.col = col2
    piece.row = row2
    
    self.board[row2][col2] = piece
    self.board[row1][col1] = None
    
    self.isWhitesTurn   = (not piece.isWhite)
    self.selected       = None
    self.availableMoves = []
  
  # Check is position is out of bounds
  def isOutOfBounds(self, pos):
    return (pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7)
  
  # Sanitize moves
  def sanitizeMoves(self, piece, moves, isStreakBasedMovement):
    # Pawn (special case)
    if (piece.name.lower() == "p"):
      sanitizedMoves = []
      if (not self.isOutOfBounds(moves[0][0]) and self.isPositionFree(moves[0][0])):
        sanitizedMoves.append(moves[0][0])
        if (not piece.hasMoved):
          if (not self.isOutOfBounds(moves[0][1]) and self.isPositionFree(moves[0][1])):
            sanitizedMoves.append(moves[0][1])
      
      # Pawn attacks
      for move in moves[1]:
        if (not self.isOutOfBounds(move)):
          if (not self.isPositionFree(move) and not piece.isFriendly(self.getPiece(move))):
            sanitizedMoves.append(move)
      
      return sanitizedMoves
    
    # Queen, Bishop, Rook
    if (isStreakBasedMovement):
      sanitizedMoves = []
      
      i = 0
      while (i < len(moves)):
        j = 0
        
        while (j < len(moves[i])):
          # Check if out-of-bounds
          if self.isOutOfBounds(moves[i][j]):
            break
          # Check if position is free and if the it's a friendly piece
          else:
            isFree = self.isPositionFree(moves[i][j])
            
            if (not isFree):
              # If the piece is not friendly, then it can be taken
              if (not piece.isFriendly(self.getPiece(moves[i][j]))):
                sanitizedMoves.append(moves[i][j])

              break
          
            sanitizedMoves.append(moves[i][j])
          j += 1
        i += 1
        
      return sanitizedMoves
    # King, Knight
    else:
      i = 0
      while (i < len(moves)):
        # Check if out-of-bounds
        if (self.isOutOfBounds(moves[i])):
          moves.pop(i)
          
        # Check if position is free and if the it's a friendly piece
        elif (not self.isPositionFree(moves[i]) and piece.isFriendly(self.getPiece(moves[i]))):
          moves.pop(i)
        else:
          i += 1
              
      return moves
    return []

