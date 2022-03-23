numbers = []
with open("day1.txt", "r") as f:
  for line in f:
    numbers.append(int(line))

cur_depth = 1000000
incr = 0
for i in range(0, len(numbers)-2):
  window = numbers[i] + numbers[i+1] + numbers[i+2]

  if window > cur_depth:
    incr += 1
  cur_depth = window

print(incr)
