depthMap = []

with open("day9full.txt") as f:
  for line in f:
    depthMap.append( list(map(int, list(line[:-1]))) )

print(depthMap[4])

mapW = len(depthMap[0])
mapH = len(depthMap)

lowestSum = 0

print(mapW, mapH)

for i in range(mapH):
  for j in range(mapW):
    l = depthMap[i][j-1] if j > 0 else 10
    r = depthMap[i][j+1] if j < mapW - 1 else 10
    u = depthMap[i-1][j] if i > 0 else 10
    d = depthMap[i+1][j] if i < mapH - 1 else 10
    if depthMap[i][j] < min(l, r, u, d):
      lowestSum += 1 + depthMap[i][j]

print(lowestSum)