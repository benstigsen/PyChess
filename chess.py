import draw
import board
import pygame
import config
from math import ceil
#import piece

class Chess:
  def __init__(self):
    self.board = board.Board()

  def run(self):
    self.running = True
    self._draw()
    
    while self.running:
      draw = self._update()
      
      if (draw):
        self._draw()
    
    
      #_update()
      #_draw()  
  
  def _update(self):
    events = pygame.event.get()
    
    for event in events:
      self.running = (event.type != pygame.QUIT)
      
      if (event.type == pygame.MOUSEBUTTONDOWN):
        if (event.button == 1): # Left click
          pos = pygame.mouse.get_pos()
          
          # Get row and column
          col = int((pos[0] - self.board.padding) // self.board.squareSize)
          row = int((pos[1] - self.board.padding) // self.board.squareSize)
  
          if (col >= 0 and col < 8):
            if (row >= 0 and row < 8):
              print(col, row)
              print(self.board.getPiece((col, row)))
              #print(self.board.getPiece((row, col)).getPossibleMoves())
              
    
          #self.board.draw()
          #moves = self.board.getPiece((0, 1)).getPossibleMoves()
          #print(self.board.sanitizeMoves(moves))
    # Update here (input, moving)
    pass
    
  def _draw(self):
    self.board.draw()
    
    pygame.display.flip()
    
  def _getInput(self):
    pass
    
if __name__ == "__main__":
  pygame.init()
  config.screen = pygame.display.set_mode(config.windowSize)
  
  game = Chess()
  game.run()

