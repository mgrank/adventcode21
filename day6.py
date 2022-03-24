from functools import reduce

with open("day6full.txt", "r") as f:
  str = f.readline()
  fishes = list(map(int, str.split(',')))

days = 256

fishTable = [[0] * 2]

for d in range(0, days + 7):
  fishTable[0] += [d // 7]


for d in range(days):
  if fishTable[d][-1] == 0:
    break
  newRow = [0] * len(fishTable[d])
  for i in range(1, len(fishTable[d])):
    diff = fishTable[d][i] - fishTable[d][i-1]
    if diff > 0:
      for j in range(i, len(newRow)):
        newRow[j] += fishTable[0][j-i] * diff
  fishTable.append(newRow)

totalFish = reduce(lambda x, y: [ x[i] + y[i] for i in range(len(x)) ], fishTable)
print(totalFish)

sum = 0
for fish in fishes:
  print( totalFish[9-fish:][days-1] + 1 )
  sum += totalFish[9-fish:][days-1] + 1

print(sum)
