import draw
import board
#import piece

class Chess:
  def __init__(self):
    self.board = board.Board()

  def run(self):
    self.board.draw()
    moves = self.board.getPiece((0, 1)).getPossibleMoves()
    print(self.board.sanitizeMoves(moves))
  
  def _update(self):
    # Update here (input, moving)
    pass
    
  def _draw(self):
    # Draw board here
    pass
    
if __name__ == "__main__":
  game = Chess()
  game.run()

