from functools import reduce
from operator import mul
import colorama
colorama.init(autoreset=True)

def printMap(depthMap):
  for i in range(len(depthMap)):
    for j in range(len(depthMap[i])):
      print(colorama.Fore.RED + str( depthMap[i][j] ), sep='', end='')
    print()

depthMap = []

with open("day9full.txt") as f:
  for line in f:
    depthMap.append( list(map(int, list(line[:-1]))) )

#printMap(depthMap)

mapW = len(depthMap[0])
mapH = len(depthMap)

lowestPoints = []
lowestSum = 0

print(mapW, mapH)

def onEdge(i, j):
  if i < 0 or j < 0 or i > mapH - 1 or j > mapW - 1:
    return True
  if depthMap[i][j] == 9:
    return True
  return False

for i in range(mapH):
  for j in range(mapW):
    l = depthMap[i][j-1] if j > 0 else 10
    r = depthMap[i][j+1] if j < mapW - 1 else 10
    u = depthMap[i-1][j] if i > 0 else 10
    d = depthMap[i+1][j] if i < mapH - 1 else 10
    if depthMap[i][j] < min(l, r, u, d):
      lowestPoints.append( (i, j) )
      lowestSum += 1 + depthMap[i][j]

print(lowestSum)

basinMask = [ [0] * mapW for _ in range(mapH) ]

def fillBasin(i, j):
  if onEdge(i, j):
    return 0
  if basinMask[i][j] == 1:
    return 0

  basinMask[i][j] = 1
  return 1 + fillBasin(i+1,j) + fillBasin(i,j-1) + fillBasin(i,j+1) + fillBasin(i-1,j)

basinsSizes = []
for lp in lowestPoints:
  basinsSizes.append( fillBasin(lp[0], lp[1]) )

print( reduce( mul, sorted(basinsSizes, reverse=True)[:3] ) )