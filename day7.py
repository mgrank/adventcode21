with open("day7full.txt") as f:
  str = f.readline()
  startPos = list(map(int, str.split(',')))

middle = int(len(startPos) / 2)
midPos = sorted(startPos)[middle]

fuel = 0
for pos in startPos:
  fuel += abs(pos - midPos)

print(fuel)