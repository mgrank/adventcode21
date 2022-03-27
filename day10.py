lines = []
pairs = {'<': '>', '(': ')', '{': '}', '[': ']'}
corruptPrice = {'>':25137, ')':3, '}':1197, ']':57}

with open("day10full.txt") as f:
  for l in f:
    lines.append( l[:-1] )

def checkCorrupt(line):
  stack = []
  for c in line:
    if c in pairs.keys():
      stack.append(c)
    else:
      if len(stack) == 0:
        return ''
      latestStack = stack.pop()
      if pairs[ latestStack ] != c:
        return c
  return None


price = 0
for line in lines:
  res = checkCorrupt(line)
  if res != None and res != '':
    price += corruptPrice[res]

print(price)
