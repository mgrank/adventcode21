numbers = []
with open("day1.txt", "r") as f:
  for line in f:
    numbers.append(int(line))

cur_depth = numbers[0]
incr = 0
for i in range(1, len(numbers)):
  if numbers[i] > cur_depth:
    incr += 1
  cur_depth = numbers[i]

print(incr)
