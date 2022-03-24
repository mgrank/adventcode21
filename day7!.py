with open("day7full.txt") as f:
  str = f.readline()
  startPos = list(map(int, str.split(',')))

def sign(n):
  if n >= 0:
    return 1
  return -1

middle = int(len(startPos) / 2)
midPos = sorted(startPos)[middle]

def fuelCost(distance):
  cost = 0
  for c in range(1, distance + 1):
    cost += c
  return cost

fuel = 0
for pos in startPos:
  diff = abs(pos - midPos)
  fuel += fuelCost(diff)
print(fuel)

for i in range(20):
  posCopy = startPos.copy()
  for pos in startPos:
    for i in range( midPos + sign(pos - midPos), pos, sign(pos - midPos) ):
      posCopy.append(i)

  fuel = 0
  for pos in posCopy:
    fuel += abs(midPos - pos)

  print(fuel)

  middle = int(len(posCopy) / 2)
  midPos = sorted(posCopy)[middle]