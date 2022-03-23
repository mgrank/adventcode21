from functools import reduce

bitLen = 12
lines = []

with open("day3.txt", "r") as f:
  f2 = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]
  for line in f:
    lines.append( [int(c) for c in line[:-1]] )

#print(lines)

def commonBit(one, two):
  common = [None] * bitLen
  for i in range(bitLen):
    common[i] = one[i] + two[i]
  return common

def list2bin(l):
  res = 0
  for i in range(len(l)):
    res += pow(2, i) * l[-(i+1)]
  return res

def filterO2(l, i):
  if common[i] == 0.5:
    return l[i] == 1
  return l[i] == round(common[i])

def filterCO(l, i):
  if common[i] == 0.5:
    return l[i] == 0
  return l[i] != round(common[i])

workList = lines
for i in range(bitLen):
  print(workList)
  common = reduce(commonBit, workList)
  common = [bit / len(workList) for bit in common]
  newList = []
  for set in workList:
    if filterO2(set, i):
      newList.append(set)
  workList = newList
  if (len(workList) == 1):
    break

print(workList[0])
print(list2bin(workList[0]))

workList = lines
for i in range(bitLen):
  common = reduce(commonBit, workList)
  common = [bit / len(workList) for bit in common]
  newList = []
  for set in workList:
    if filterCO(set, i):
      newList.append(set)
  workList = newList
  if (len(workList) == 1):
    break

print(workList[0])
print(list2bin(workList[0]))