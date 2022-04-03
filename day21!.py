import functools
import itertools

pos = [4, 8]
scores = [0, 0]

diracDie = {}
for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      s = i + j + k
      if s not in diracDie:
        diracDie[s] = 1
      else:
        diracDie[s] += 1

@functools.cache
def rollDiracDice(pos):
  variants = {}
  for k in diracDie.keys():
    npos = pos + k
    if npos > 10:
      npos -= 10
    variants[npos] = diracDie[k]
  return variants

def playGame(pos1, pos2, score1, score2):
  w1 = w2 = 0
  variants = rollDiracDice(pos1)
  for p, c in variants.items():
    if p + score1 >= 21:
      w1 += c
    else:
      pos1 = p
      score1 += p
      nw2, nw1 = playGame(pos2, pos1, score2, score1)
      w1 += nw1
      w2 += nw2
  return w1, w2

print(diracDie)
print(rollDiracDice(8))
variants = rollDiracDice(8)
for p, c in variants.items():
  print(p, c)
print(playGame(4, 8, 0, 0))