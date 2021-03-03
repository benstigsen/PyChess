import draw
import board
import pygame
#import piece

screen = None

squareSize = 55

class Chess:
  def __init__(self):
    self.board = board.Board()

  def run(self):
    self.running = True
    
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
          
          row = pos[0] // squareSize
          col = pos[1] // squareSize
  
          self.board.draw()
    #moves = self.board.getPiece((0, 1)).getPossibleMoves()
    #print(self.board.sanitizeMoves(moves))
    # Update here (input, moving)
    pass
    
  def _draw(self):
    # Draw board
    pygame.draw.rect()
    pass
    
  def _getInput(self):
    pass
    
if __name__ == "__main__":
  pygame.init()
  screen = pygame.display.set_mode([500, 500])
  
  game = Chess()
  game.run()

