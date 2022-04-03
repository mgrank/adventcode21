dots = []
folds = []

def printDots(dots):
  w = max(dots, key=lambda d: d[0])[0]
  h = max(dots, key=lambda d: d[1])[1]

  for y in range(h+1):
    for x in range(w+1):
      if (x,y) in dots:
        print('#', sep='', end='')
      else:
        print('.', sep='', end='')
    print()

with open("day13full.txt") as f:
  for line in f:
    line = line.strip()
    if line == '':
      break
    x, y = [int(s) for s in line.split(',')]
    dots += [(x,y)]

  for line in f:
    part = line.split()[2]
    axis, coord = part.split('=')
    folds += [ (axis, int(coord)) ]

print(dots)
print(folds)

for fold, fcoord in folds:
  newDots = []
  for x, y in dots:
    if fold == 'x':
      if x > fcoord:
        x = 2 * fcoord - x
    if fold == 'y':
      if y > fcoord:
        y = 2 * fcoord - y

    newDot = (x, y)
    if newDot not in newDots:
      newDots.append(newDot)
  dots = newDots

print(len(dots))
printDots(dots)

