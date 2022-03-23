gamma = [None] * 12
epsilon = [None] * 12

ones = [0] * 12
zeroes = [0] * 12

with open("day3.txt", "r") as f:
  for line in f:
    for i in range(12):
      if line[i] == "1":
        ones[i] += 1
      else:
        zeroes[i] += 1

for i in range(12):
  if ones[i] > zeroes[i]:
    gamma[i] = '1'
    epsilon[i] = '0'
  else:
    gamma[i] = '0'
    epsilon[i] = '1'

gammaN = int(''.join(gamma), 2)
epsilonN = int(''.join(epsilon), 2)

print(gammaN * epsilonN)


