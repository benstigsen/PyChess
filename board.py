from piece import *
# Import piece
# Initialize board with all pieces
# Display board

class Board:
  def __init__(self):
    board = []
    
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
    for row in self.board:
      for col in row:
        if (col):
          print(f"{col.name}, ", end="")
        else:
          print("., ", end="")
      
      print("\n")
    #pprint(self.board)
    pass

