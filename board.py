from piece import *
# Import piece
# Initialize board with all pieces
# Display board

class Board:
  def __init__(self):
    board = []
    
    # Black
    board.append(
      [Pawn(0, 0), Knight(0, 1), Pawn(0, 2), Pawn(0, 3), Pawn(0, 4), Pawn(0, 5), Knight(0, 6), Pawn(0, 7)])
    
    board.append([])
    
    for i in range(8):
      board[1].append(Pawn(1, i))
    
    # Empty fields
    for i in range(4):
      board.append([])
      for j in range(8):
        board[2 + i].append(None)
    
    # White
    board.append([])
    for i in range(8):
      board[6].append(Pawn(6, i, True))
    
    board.append(
      [Pawn(0, 0), Knight(0, 1), Pawn(0, 2), Pawn(0, 3), Pawn(0, 4), Pawn(0, 5), Knight(0, 6), Pawn(0, 7)]
    )
    
    self.board = board

  def update(self):
    pass
    
  def draw(self):
    for row in self.board:
      for col in row:
        if (col):
          print(f"{col.name}, ", end="")
        else:
          print("., ", end="")
      
      print("\n")
    #pprint(self.board)
    pass

