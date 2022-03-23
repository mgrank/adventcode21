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

def fillBoards(boards, boardMasks, n):
  for b in range(len(boards)):
    for i in range(boardSize):
      for j in range(boardSize):
        if boards[b][i][j] == n:
          boardMasks[b][i][j] = 1

    if checkBoardWin(boardMasks[b]):
      return b
  return -1

def getWinningScore(b, boards, masks):
  sum = 0
  for i in range(boardSize):
    for j in range(boardSize):
      if masks[b][i][j] == 0:
        sum += boards[b][i][j]

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

for n in numbers:
  winningBoard = fillBoards(boards, boardMasks, n)
  if winningBoard != -1:
    score = getWinningScore(winningBoard, boards, boardMasks) * n
    print(boardMasks[winningBoard])
    print(score)
    break

