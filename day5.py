lines = []
board = dict()

with open("day5full.txt", "r") as f:
  for line in f:
    lsplit = line.split()
    coord = [lsplit[0], lsplit[2]]
    coord = map(lambda s: [int(n) for n in s.split(',')], coord)
    lines.append( list(coord) )

def straightLine(line):
  x1, y1 = line[0]
  x2, y2 = line[1]
  return x1 == x2 or y1 == y2

def sign(n):
  if n > 0:
    return 1
  elif n < 0:
    return -1
  else:
    return 0

#straightLines = list(filter(straightLine, lines))
for line in lines:
  x1, y1 = line[0]
  x2, y2 = line[1]

  if x1 == x2:
    xrange = [x1] * (abs(y1 - y2) + 1)
    yrange = range(min(y1, y2), max(y1, y2) + 1)
  elif y1 == y2:
    xrange = range(min(x1, x2), max(x1, x2) + 1)
    yrange = [y1] * (abs(x1 - x2) + 1)
  else:
    xrange = range(x1, x2 + sign(x2 - x1), sign(x2 - x1))
    yrange = range(y1, y2 + sign(y2 - y1), sign(y2 - y1))

  for coord in zip(xrange, yrange):
      if coord not in board:
        board[coord] = 1
      else:
        board[coord] += 1

intersections = 0
for coords, value in board.items():
  if value > 1:
    intersections += 1

print(intersections)