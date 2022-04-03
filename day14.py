from collections import Counter

rules = {}
with open("day14.txt") as f:
  template = f.readline().strip()
  f.readline()
  for line in f:
    a, b = [s.strip() for s in line.strip().split('->')]
    rules[a] = b

print(template)
print(rules)

steps = 4

pairCount = {}
for pair in rules.keys():
  pairCount[pair] = 0

for i in range( len(template)-1 ):
  chPair = template[i:i+2]
  print(chPair)
  pairCount[chPair] += 1

print(pairCount)

for step in range(steps):
  newTemplate = []
  for i in range(len(template)-1):
    chPair = template[i:i+2]
    toInsert = rules[chPair]
    newTemplate += [ chPair[0], toInsert ]
  newTemplate.append(template[-1])
  template = ''.join(newTemplate)
  #print(newTemplate)

print( "Template length", len(template) )

counter = Counter(template).most_common()
print(counter)
most_common,num_most_common = counter[0]
least_common,num_least_common = counter[-1]

print(num_most_common - num_least_common)
