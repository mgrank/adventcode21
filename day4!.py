numbers = []
boards = []
boardSize = 5

def readBoard(f):
  board = []
  for i in range(boardSize):
    bline = f.readline()
    if not bline:
      break
    board.append( [int(num) for num in bline.split()] )

  f.readline()
  return board

def checkBoardWin(mask):
  for row in mask:
    if sum(row) == boardSize:
      return True

  for i in range(boardSize):
    checked = 0
    for j in range(boardSize):
      if mask[j][i] == 1:
        checked += 1
      else:
        break
    if checked == boardSize:
      return True

  return False

def fillBoard(board, mask, numbers):
  turns = 0
  for n in numbers:
    turns += 1
    for i in range(boardSize):
      for j in range(boardSize):
        if board[i][j] == n:
          mask[i][j] = 1

    if checkBoardWin(mask):
      return (turns, n)

def getWinningScore(board, mask):
  sum = 0
  for i in range(boardSize):
    for j in range(boardSize):
      if mask[i][j] == 0:
        sum += board[i][j]
  return sum

with open("day4full.txt", "r") as f:
  numLine = f.readline().split(',')
  numbers = [int(num) for num in numLine]
  f.readline()

  while True:
    board = readBoard(f)
    if board == []:
      break
    boards.append(board)

boardMasks = []
for b in boards:
  mask = [ [0] * boardSize for _ in range(boardSize)]
  boardMasks.append(mask)

boardResults = []
for i in range(len(boards)):
  board = boards[i]
  mask = boardMasks[i]
  turns, n = fillBoard(board, mask, numbers)
  score = getWinningScore(board, mask) * n
  boardResults.append((turns, score))

print(sorted(boardResults))
