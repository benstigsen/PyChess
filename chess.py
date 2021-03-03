import draw
import board
import pygame
from math import ceil
#import piece

WIDTH  = 500
HEIGHT = 500
screen = None

squareSize = WIDTH / 9
boardPadding = squareSize / 2

boardRegion = pygame.Rect(boardPadding, boardPadding, WIDTH - squareSize, HEIGHT - squareSize)

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
          row = (pos[0] - boardPadding) // squareSize
          col = (pos[1] - boardPadding) // squareSize
  
          if (row >= 0 and row < 8):
            if (col >= 0 and col < 8):
              print(row, col)
              
    
          #self.board.draw()
    #moves = self.board.getPiece((0, 1)).getPossibleMoves()
    #print(self.board.sanitizeMoves(moves))
    # Update here (input, moving)
    pass
    
  def _draw(self):
    # Draw board
    pygame.draw.rect(screen, (118, 150, 86), boardRegion)
    
    for x in range(0, 8, 2):
      for y in range(0, 8, 2):
        position = pygame.Rect(boardPadding + (x * squareSize), boardPadding + y * squareSize, squareSize, squareSize)
        pygame.draw.rect(screen, (238, 238, 210), position)
        
    for x in range(1, 8, 2):
      for y in range(1, 8, 2):
        position = pygame.Rect(boardPadding + (x * squareSize), boardPadding + y * squareSize, squareSize, squareSize)
        pygame.draw.rect(screen, (238, 238, 210), position)
    
    pygame.display.flip()
    
  def _getInput(self):
    pass
    
if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode([WIDTH, HEIGHT])
  
  game = Chess()
  game.run()

