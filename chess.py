import board
import pygame
import config
from math import ceil
#import piece

class Chess:
  def __init__(self):
    self.board = board.Board()
    self.drawQueue = [[self.board.drawChessboard], [self.board.drawChessPieces]]
  
  # Run (start game)
  def run(self):
    self.running = True
    draw = True
    
    # Run loop
    while self.running:
      if (draw):
        self._draw()
        
      draw = self._update()
  
  # Update (events, positions, moves, draw queue)
  def _update(self):
    events = pygame.event.get()
    
    for event in events:
      self.running = (event.type != pygame.QUIT)
      
      # On Mouse Click
      if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1):
          pos = pygame.mouse.get_pos()
          
          # Get row and column
          col = int((pos[0] - self.board.padding) // self.board.squareSize)
          row = int((pos[1] - self.board.padding) // self.board.squareSize)
  
          if (col >= 0 and col < 8):
            if (row >= 0 and row < 8):
              piece = self.board.getPiece((col, row))
              
              if (piece):
                self.board.selectedPiece = piece
                
                moves, isStreakBasedMovement = piece.getPossibleMoves()
                moves = self.board.sanitizeMoves(piece, moves, isStreakBasedMovement)
                
                self.board.availableMoves = moves
                
                self.drawQueue.append([self.board.drawChessboard])
                self.drawQueue.append([self.board.drawAvailableMoves, moves])
                self.drawQueue.append([self.board.drawChessPieces])
              else:
                if (self.board.selectedPiece):
                  piece = self.board.selectedPiece
                  if ((col, row) in self.board.availableMoves):
                    self.board.movePiece(piece, (col, row))
                  else:
                    self.board.selectedPiece = None
                    self.board.availableMoves = None
                    
                self.drawQueue.append([self.board.drawChessboard])
                self.drawQueue.append([self.board.drawChessPieces])
                
              return True
                
    return False
    
  def _draw(self):
    for item in self.drawQueue:
      if (len(item) == 1):
         item[0]()
      else:
        item[0](*item[1:])
        
    pygame.display.flip()
    
if __name__ == "__main__":
  pygame.init()
  config.screen = pygame.display.set_mode(config.windowSize)
  
  game = Chess()
  game.run()

