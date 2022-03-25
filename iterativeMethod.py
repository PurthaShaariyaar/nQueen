class QueenBoard: 
  # initialize board with dimensions size x size 
  def __init__(self, size):
    self.size = size 
    # initialize col[r] as columns[row] keeps track of which columns in row queen is placed 
    self.cols = []

  # place queen in next row
  def nextRow(self, col): 
    self.cols.append(col)
  
  # remove queen from current row 
  def removeCurrentRow(self): 
    return self.cols.pop()

  # check if next row is safe to place queen
  def isSafe(self, col): 
    # identify the index of the next row
    row = len(self.cols)
    
    # check if queen safe in column 
    for queenCol in self.cols:
      if col == queenCol:
        return False 
    
    # check if queen is safe in downward diagnal  
    for queenRow, queenCol in enumerate(self.cols): 
      if queenCol - queenRow == col - row: 
        return False
    
    # check if queen is safe in upward diagnol 
    for queenRow, queenCol in enumerate(self.cols): 
      if ((self.size - queenCol) - queenRow == (self.size - col) - row): 
        return False 

    return True 

  # display a queen in each safe position
  def displayQueen(self): 
    for row in range(self.size): 
      for col in range(self.size): 
        if col == self.cols[row]: 
          print('Q', end = ' ')
        else: 
          print('.', end = ' ')
      print()

def solveQueen(size): 
  # display chess board for each safe queen position based on the dimensions of the board 
  # initialize board dimensions
  board = QueenBoard(size)

  # initialize starting solution, rows and columns 
  solutions = 0; 
  row = 0
  col = 0 

  # iterate over board rows 
  while True: 
    # place queen in next row incrementally if safe in column, else increment column
    while col < size: 
      if board.isSafe(col):
        board.nextRow(col)
        row += 1 
        col = 0 
        break 
      else: 
        col += 1

    # if no column was found to place queen in or board is full 
    if (col == size or row == size): 
      # board full meaning a solution thus display solution increment solutions by 1 
      if row == size: 
        board.displayQueen()
        print()
        solutions += 1 

        # if queens already placed in rows except last at best one position in last row 
        # option to backtrack to reach second last row
        board.removeCurrentRow()
        row -= 1

      # use backtracking method 
      try: 
        prevCol = board.removeCurrentRow()
      except IndexError: 
        # break if removed all queens means no more solutions 
        break 
      
      # check previous row 
      row -= 1
      # check each column and increment column based on previous row
      col = 1 + prevCol
  
  # display total number of solutions 
  print('Number of solutions: ', solutions)

n = int(input('Enter the dimensions of the board: '))
solveQueen(n)
