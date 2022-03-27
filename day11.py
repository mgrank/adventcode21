import colorama
colorama.init(autoreset=True)

board = []

with open("day11full.txt") as f:
  for line in f:
    board.append( list(map(int, list(line.strip()))) )

def printBoard(board):
  for row in board:
    for c in row:
      if c == 0:
        print(colorama.Fore.RED + str(c), end='', sep='')
      else:
        print(c, end='', sep='')
    print()
  print()

def directionsList(board,i,j):
  dList = []
  for di in range(i-1, i+2):
    for dj in range(j-1, j+2):
      if di == i and dj == j:
        continue
      if di < 0 or dj < 0 or di > len(board) - 1 or dj > len(board[0]) - 1:
        continue
      dList.append( (di, dj) )
  return dList

def flashOctopus(board, i, j):
  flashes = 1
  board[i][j] = 0
  dList = directionsList(board, i, j)
  for y, x in dList:
    if board[y][x] == 0:
      continue
    board[y][x] += 1
    if board[y][x] > 9:
      flashes += flashOctopus(board, y, x)
  return flashes

def boardStep(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      board[i][j] += 1

  flashes = 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] > 9:
        flashes += flashOctopus(board, i, j)
  return flashes

totalFlashes = 0
printBoard(board)
for i in range(0, 300):
  newFlashes = boardStep(board)
  if newFlashes == len(board) * len(board[0]):
    print("Step", i+1)
    break
  totalFlashes += newFlashes
  print("After step ", i + 1)
  printBoard(board)

print(totalFlashes)