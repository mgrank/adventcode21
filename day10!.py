lines = []
pairs = {'<': '>', '(': ')', '{': '}', '[': ']'}
corruptPrice = {'>':25137, ')':3, '}':1197, ']':57}
completePrice = {')':1, ']':2, '}':3, '>':4}

with open("day10full.txt") as f:
  for l in f:
    lines.append( l[:-1] )

def notCorrupt(line):
  stack = []
  for c in line:
    if c in pairs.keys():
      stack.append(c)
    else:
      if len(stack) == 0:
        return False
      latestStack = stack.pop()
      if pairs[ latestStack ] != c:
        return False
  return True

def completeLine(line):
  stack = []
  for c in line:
    if c in pairs.keys():
      stack.append(c)
    else:
      stack.pop()

  stack = list(map(lambda c: pairs[c], stack))
  stack.reverse()
  return stack

def completionCost(str):
  score = 0
  for c in str:
    score = score * 5 + completePrice[c]
  return score



incompleteLines = list(filter(notCorrupt, lines))
scores = []
for l in incompleteLines:
  scores.append( completionCost(completeLine(l)) )

scores.sort()
print(scores[ len(scores)//2 ])

