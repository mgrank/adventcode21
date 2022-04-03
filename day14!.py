from collections import Counter
from collections import defaultdict
from math import ceil
rules = {}
with open("day14full.txt") as f:
  template = f.readline().strip()
  f.readline()
  for line in f:
    a, b = [s.strip() for s in line.strip().split('->')]
    rules[a] = b

print(template)
print(rules)

steps = 40

pairCount = {}
for pair in rules.keys():
  pairCount[pair] = 0
zeroPairCount = pairCount.copy()

for i in range( len(template)-1 ):
  chPair = template[i:i+2]
  print(chPair)
  pairCount[chPair] += 1

#print(pairCount)

for step in range(steps):
  newPairCount = zeroPairCount.copy()
  for pair, pCount in pairCount.items():
    newChar = rules[pair]
    newPairCount[ pair[0]+newChar ] += pCount
    newPairCount[ newChar+pair[1] ] += pCount
  pairCount = newPairCount

#print(pairCount)

letters = defaultdict(lambda: 0)
for pair, count in pairCount.items():
  letters[ pair[0] ] += count
  letters[ pair[1] ] += count

c = Counter()
for letter, doubleCount in letters.items():
  c[letter] = ceil( doubleCount / 2 )

slist = c.most_common()

print(slist[0][1] - slist[-1][1])
