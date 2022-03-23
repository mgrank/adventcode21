forw = 0
depth = 0
aim = 0

with open("day2.txt", "r") as f:
  for line in f:
    if line[0] == "f":
      movement = int(line[7:])
      forw += movement
      depth += aim * movement
    elif line[0] == "u":
      movement = int(line[2:])
      aim -= movement
    elif line[0] == "d":
      movement = int(line[4:])
      aim += movement

print(forw * depth)
